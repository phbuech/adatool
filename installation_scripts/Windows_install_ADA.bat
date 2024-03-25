ECHO This script installs a Python distribution [3.11], an environment and the dependencies for ADA using conda. Please follow the instructions.
ECHO Do you want to execute the installation script [yes/no]?
SET /p "reply=reply: "
IF %reply%==yes (
    CALL C:\Users\%USERNAME%\anaconda3\Scripts\activate base
    IF EXIST C:\Users\%USERNAME%\anaconda3\envs\ada_env\ (
        ECHO Remove ada environment
        ECHO y | CALL conda remove --name ada_env --all        
    )
    ECHO install ada environment
    ECHO y | CALL conda create --name ada_env Python=3.11
    ECHO Activate ada environment
    CALL conda activate ada_env
    ECHO Install dependencies
    ECHO y | CALL pip3 install -r %~dp0\requirements.txt

    ) else ( ECHO Ada environment not installed. )


ECHO Ada environment installed

pause