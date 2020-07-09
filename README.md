# ChordIdentification

# Startup
1. Clone respository 
2. Add file BasicRecognition.py to a python project.

# Converting Notes to Chords
Call function NotesToChords() which takes requires list of notes as an argument. 
The list of notes must be seperated by spaces and all notes should be natural or sharp (convert any flats to sharps) ie. ['c', 'e', 'g']
The output of the function is a dictionary. Each entry will have the root of the chord as the key and the chord type as the value. All entries are potential chord names. ie. {'c': 'Major'}
