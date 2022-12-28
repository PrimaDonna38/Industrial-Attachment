*** Settings ***
Library    OperatingSystem 
Library    String
Library    SeleniumLibrary   

*** Variables ***
${user}    ayesha
${pasword}    123456

*** Test Cases ***
login
    
    Open Browser    http://192.168.1.9:8080/caab/login    chrome
    
    Maximize Browser Window
    
    Input Text    name=username    ${user}
    Sleep    1s
    
    Input Password    name=password    ${pasword}
    Sleep    1s
    
    Click Element    xpath=//body/div[@id='middle']/div[@id='login_panel']/div[2]/div[2]/form[1]/div[5]/div[1]/select[1]
    Sleep    1s
    
    Click Element    xpath=//option[contains(text(),'0007 - Hazrat Shahjalal International Airport')]
    Sleep    1s
    
    Click Button    xpath=//input[@id='submit']
    Sleep    1s

    Location Should Be    http://192.168.1.9:8080/caab/home
    
    Click Element    xpath=//a[contains(text(),'Human Resource')]
    Sleep    1s    
    
    Click Element    xpath=//a[contains(text(),'HR Payroll')]
    Sleep    1s
    
    Click Element    xpath=//body/div[@id='resizeContainer']/div[@id='resizeMenu']/div[@id='mCSB_1']/div[1]/div[1]/div[5]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/h4[1]/a[1]
    Sleep    1s
    
    Click Element    xpath=//body/div[@id='resizeContainer']/div[@id='resizeMenu']/div[@id='mCSB_1']/div[1]/div[1]/div[5]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[4]/a[1]
    Sleep    1s
    
    Click Element    xpath=//a[contains(text(),'Deductions')]
    Sleep    1s

    Location Should Be    http://192.168.1.9:8080/caab/hrpAllowanceDeduction
    
    ${input}     Get File    AllowanceDeduction.txt
    ${variable1}    ${variable2}    ${variable3}    ${variable4}    ${variable5}    ${variable6}    ${variable7}    ${variable8}    ${variable9}    ${variable10}    ${variable11}    ${variable12}    ${variable13}    ${variable14}    ${variable15}=  Split String  ${input}
    
    Sleep    4s

    Click Element    xpath=//select[@id='month'] 
    Sleep    2s
    
    Click Element    xpath=//option[contains(text(),'${variable1}')]
    Sleep    2s
    
    Click Element    xpath=//select[@id='year']
    Sleep    2s
    
    Click Element    xpath=//option[contains(text(),'${variable2}')]
    Sleep    3s
    
    Input Text    name=employeeId    ${variable3}
    Sleep    2s

    Click Element    xpath=//input[@id='groupInsurance']
    Sleep    2s
    
    Input Text    name=groupInsurance    ${variable4}
    Sleep    2s
    
    Input Text    name=benevolentFund    ${variable5}
    Sleep    2s
    
    Input Text    name=gPFAmount    ${variable6}
    Sleep    2s
    
    Input Text    name=gPFAmountAccountNo    ${variable7}
    Sleep    3s
    
    Input Text    name=incomeTax    ${variable8}
    Sleep    3s
    
    Input Text    name=houseRent    ${variable9}
    Sleep    2s
    
    Input text    name=houseRentMaintenance    ${variable10}
    Sleep    2s
    
    Input Text    name=electricalBill    ${variable11}
    Sleep    2s
    
    Input Text    name=waterAndSewerageBill    ${variable12}
    Sleep    2s
    
    Input Text    name=gas    ${variable13}
    Sleep    2s
    
    Input Text    name=mtCharge    ${variable14}
    Sleep    2s
    
    Input Text    name=stampFee    ${variable15}
    Sleep    2s
    
    Click Button    id=btnSaveDeduction   
    Sleep    4s

    Close All Browsers
