*** setting ***
Library    SeleniumLibrary  
*** Variables ***
${username}       2054901014
${password}       Bismillah@14
*** Test Cases ***
login
    Open Browser    https://webportal.bup.edu.bd/    chrome
    Maximize Browser Window
    Sleep    2s
    Input Text    name=UserId    ${username}
    Sleep    2s
    Input Text    name=Password    ${password}
    Sleep    2s
    Click Button    class=login-btn

