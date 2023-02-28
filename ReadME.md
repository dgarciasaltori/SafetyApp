# Safety App
## Seja bem-vindo(a) ao Safety App.

Fala pessoal! Tudo bem?

Então este é um caso de estudo sobre como podemos implementar uma API para verificação de vírus utilizando a linguagem Python como ponto de partida.
Para o estudo, foi necessário a criação de uma aplicação que aceite upload de arquivos e salve o mesmo em um banco de dados, para isso utilizei a biblioteca SQLite3. 
Ao inserir o arquivo ele é convertido em bytes para melhor armazenagem e também manipulação do mesmo.
Para a criação do aplicativo estou utilizando a biblioteca PyQt para manipular mesmo que de forma rudimentar inicialmente os: botões, lista, boxes de mensagens e outras funcionalidades visuais da aplicação.
Mas isso não impede de utilizar em nuvem ou até mesmo auxiliar em outra aplicação já criada.

Para efetuar a checagem do arquivo, estou utilizando a API Cloudmersive, que tem opção gratuita com uma limitação de 1 arquivo por segundo e 800 consultas por mês. Por este motivo não estarei deixando a minha API Key aqui no Github, mas para cadastrar é bem simples e não demora nem dois minutos...

Acesse:  https://www.cloudmersive.com/

Clique em: "Signup" e preencha o formulário ou também é possível utilizar a sua conta Google ou Microsoft.
Você receberá um e-mail para confirmação, basta clicar no link e fazer login no site novamente (Pode ser que nem seja necessário conectar novamente).

Em seu dashboard escolha a opção API Keys, e clicar em seguida no botão de Create Key. Pronto, basta copiar e colar na aplicação.

Para buscar as bibliotecas em caso de dúvida utilize o site: PyPi.org

Para verificar se esta funcionando tudo, precisaremos de um arquivo infectado.

## Alerta! Caso não saiba o que esta fazendo, dê uma pesquisada antes, mas não deixe de tentar, pois é importante para o aprendizado de como manter uma aplicação segura.
Bem existe no diretório test_files deste repositório um arquivo .txt com o nome ‘trojan’ basta copiar a linha de código abaixo (copie apenas o que está dentro dos: >>> <<<)

Código Trojan: >>> X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H* <<<
Salve o arquivo.

É provável ter que desligar seu antivírus e também o Windows Defender, como eles vão detectar o arquivo, já sabemos que está funcionando.

## DESATIVE seus recursos de antivírus 
# (CUIDADO!! NÃO SE ESQUEÇA DE ATIVÁ-LOS NOVAMENTE APÓS CONCLUIR O ESTUDO!!)

### Para melhor instrução estarei deixando um video, basta acessar usando o link abaixo:
## Link YouTube:

# Safety App
## Welcome to the Safety App.

Speak guys! All good?

So this is a study case on how we can implement an API for virus check using Python language as a starting point.
For the study, it was necessary to create an application that accepts file upload and save it in a database, so I used the SQLite3 library3.
When inserting the file it is converted to bytes for better storage and also manipulation of it.
For the creation of the application I am using the PYQT library to manipulate even if initially rudimentary: buttons, list, messaging boxes and other visual features of the application.
But this does not prevent cloud use or even help with another application already created.

To check the file, I am using the Cloudmersive API, which has a free option with a limitation of 1 file per second and 800 queries per month. For this reason I will not be leaving my Key Api here at Github, but to register is very simple and does not take even two minutes ...

Visit: https://www.cloudmersive.com/

Click: "Signup" and fill out the form or you can also use your Google or Microsoft account.
You will receive an email for confirmation, just click on the link and log in to the site again (you may not even need to connect again).

In your Dashboard choose the API Keys option, and then click the Create Key button. Ready, just copy and paste in the application.

To seek libraries in case of doubt use the site: pypi.org

To check if everything is working, we will need an infected file.

## Alert! If you don't know what you are doing, take a survey before, but be sure to try, as it is important for learning how to maintain a safe application.
Well there is a directory test_files in this repository a file .txt with the name 'trojan' just copy the code line below (copy only what is within: >>> <<<)

Trojan Code: >>> x5o! P%@ap [4 \ pzx54 (p^) 7cc) 7} $ eicar-standard-antivirus-test-file! $ H+h* <<<
Save the file.

It is likely to have to turn off your antivirus and also Windows Defender, as they will detect the file, we already know it is working.

## Disable your antivirus resources
# (Be careful !! Do not forget to activate them again after completing the study !!)

### For better instruction I will be leaving a video, just access using the link below:
## Link YouTube:
