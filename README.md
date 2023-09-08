
# Script för att skapa och flytta fakturor, för ett sk "luftjobb"

Detta projekt använder Python, openpyxl, flask och waitress för att tillhandahålla två knappar i en webläsare i samma nätverk som projektet körs. Knapparna kommer att flytta två eller tre "fakturor" i xlsx-format samt ändra kvantiteterna på de "inhandlade" varorna. Be nätverksteknikern om att få fast ip till datorn som kör detta så blir det lätt att hålla ordning på vilket ip som ska skrivas in i webläsaren för att nå webgränssnittet. Pga waitress så bör man använda windows. 
<br />

## The web interface

Gif to demo project.

<br />

![Website preview](https://github.com/betaniahemmet/fakturor/blob/main/media/demo.gif)

<br />

## Build from sources


<br />
Man bör ha Python 3.10 eller senare.
<br />

```bash
$ # Clone the sources
$ git clone https://github.com/betaniahemmet/fakturor.git
$ cd fakturor
$
$ # Install requirements (Windows)
$ pip install -r requirements.txt
$
$ # Start the app (Windows)
$ python app.py
$ 
$ # Access the UI in browser: 
$ http://localhost:5000/
$
$
$ # ...or preferably get your network technician
$ to manually assign a static IP to the MAC address
$ of the computer running this. That IP can then be
$ used in any browser in the same network. If this is
$ not done, the DHCP might assign a different IP
$ when the computer is restarted.
```

<br />



## Credits & Links

- [Flask Framework](https://www.palletsprojects.com/p/flask/) - The official website
- [OpenPyXL](https://openpyxl.readthedocs.io/en/stable/) - Documentation
- [Pillow](https://pillow.readthedocs.io/en/stable/) - Documentation
- [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/index.html) - Documentation

<br />


