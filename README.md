Monitoramento de Temperatura e Umidade com Microcontrolador
Imagem do Sensor DHT11

Este repositório contém um projeto de automação que monitora a temperatura e a umidade ambiente usando um microcontrolador (provavelmente um ESP8266 ou ESP32) com um sensor DHT11. Os dados são coletados, processados e enviados para uma API da web com base em determinados critérios de temperatura e umidade.

Funcionalidades
Coleta dados de temperatura e umidade com um sensor DHT11.
Ativa ou desativa um dispositivo (relé) com base em limites de temperatura e umidade.
Conecta-se a uma rede Wi-Fi.
Realiza solicitações HTTP para enviar dados para uma API da web.
Faz isso em um ciclo contínuo para monitoramento constante.
Pré-requisitos
Antes de usar este projeto, você precisará:

Um microcontrolador compatível (como ESP8266 ou ESP32).
Sensor de temperatura e umidade DHT11.
Acesso a uma rede Wi-Fi.
Acesso a uma API da web para enviar os dados de monitoramento, como ThingSpeak.
Ambiente de desenvolvimento configurado, como Thonny IDE em uma máquina virtualizada Linux Oracle VM.
Configuração
Para que o projeto funcione corretamente, siga as etapas abaixo:

Wi-Fi: No código do projeto, configure as credenciais de rede Wi-Fi com as informações do seu próprio Wi-Fi. Substitua "Nome do wifi" e "Senha do Wifi" pelas informações da sua rede.

ThingSpeak: Crie uma conta no ThingSpeak e configure seu próprio canal para armazenar os dados de temperatura e umidade. Obtenha uma chave de API do ThingSpeak e substitua "LINK DA API do FIELD1" e "LINK DA API do FIELD2" no código pelos URLs do seu canal do ThingSpeak.

Chave de API ThingSpeak: Certifique-se de que seu canal no ThingSpeak seja público ou configure as permissões apropriadas para que os dados possam ser acessados.

Uso
Carregue o código no seu microcontrolador.
Configure as credenciais da rede Wi-Fi no código.
Configure a URL da API do ThingSpeak no código para enviar os dados para o seu canal do ThingSpeak.
Defina os critérios de temperatura e umidade no código para controlar o relé.
Execute o projeto no seu microcontrolador.
Enviando Dados para ThingSpeak
Você pode usar o serviço ThingSpeak para armazenar e visualizar os dados de monitoramento. Certifique-se de configurar seu próprio canal e chave de API do ThingSpeak.

Contribuição
Este é um projeto de exemplo e pode ser personalizado para atender às suas necessidades. Sinta-se à vontade para contribuir com melhorias, correções de bugs ou recursos adicionais.
