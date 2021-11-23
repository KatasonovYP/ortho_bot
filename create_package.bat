@echo off

del bot_pkg.zip
mkdir template
xcopy src template /s/e/
move template\server_main.py template\lambda_function.py
7z a -tzip bot_pkg.zip .\template\*

rmdir /s/q template
