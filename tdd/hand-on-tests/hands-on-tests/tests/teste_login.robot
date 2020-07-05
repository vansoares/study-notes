*** Settings ***
Library  SeleniumLibrary
Documentation  Testes no login do predict
...
...            Teste parágrafo

*** Test Cases ***
Login com sucesso no PredictCovid
    Abrir o site do predict
    Escpera o predict carregar 
    Clicar em acessar
    Esperamos carregar 
    Insiro meu e-mail 
    Insiro minha senha 
    Clico no botão de login
    Fechar navegador

*** Keywords ***
Abrir o site do predict
    Open Browser        https://predictcovid.com.br     firefox
    Set Window Size     1080    720
    Set Selenium Implicit Wait  5

Esperar o predict carregar
    Wait Until Element Is Visible       css:a[href='/home/']    timeout:5

Clicar em acessar
Esperamos carregar 
Insiro meu e-mail 
Insiro minha senha 
Clico no botão de login
Fechar navegador
    Capture Page Screenshot
    Close Browser