*** setting ***
Library    SeleniumLibrary   

*** Variables ***
${search}         mouse
*** test cases***
login
   Open Browser    https://www.daraz.com.bd/    chrome
   Maximize Browser Window
   Sleep    2s
   Input Text    name=q   ${search}
   Sleep    2s
   Click Button    class=search-box__button--1oH7
   Sleep    2s
   Click Element    xpath=//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]
   Sleep    2s
   Click Element    xpath=//div[contains(text(),'Price high to low')]
   Sleep    5s
   Click Element    xpath=//*[@id='root']/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div[1]/div/a/img
   Sleep    2s
   Click Button    xpath=//body/div[@id='container']/div[@id='root']/div[@id='block-F4KXhLDUKR']/div[@id='block-w3Jz3V-dNP']/div[@id='block-nmb82fpO-P']/div[@id='block-sWqtrZRyI2']/div[@id='module_add_to_cart']/div[1]/button[2]
   Sleep    2s
