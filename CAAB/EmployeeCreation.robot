*** setting ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    String

*** Variables ***
${nameInEnglish}        
${nameInBengali}
${joiningYear}
${image}

*** test cases ***
login
    Open Browser    http://192.168.1.9:8080/caab/login    chrome
    Maximize Browser Window
    Sleep    2s
    Input Text    name=username    test1
    Sleep    2s
    Input Password    name=password    123456
    Sleep    2s
    Click Element    xpath=//body/div[@id='middle']/div[@id='login_panel']/div[2]/div[2]/form[1]/div[5]/div[1]/select[1]
    Sleep    2s
    Click Element    xpath=//option[contains(text(),'0007 - Hazrat Shahjalal International Airport')]
    Sleep    2s
    Click Button    xpath=//input[@id='submit']
    Sleep    2s

    Location Should Be    http://192.168.1.9:8080/caab/home

    #Wait Until Element Contains    xpath=//a[contains(text(),'Human Resource')]    Human Resource

    Click Element    xpath=//a[contains(text(),'Human Resource')]
    Sleep    2s
    Click Element    xpath=//a[contains(text(),'HR Admin')]
    Sleep    2s
    Click Element    xpath=//body/div[@id='resizeContainer']/div[@id='resizeMenu']/div[@id='mCSB_1']/div[1]/div[1]/div[5]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/h4[1]/a[1]
    Sleep    2s
    Click Element    xpath=//a[contains(text(),'Employee ID Creation')]
    Sleep    4s

    ${input}    Get File     EmployeeCreation.txt

    ${English}    ${Bangla}    ${year}    ${picture}=  Split String  ${input} 

    Input Text    Xpath=//input[@id='employeeNameEnglish']    ${English}
    Sleep    2s
    Input Text    Xpath=//input[@id='employeeNameBangla']    ${Bangla}
    Sleep    2s
    Click Element    Xpath=//select[@id='joinYear']
    Sleep    2s
    Click Element    xpath=//option[contains(text(),'${year}')]
    Sleep    2s
    Input Text    xpath=//input[@id='search']    ${picture}
    Sleep    2s
    Click Button    xpath=//input[@id='btnSave']
    Sleep    2s
    Click Button    xpath=//button[contains(text(),'OK')]
    Sleep    2s
    Close All Browsers