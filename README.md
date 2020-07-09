# ChordIdentification
This python project converts a list of notes (as strings) into a dictionary of potential chord names for that set of notes. It also does live midi analysis of what chord is being played from a standard midi keyboard.
# Startup
1. Clone respository 
2. Add file BasicRecognition.py to a python project.

# Converting Notes to Chords
Call function NotesToChords() which takes requires list of notes as an argument. 
The list of notes must be seperated by spaces and all notes should be natural or sharp (convert any flats to sharps) ie. ['c', 'e', 'g'].  
The output of the function is a dictionary. Each entry will have the root of the chord as the key and the chord type as the value. All entries are potential chord names. ie. {'c': 'Major'}

# Live Midi Analysis
Midi channels will depend on the particular instrument and midi channels being used so this will require some tweaking.

1. Ensure that BasicRecognition.py and MidiNotes.py are in the same folder.
2. Run MidiNotes.py in an IDE or directly from the console.
3. Any Midi devices plugged in should be recongized automatically and playing a chord should print the name of the chord to the console.
4. Please let me know there are issues, pygame doesnt always play nice.
