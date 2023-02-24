#Requires AutoHotkey v2.0

Home::
{
Run "cmd.exe"
WinWait "ahk_exe" "cmd.exe"
Send "cd\ {enter}"
Send "cd C:\Users\henri\Documents\code\fakturor {enter}"
WinWait "ahk_exe" "cmd.exe"
Send "venv\Scripts\activate.bat {enter}"
Send "python fakturor.py {enter}"


;"C:\Users\henri\Documents\code\fakturor\venv\Scripts\python.exe" "C:\Users\henri\Documents\code\fakturor\fakturor.py" 
}
return
