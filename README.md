[README.md](https://github.com/user-attachments/files/33356959/README.md)
# Monitoring

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Das hier ist ein schlankes Web-Dashboard im Container, das Systemauslastung (CPU, RAM und Speicher) sowie Hardware-Spezifikationen in Echtzeit anzeigt. Ich habe es mit Streamlit und psutil geschrieben, als Docker-Image ausgeliefert und per GitHub Actions automatisch gebaut.

## Features:

#### Systemauslastung (In Echtzeit aktualisiert):

- CPU-Auslastung in %
- RAM-Auslastung in %
- Speichernutzung in %
- Freier Speicherplatz in GB
  
(Anzeige aktualisiert sich automatisch im Sekundentakt)

#### System-Spezifikationen

- Logische & physische CPU-Kerne
- Gesamter Arbeitsspeicher und Speicherplatz in GB

## Tech-Stack

-----------------------------------------------

| Komponente | Zweck |
|---|---|
| **Python 3.13**    | Die verwendete Programmiersprache |
| **Streamlit**      | Sorgt für die Web-Oberfläche |
| **psutil**         | Zum Auslesen der Systemdaten |
| **Docker**         | Für die Containerisierung |
| **GitHub Actions** | Für die CI-Pipeline |

## Struktur/Dateienpfad:

```
Monitoring/
|---- .github/workflows/
|   '--- ci.yml              # CI: Docker-Build bei Push auf main
|---- app.py                 # Monitoring-Anwendung
|---- Dockerfile             # Container-Image
|---- requirements.txt       # Abhängigkeiten
|---- README.md
```


## Installation & Start:

#### Mit Docker:

(Voraussetzung: Docker Desktop)

```bash
git clone https://github.com/aleks-dabkowski/Monitoring.git
cd Monitoring
docker build -t monitoring-app:latest . 
docker run -d -p 8080:8080 --name monitoring monitoring-app:latest
```

### **Achtung:** 
*Falls die App auf dem Docker-Container läuft, bezieht sich psutil auf die Werte des Containers!*

#### Lokal auf Windows App nutzen (Ohne Docker):

(Voraussetzung: Python 3.10 oder neuer)

 **In Powershell**

```bash
git clone https://github.com/aleks-dabkowski/Monitoring.git 
cd Monitoring 
pip install -r requirements.txt
streamlit run app.py
```

Die App kann dann unter http://localhost:8080/ (oder dem Port welcher im Terminal ausgegeben wird) abgerufen werden

## CI-Pipeline:

Der Workflow ci.yml läuft bei jedem Push zu GitHub auf main:

Hierbei wird:

1. Code mit actions/checkout@v4 ausgecheckt
2. Das Docker-Image mit docker build -t monitoring-app:latest . mit der neusten Dockerfile gebaut. 

Ist der Build fehlerhaft, zeigt sich der Workflow rot. Gelingt dieser, kommt ein grünes Häkchen. Somit lassen sich Probleme sofort erkennen damit ich diese so schnellst wie möglich beheben kann. 


## Sinn dieses Projekts:

Ich wollte lernen, wie man Anwendungen in einen Container packt, per Push auf GitHub hochlädt und automatisch bauen lässt. Somit kann ich auch sicherstellen, dass andere das Projekt so reibungslos wie möglich ausführen können. Zudem kann ich jederzeit weiteres mit psutil in die App schreiben um zusätzliche Messwerte hinzuzufügen, die bei Bedarf gebraucht wären.
