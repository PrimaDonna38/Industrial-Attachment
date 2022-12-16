*** setting ***
Library    SeleniumLibrary  
*** Variables ***
${username}       2054901038
${password}       Begood@life1
*** Test Cases ***
login
    Open Browser    https://webportal.bup.edu.bd/    chrome
    Maximize Browser Window
    Sleep    2s
    Input Text    name=UserId    ${username}
    Sleep    2s
    Input Password    name=Password    ${password}
    Sleep    2s
    Click Button    class=login-btn
    Sleep    2s