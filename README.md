[README.md](https://github.com/user-attachments/files/33356959/README.md)
# Monitoring

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Ein schlankes Web-Dashboard im Container, das Systemauslastung (CPU, RAM und Speicher) sowie Hardware-Spezifikationen in Echtzeit anzeigt. Mit Streamlit und psutil geschrieben, als Docker-Image ausgeliefert und per GitHub Actions automatisch gebaut.

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
| **Python 3.13** | Programmiersprache |
| **Streamlit** | Web-Oberfläche |
| **psutil** | Auslesen der Systemdaten |
| **Docker** | Containerisierung |
| **GitHub Actions** | CI-Pipeline |

## Struktur/Dateienpfad:

```
Monitoring/
├── .github/workflows/
│   └── ci.yml             # CI: Docker-Build bei Push auf main
├── app.py                 # Monitoring-Anwendung
├── Dockerfile             # Container-Image
├── requirements.txt       # Abhängigkeiten
└── README.md
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
*Die Werte beziehen sich auf den Docker-Container!*

#### Lokal auf Windows App nutzen (Ohne Docker):

(Voraussetzung: Python 3.10 oder neuer)

 **In Powershell**

```bash
git clone https://github.com/aleks-dabkowski/Monitoring.git 
cd Monitoring 
pip install -r requirements.txt
streamlit run app.py
```

App kann dann unter http://localhost:8080/ (oder dem Port welcher im Terminal ausgegeben wird) abgerufen werden

## CI-Pipeline:

Der Workflow ci.yml läuft bei jedem Push zu GitHub auf main:

Hierbei wird:

1. Code mit actions/checkout@v4 ausgecheckt
2. Das Docker-Image mit docker build -t monitoring-app:latest . mit der neusten Dockerfile gebaut. 

Ist der Build fehlerhaft, zeigt sich der Workflow rot. Gelingt dieser, kommt ein grünes Häkchen. Somit lassen sich sofort Probleme erkennen um diese so schnellst und automatisiert beheben zu können. 
