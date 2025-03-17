# SoftwareEngineering24
Creating this repository is an exercise for our Software Engineering course.

## Describing a fictional use case:

### Name und Identifikationsnummer
UC 1.07. - Abbruch des Leistungstests

### Beschreibung
Sicheres herunterfahren und Speicherung der Daten, falls frühzeitig Fehler erkannt werden oder aufgrund eines Notfalls.

### Beteligte Akteure
Diagnostiker:in, Proband:in

### Status
Anforderungen erfüllt, benötigt jedoch noch weiteres Testing, sowie Feedback vom Kunden.

### Verwendete
- UC 1.02. Leistungstest anlegen
- UC 1.05. Laktatmessung eingeben

### Auslöser
- Stopp Knopf am Ergometer
- Diagnostiker:in bricht Leistungstest frühzeitig ab
- Sonstige kritische Störungen

### Vorbedingungen
Leistungstest muss laufen

### Invarianten
Aufgezeichnete Daten müssen gespeichert werden

### Nachbedingungen/Ergebnis
Ein neuer Leistungstest muss erstellt werden können

### Standardablauf
Es wurde eine falsche Einstellung getroffen. Der/die Diagnostiker:in beendet den Leistungstest, speichert die aufgezeichneten Daten und startet einen neuen Leistungstest.

### Alternative Ablaufschritte

### Hinweise

### Änderungsgeschichte
0.01: 17.03. 2025.: Moritz Mattes
