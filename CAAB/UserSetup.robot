* Settings *
Library    SeleniumLibrary
Library    OperatingSystem
Library    String

*** Variables ***
${U_name}       test2
${U_pass}       123456
${U_name2}      tasmia
${U_pass2}      123456

* Test Cases *
Login
    Open Browser    http://192.168.1.9:8080/caab/login    chrome
    Maximize Browser Window
    Sleep    2s

    Input Text    name=username    ${U_name}
    Sleep    2s

    Input Password    name=password    ${U_pass}
    Sleep    2s

    Click Element    name=branchCode
    Sleep    2s

    Click Element    xpath=//option[contains(text(),'0000 - CONSOLIDATED CAAB')]
    Sleep    2s

    Click Element    xpath=//input[@id='submit']
    Sleep    2s
    
    Location Should Be    http://192.168.1.9:8080/caab/home
    
    Wait Until Element Contains    xpath=//a[contains(text(),'Security Administration')]    Security Administration
   
   
    Click Element    xpath=//a[contains(text(),'Security Administration')]
    Sleep    2s

    Click Element    xpath=//a[contains(text(),'User Access')]
    Sleep    2s

    Click Element    xpath=//a[contains(text(),'User Setup')]
    Sleep    2s

    ${input}  Get File  UserSetup.txt
    ${User_ID}  ${Password}  ${Confirm_Password}  ${Group}   ${Branch}=  Split String  ${input}    \n
    
    Log To Console    ${User_ID}
    Log To Console    ${Password}
    Log To Console    ${Confirm_Password}
    Log To Console    ${Group}
    Log To Console    ${Branch}
    
    Location Should Be    http://192.168.1.9:8080/caab/userSetup

    Input Text    name=userID    ${User_ID}
    Sleep    3s
    

    Click Element    xpath=//input[@id='userPassword']
    Sleep    2s

    Input Text    xpath=//input[@id='userPassword']    ${Password}
    Sleep    3s
    

    Click Element    name=userConfirmPassword
    Sleep    2s

    Input Text    name=userConfirmPassword    ${Confirm_Password}
    Sleep    3s


    Click Element    name=userGroupID
    Sleep    3s
    Click Element    xpath=//option[contains(text(),'${Group}')]
    Sleep    3s

    Click Element    name=userDefaultBranchCode
    Sleep    3s
    Click Element    xpath=//option[contains(text(),'${Branch}')]
    Sleep    5s
    
    Click Button    xpath=//input[@id='btnSave']
    Sleep    6s


    Click Button    xpath=//button[contains(text(),'OK')]
    Sleep    5s

    
    Click Element    xpath=//header/div[2]/div[1]/div[2]/a[1]
    
    Location Should Be    http://192.168.1.9:8080/caab/login
    
    Input Text    name=username    ${U_name2}
    Sleep    2s

    Input Password    name=password    ${U_pass2}
    Sleep    2s

    Click Element    name=branchCode
    Sleep    2s

    Click Element    xpath=//option[contains(text(),'0000 - CONSOLIDATED CAAB')]
    Sleep    2s

    Click Element    xpath=//input[@id='submit']
    Sleep    2s

    Location Should Be    http://192.168.1.9:8080/caab/home
    
    Wait Until Element Contains    xpath=//a[contains(text(),'Security Administration')]    Security Administration
   
    Click Element    xpath=//a[contains(text(),'Security Administration')]
    Sleep    2s

    Click Element    xpath=//a[contains(text(),'User Access')]
    Sleep    2s

    Click Element    xpath=//a[contains(text(),'Activate User')]
    Sleep    2s

    Input Text    name=userID    ${User_ID}
    Sleep    2s
    
    Click Element    xpath=//body/div[@id='resizeContainer']/div[@id='resizeBody']/form[@id='activateUserForm']/div[1]/fieldset[1]/div[1]/div[1]/div[2]/a[1]
    Sleep    2s

    Click Element    name=userEnabledYN
    Sleep    2s

    Click Button    xpath=//input[@id='btnSave']
    Sleep    2s

    Click Button    xpath=//button[contains(text(),'OK')]
    Sleep    2s

    Click Element    xpath=//header/div[2]/div[1]/div[2]/a[1]
    Sleep    2s

    Close All Browsers
