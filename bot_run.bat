@echo off

call %~dp0venv\Scripts\activate

@REM set TOKEN=2108958665:AAE8AYpXY0aEIOdXU3wWR0Tz2aSrl67cwuk
set TOKEN=2102552647:AAGnhnq4_B_K_bzT072rJADoWuJYFCCfh-o

set PATH_TO_DATA=src\data\data.json

python src\locale_main.py

pause