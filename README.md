<h1><div align='center'>Telas de Monitoração - Hospital 9 de Julho</div></h1>
<div align='center'>
    <img src="http://img.shields.io/static/v1?label=python%20&message=3.8.3&color=blue&logo=python"/>
    <img src="http://img.shields.io/static/v1?label=Selenium%20&message=3.141.0&color=green"/>
    <img src="http://img.shields.io/static/v1?label=VS Code%20&message=1.47.3&color=blue&logo=visual-studio-code"/>
    <img src="http://img.shields.io/static/v1?label=status%20&message=Em%20andamento&color=yellow"/>
</div>


### Tópicos Abordados :scroll:
- Introdução 
- Pré-requisitos 
    - Requirements.txt
    - Arquivo .crx
- Configurações de tela
- Sites acessados
- Funcionamento 
- Dificuldades/Desafios

### Introdução :rocket:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Este projeto foi baseado em uma solicitação de um técnico da empresa Microblau, residente no Hospital 9 de Julho.</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Aparentemente, o técnico demorava cerca de 21 minutos para acessar e logar nas páginas que deveriam ser monitoradas. Por isso, a partir da minha ideia de agilizar o meu processo de configuração na [central BMS da Microblau](https://github.com/HenriqueSaKi/OxynG5-AUT-SCREEN), ele viu a oportunidade de solicitar a implementação do mesmo no Hospital 9 de Julho.</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Com essa implementação, foi possível obter um ganho de 80,9% de produtividade nesse processo, ou seja, onde era gasto um tempo de 21 minutos, passou a ser 4 minutos. Sem contar com a possibilidade de realizar outras tarefas em meio à execução do programa.

### Pré-requisitos :pushpin:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Após realizar o download dos arquivos desse projeto, será necessário editar o código, aplicando os dados de acesso (login e senha), nos campos destacados com comentários no código.</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Após editar os campos de acesso, o arquivo já poderá ser executado normalmente. No entanto, dessa forma o computador deverá possuir o Python e suas bibliotecas instaladas.</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Caso opte por essa primeira opção, após instalar o Python e adicioná-lo ao seu Path, no **prompt de comando**, acesse a pasta do arquivo e execute o seguinte comando:</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Comando para acessar a pasta: ```cd <local do arquivo>```</br>

<div align= 'center'>

```pip install -r requirements.txt```

</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Isso fará com que todas as bibliotecas aplicadas nesse projeto, sejam instaladas com apenas um único comando.</br></br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Agora, no meu caso, não havia possibilidade de instalar o Python no computador do Hospital 9 de Julho, por isso, procurei uma forma de criar um arquivo executável para que ele pudesse operar de forma *standalone*.</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A solução encontrada, foi utilizar o *framework* ```pyinstaller```, que é uma ferramenta responsável por transformar os arquivos python em executáveis, a partir do comando a seguir:</br>
<div align='center'>

```py -m pyinstaller <nome do arquivo.py> --onefile```

</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Com isso, gerei um arquivo capaz de rodar em qualquer computador, mesmo não contendo nenhuma versão do Python instalada.

### Configurações de tela :wrench:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Recomenda-se que as telas possuam o tamanho padrão de 1920x1080, pois assim é possível garantir que as etapas que são executadas pela biblioteca ```pyautogui```, sejam mais garantidas. (*Ex: Habilitação da extensão, posicionamento das telas*)


### Sites acessados :link:
- [Microsoft Online](https://login.microsoftonline.com/)
- [Netvmi](http://netvmi.com.br/)
- [Oxyn G5](https://g5.oxyn.com.br/)
- [Power BI](https://app.powerbi.com/)
- [Powerhub](http://site.powerhub.io/)
- [Projeto - Central BMS Microblau](https://github.com/HenriqueSaKi/OxynG5-AUT-SCREEN)

### Funcionamento :arrow_forward:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Para que a execução das telas seja bem sucedida, o arquivo ```.crx```, deve estar contido dentro da mesma página do programa ```.exe``` criado pelo pyinstaller, pois esse arquivo será responsável por abrir o chromedriver com a extensão *Revolver Tabs* já habilitado.

### Dificuldades / Desafios :muscle:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A programação por um todo, foi bem tranquila, visto que os maiores aprendizados foram adquiridos no primeiro projeto da [central BMS da Microblau](https://github.com/HenriqueSaKi/OxynG5-AUT-SCREEN). </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No entanto, é possível citar duas dificuldades encontradas.</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A primeira delas, foi no posicionamento das telas. Como nunca havia visto como eram realizados a transição de uma tela à outra, inicialmente houveram diversos retrabalhos, até que foi decidido que por motivos de produtividade, teríamos um maior ganho se eu realizasse essas configurações pessoalmente.</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O segundo problema encontrado foi na programação do iframe, no site [Powerhub](http://site.powerhub.io/), onde o mesmo não estava sendo reconhecido, fazendo com que eu mudasse o xpath procurado, por um outro mais detalhado.</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Os dois problemas foram corrigidos e o programa encontra-se finalizado e rodando no Hospital 9 de Julho.
