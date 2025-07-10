# REST-Full-API
<h1>1 Idee</h1> 
Flask ist ein Webframework, das in Python entwickelt wurde. Es legt seinen Schwerpunkt auf Erweiterbarkeit und umfassende Dokumentation. Die einzigen Softwareabhängigkeiten sind Jinja2, eine Template-Engine, und Werkzeug, eine Softwarebibliothek zur Erstellung von WSGI-Anwendungen. Hier muss eine RESTful API entwickelt werden, und die Benutzer (Client) müssen über HTTP-Anfragen auf die Daten zugreifen können. Die Daten sind persistent in einer Datenbank (Datagrip) gespeichert. Es geht um Eigenschaften von Autos, die in der Datenbank abgelegt sind. Hier kann der Benutzer HTTP-Anfragen wie POST, PUT, DELETE und GET senden, um Autos hinzuzufügen, zu löschen, Autoseigenschaften zu bearbeiten oder einfach die Eigenschaften eines Autos abzurufen. Jedes Auto hat folgende Eigenschaften:

➠ id 

➠ Marke

➠ Baujahr

➠ Preis

➠ Farbe 

➠ Getriebe

➠ Geschwindigkeit


<h1>2 Software</h1> 

➠ Visual Studio Code:
Ist ein kostenloser Texteditor von Microsoft, der auf verschiedenen Betriebssystemen wie Windows, macOS und Linux läuft. Er nutzt das Electron-Framework und bietet zahlreiche Funktionen wie Syntaxhervorhebung, Code-Faltung, Debugging, automatisches Vervollständigen und Versionskontrolle.


➠ Datagrip:
Ist ein Datenbank-Tool, das speziell auf die Bedürfnisse von SQL-Entwicklern zugeschnitten ist. Arbeitet intelligent mit SQL- und NoSQL-Datenbanken zusammen.

<br />
<img src="https://i.imgur.com/YiOOPlL.png" style="max-width:100%; height:auto; display:block; margin:auto;" alt="Disk Sanitization Steps"/>
<br />

➠ Postman:
Postman stellt eine proprietäre Plattform für Programmierschnittstellen (APIs) dar, auf der Entwickler die Möglichkeit haben, ihre APIs zu entwerfen, zu erstellen, zu testen und weiterzuentwickeln. In diesem Projekt wird Postman verwendet, um die REST-API zu testen.

<h1>3 Test der RESTful API mit Postman</h1> 
<h2>3.1 Neues Auto hinzufügen dank POST-Anfrage </h2> 
In folgendem Formular werden die Eigenschaften des Autos erfasst. Die API ist dafür zuständig, diese Daten in der Datenbank zu speichern, sodass sie später abgerufen, gelöscht oder bearbeitet werden können. <br />

<br />
<img src="https://i.imgur.com/RFbiodq.png" style="max-width:100%; height:auto; display:block; margin:auto;" alt="Disk Sanitization Steps"/>
<br />
<img src="https://i.imgur.com/5Tzl4bl.png" style="max-width:100%; height:auto; display:block; margin:auto;" alt="Disk Sanitization Steps"/>
<br />


<h2>3.2 Auto abrufen dank seiner Id mit GET Anfrage  </h2> 

Hier kann man ein Auto dank seiner Id abrufen werden. In diesem Beispiel wird ein Auto mit ID 10 abgerufen werden und das entspricht das Auto, das vorher hinzugefügt wurde.

<br />
<img src="https://i.imgur.com/zfnHFld.png" style="max-width:100%; height:auto; display:block; margin:auto;" alt="Disk Sanitization Steps"/>
<br />


<h2>3.3 Auto Eigenschaften modifizieren dank PUT Http-Anfrage  </h2> 

Hier kann man ein Auto dank seiner Id modifiziert werden. In diesem Beispiel wird ein Auto mit ID 10 modifiziert und zwar die Farbe von grau zu blau.

<br />
<img src="https://i.imgur.com/I5YTvtg.png" style="max-width:100%; height:auto; display:block; margin:auto;" alt="Disk Sanitization Steps"/>
<br />

<h2>3.4 Auto löschen dank seiner Id</h2> 

Hier kann man ein Auto dank seiner Id gelöscht werden. In diesem Beispiel wird ein Auto mit ID 10 gelöscht  und das entspricht das Auto, das vorher hinzugefügt wurde.

<br />
<img src="https://i.imgur.com/XLVDA4Q.png" style="max-width:100%; height:auto; display:block; margin:auto;" alt="Disk Sanitization Steps"/>
<br />
