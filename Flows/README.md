# Nodered flows 
- Flow 2 Tjørring dataopsamling 
- Flow 3 Kontakt med API
- Flow 4 MQTT til python script


- flow 2 . Data indsamling (MQTT In)
MQTT Input Node lytter på emnet 00-02-01-aa-53-bd med QoS 2
Modtager data fra en enhed og sender det videre til to funktioner
2. Databehandling (Function 1)
Denne funktion transformerer rå JSON-data til læseligt format:

Parser JSON hvis det kommer som tekst
Tæller heartbeats (livstegn fra enheden)
Dekoder hexadecimal data til faktiske værdier:
værdier:
Tryk: Bytes 0-1 → konverteres til bar (delt med 100)
Temperatur: Bytes 2-3 eller 4-5 → konverteres til °C (delt med 10 eller 100 afhængig af port)
Output er et struktureret objekt med alle sensordata
3. Første formatering (Function 2)
Plukker trykværdier ud fra alle kilder
Navngiver dem Sensor 1 til Sensor 9
Tilføjer TSensor 2 og TSensor 4 (temperaturdata fra specifikke sensorer)
4. Sensor-opdeling (Functions 3-11)
Hver funktion ekstrakter én sensor ad gangen:

Sætter msg.topic til sensornavnet (fx "Sensor 1")
Sætter msg.payload til værdien


5. Dashboard visualisering
Data sendes til UI Charts:

"Tryk (Bar)" - søjlediagram med alle trykværdier
"Temperatur S2 (C)" - linjediagram med sensor 2's temperatur
"Temperatur S4 (C)" - linjediagram med sensor 4's temperatur
6. Cloud upload (Function 12 + 13)
Function 12: Formaterer data til ThingSpeak-format (p1, p2, t1, osv.)
Function 13: Bygger GET-request til ThingSpeak API med alle 8 felter
Data gemmes i cloud for historik og analyse
7. Data samling (Join Node)
Samler Sensor 2 og TSensor 2 data sammen før de sendes til ThingSpeak