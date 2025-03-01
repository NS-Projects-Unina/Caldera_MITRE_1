# Caldera_MITRE_1
Sviluppo di una "ability" Caldera MITRE.

Il progetto utilizza la piattaforma di adversary emulation Caldera MITRE per simulare un attacco ad una macchina target, al fine di ottenere le sequenze di input da tastiera della vittima.
In particolare, è stato creato un Adversary profile costituito da due "ability" custom. 
La prima ricade nella categoria "execution" in quanto comporta l'esecuzione di codice malevolo, ovvero il payload "keylogger.py", incorporato nella stessa ability.
Il malware in questione è un semplice registratore delle battiture scritto in Python attraverso la libreria "pynput".
La relativa tecnica nella matrice MITRE ATT&CK è "Input Capture: Keylogging"(https://attack.mitre.org/techniques/T1056/001). I dati catturati vengono collezionati nel file locale "keylog.txt" creato dal payload stesso.
Quest'ultimo viene scaricato dalla macchina vittima, tramite l'agent Sandcat, e successivamente eseguito.
Dopodichè, entra in gioco la seconda ability, di tipo "exfiltration" (https://attack.mitre.org/techniques/T1048). Questa permette il vero e proprio recupero del file contenente i dati rubati, verso il server Caldera controllato dall'esecutore della simulazione.



