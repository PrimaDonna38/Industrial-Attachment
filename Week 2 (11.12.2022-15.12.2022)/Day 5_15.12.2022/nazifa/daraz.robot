*** setting ***
Library    SeleniumLibrary  
*** Variables ***
${search}       mouse

*** Test Cases ***
login
    Open Browser    https://www.daraz.com.bd/    chrome
    Maximize Browser Window
    Sleep    2s
    Input Text    name=q    ${search}
    Sleep    2s
    Click Element    xpath=//*[@id='topActionHeader']/div/div[2]/div/div[2]/form/div/div[2]/button
    Sleep    2s
    Click Element    xpath=//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/span[1]  
    Sleep    2s
    Click Element    xpath=/html/body/div[6]/div/div/div/ul/li[3]/div
    Sleep    2s
    Click Element    xpath=//*[@id='root']/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div[1]/div/a/img
    Sleep    2s
    Click Button    xpath=//body/div[@id='container']/div[@id='root']/div[@id='block-F4KXhLDUKR']/div[@id='block-w3Jz3V-dNP']/div[@id='block-nmb82fpO-P']/div[@id='block-sWqtrZRyI2']/div[@id='module_add_to_cart']/div[1]/button[2]
    Sleep    2s