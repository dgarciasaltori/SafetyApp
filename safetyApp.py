##################################################################################
#                       Code by: Diego Garcia Saltori                            #
#                       UTF-8        https://saltori.dev                         #
#                       Lang: PT-BR                                              #
#                       Version: 1.0                                             #
##################################################################################
#                       Importar Bibliotecas                                     #
#                                                                                #
##################################################################################
import os
import io
from io import StringIO
import sys
import sqlite3
import cloudmersive_virus_api_client
from cloudmersive_virus_api_client.rest import ApiException
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QFileDialog, QPushButton, QListWidget
from PyQt5.QtWidgets import QApplication, QListWidgetItem, QWidget, QHBoxLayout, QVBoxLayout, QAbstractItemView

class FileUploader(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        # Conecta com o banco de dados
        self.conn = sqlite3.connect('files.db')
        self.cursor = self.conn.cursor()
        # Cria a tabela se ela não existe
        self.cursor.execute('CREATE TABLE IF NOT EXISTS files (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, path TEXT, data BLOB)')
        # Atualiza a lista de arquivos
        self.refresh_files()

    def initUI(self):
        # Cria a lista de arquivos
        self.files_list = QListWidget()
        # Permite seleção múltipla com checkbox
        self.files_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        # Cria os botões
        self.upload_btn = QPushButton('Verificar Arquivo')
        self.remove_btn = QPushButton('Remover')
        # Conecta os botões aos métodos
        self.upload_btn.clicked.connect(self.upload_file)
        self.remove_btn.clicked.connect(self.remove_file)
        # Criando o Layout 
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.upload_btn)
        buttons_layout.addWidget(self.remove_btn)
        layout = QVBoxLayout()
        layout.addWidget(self.files_list)
        layout.addLayout(buttons_layout)
        # Criando o Layout da Janela
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        # Define as propriedades da janela
        self.setWindowTitle('Safety App - V1.0 - @Diego.Saltori')
        self.setGeometry(100, 100, 500, 500)
        # Conecta o sinal itemChanged para tratar o checkbox
        self.files_list.itemChanged.connect(self.handle_item_change)
        # Conecta o evento de fechar a janela ao método closeEvent
        self.closeEvent = self.closeEvent

    def handle_item_change(self, item):
        # Define uma coluna checkbox para cada item
        item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
        item.setData(Qt.CheckStateRole, Qt.Unchecked)
        self.refresh_files()

    def get_files(self):
        # Consulta o banco de dados e retorna uma lista com os caminhos dos arquivos
        self.cursor.execute('SELECT path FROM files')
        return [row[0] for row in self.cursor.fetchall()]

    def refresh_files(self):
        # Limpa a lista de arquivos e preenche com os arquivos do banco de dados
        self.files_list.clear()
        for file_path in self.get_files():
            # Obtem o nome do arquivo a partir do caminho completo
            file_name = os.path.basename(file_path)
            # Cria um objeto QListWidgetItem com o nome do arquivo
            list_item = QListWidgetItem(file_name)
            # Adiciona o caminho do arquivo como um atributo do item
            list_item.path = file_path
            # Adiciona o item na lista de arquivos
            self.files_list.addItem(list_item)

    def checkVirus(self, file_path):
        # Configurando API key authorization: Apikey
        configuration = cloudmersive_virus_api_client.Configuration()
        configuration.api_key['Apikey'] = 'API-KEY'
        # Cria a instancia com a API Cloudmersive
        api_instance = cloudmersive_virus_api_client.ScanApi(cloudmersive_virus_api_client.ApiClient(configuration))
        try:
            # Scan do arquivo apontando para a função de upload
            api_response = api_instance.scan_file(file_path)
            print(api_response)
        except ApiException as e:
            print("Exception when calling ScanApi->scan_file: %s\n" % e)

    def capture_stdout(func, *args, **kwargs):
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(f"An exception occurred: {str(e)}")
        sys.stdout = old_stdout
        return result.getvalue()

    def upload_file(self):
        # Abre uma janela de diálogo para selecionar o arquivo
        file_path, _ = QFileDialog.getOpenFileName(self, 'Selecionar arquivo', '', 'Todos os arquivos (*.*)')
        if file_path:
            # Abre o arquivo e lê seu conteúdo
            with open(file_path, 'rb') as file:
                file_content = file.read()
            # Insere o arquivo no banco de dados
            file_name = os.path.basename(file_path)
            self.cursor.execute('INSERT INTO files (name, path, data) VALUES (?, ?, ?)', (file_name, file_path, file_content))
            self.conn.commit()
            # verifica se o arquivo contém vírus
            # Criar um objeto io.StringIO
            output_buffer = io.StringIO()
            # Redirecionar a saída padrão para o objeto io.StringIO
            sys.stdout = output_buffer
            result_str = self.checkVirus(file_path)
            # Restaurar a saída padrão
            sys.stdout = sys.__stdout__
            # Obter o conteúdo do objeto io.StringIO como uma string
            result_str = output_buffer.getvalue()
            QMessageBox.information(None, 'Resultado da verificação', f'Resultado da verificação do arquivo {file_path}:\n\n{result_str}')
            self.refresh_files()

    def remove_file(self):
        # Verifica se algum arquivo foi selecionado
        if self.files_list.currentItem():
            # Remove o arquivo do banco de dados
            item = self.files_list.currentItem()
            self.cursor.execute('DELETE FROM files WHERE path=?', (item.path,))
            self.conn.commit()
            # Remove o item da lista de arquivos
            self.files_list.takeItem(self.files_list.row(item))

    def closeEvent(self, event):
        #Criando a caixa de dialogo de saida da aplicação
        reply = QMessageBox.question(
            self,
            'Sair...',
            'Tem certeza que deseja sair?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication([])
    file_uploader = FileUploader()
    file_uploader.show()
    app.exec_()