
# Script för att skapa och flytta fakturor, till ett sk "luftjobb"

Detta projekt använder Python, openpyxl och flask för att tillhandahålla två knappar i en webläsare i samma nätverk som projektet körs. Knapparna kommer att flytta två eller tre fakturor i xlsx-format samt ändra kvantiteterna på de "inhandlade" varorna. Detta gjordes tidigare manuellt men kan nu göras från varsomhelst i samma nätverk.

<br />

> Links

- [Winget](https://learn.microsoft.com/en-us/windows/package-manager/winget/) - Winget
- [Powershell](https://winget.run/pkg/Microsoft/PowerShell) - Winget Powershell
- [Pyenv-win](https://pyenv-win.github.io/pyenv-win/) - Pyenv-win
y



<br />

## The web interface

Gif to demo project.

<br />

![Website preview](https://github.com/betaniahemmet/fakturor/blob/main/media/demo.gif)

<br />

## Build from sources


<br />
Jag rekommenderar att man använder Winget som pakethanterare, Powershell istället för CMD och Pyenv-win istället för att installera senaste Python-versionen. Inget av detta är dock nödvändigt. Nedan följer en enkel beskrivning av hur man gör utan att använda något av detta.
<br />

```bash
$ # Clone the sources
$ git clone https://github.com/betaniahemmet/fakturor.git
$ cd fakturor
$
$ # Virtualenv modules installation (Unix based systems)
$ python3 -m venv "fakturor-env"
$ source fakturor-env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ python -m venv venv
$ .\venv\Scripts\activate
$
$ # Install requirements (Unix based systems)
$ pip3 install -r requirements.txt
$
$ # Install requirements (Windows)
$ pip install -r requirements.txt
$
$
$ # Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=run.py
$ (Windows) set FLASK_APP=run.py
$ (Powershell) $env:FLASK_APP = ".\run.py"
$
$ 
$ # Access the UI in browser: 
$ http://127.0.0.1:5000/
```

<br />



## Credits & Links

- [Flask Framework](https://www.palletsprojects.com/p/flask/) - The official website


<br />


