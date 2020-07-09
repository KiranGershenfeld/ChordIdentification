raw = []
#Function declarations
def rawToNotes(raw):
    notes = []
    for note in raw:
        if note not in notes:
            notes.append(note) #Get rid of duplicates
    return notes
def getRootNoteArray(root):
    localAllNotes = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"]
    for i in localAllNotes:
        if(i == root):
            for x in range(localAllNotes.index(i)):
                localAllNotes.append(localAllNotes[0])
                localAllNotes.remove(localAllNotes[0])
            return localAllNotes #Rearranges all 12 notes to begin with the root note
def createIntervalDictionary(array):
    allIntervals = ["0", "m2", "M2", "m3", "M3", "P4", "TT", "P5", "m6", "M6", "m7", "M7"]
    intervalDictionary = {}
    for i in range(len(array)):
        intervalDictionary[array[i]] = allIntervals[i]
    return intervalDictionary #Creates a dictionary of every note and its corresponding interval to the root note
def notesToIntverals(noteArray, dict):
    intervals = []
    for note in noteArray:
        for entry in dict:
            if (note == entry):
                intervals.append(dict[entry])
    return intervals #Creates a list that is the intervals of the raw notes in relation to the root note
def getIntervalDictionary():
    twoNote = {}
    #Not Using Two Note Intervals Anymore-- twoNote = {"Minor 2nd Interval" : ["0", "m2"], "Major 2nd Interval" : ["0", "M2"], "Minor 3rd Interval" : ["0", "m3"], "Major 3rd Interval" : ["0", "M3"], "Perfect 4th Interval" : ["0", "P4"], "TriTone Interval" : ["0", "TT"], "Perfect 5th Interval" : ["0", "P5"], "Minor 6th Interval" : ["0", "m6"], "Major 6th Interval" : ["0", "M6"], "Minor 7th Interval" : ["0", "m7"], "Major 7th Interval" : ["0", "M7"]}
    threeNote = {"Major" : ["0", "M3", "P5"], "Minor" : ["0", "m3", "P5"], "Augmented" : ["0", "M3", "m6"],"Diminished" : ["0", "m3", "TT"], "Sus 2" : ["0", "M2", "P5"], "Sus 4" : ["0", "P4", "P5"]}
    fourNote = {"Major 7" : ["0", "M3", "P5", "M7"], "Minor 7" : ["0", "m3", "P5", "m7"], "Dominant 7" : ["0", "M3", "P5", "m7"], "Diminished 7" : ["0", "m3", "TT", "M6"], "Minor(Maj 7)" : ["0", "m3", "P5", "M7"], "Minor 7 b5" : ["0", "m3", "TT", "m7"], "6" : ["0", "M3", "P5", "M6"]}
    fiveNote = {"Major 9" : ["0", "M3", "P5", "M7", "M2"], "Minor 9" : ["0", "m3", "P5", "m7", "M2"], "9" : ["0", "M3", "P5", "m7", "M2"], "6/9" : ["0", "M3", "P5", "M6", "M2"], "11" : ["0", "M3", "P5", "m7", "P4"], "13" : ["0", "M3", "P5", "m7", "M6"]}
    twoNote.update(threeNote)
    twoNote.update(fourNote)
    twoNote.update(fiveNote)
    return twoNote
def intervalsToChords(data):
    matchingChords = []
    combinedDict = getIntervalDictionary()
    for chordName in combinedDict: #loops over each chord possible
        chordIntervals = combinedDict[chordName] #grabs the list of intervals for that chord
        if(checkIntervalMatch(data, chordIntervals)): #Checks to see if the intervals in that chord exist in the data
            matchingChords.append(chordName)

    return matchingChords
def checkIntervalMatch(data, chordIntervals):
    for note in chordIntervals: #Loops over each interval in the chord that we are checking
        if(note not in data): #If the chord has an interval that isnt in the data, return false
            return False
    return True #If every interval in the chord is met in the data, return true
def getLengthOfBiggestChordInList(chordList):
    intervaldict = getIntervalDictionary()
    return len(intervaldict[chordList[-1]])
def trimEmptyDictEntries(dict):
    updatedDict = {}
    for entry in dict:
        if(len(dict[entry]) != 0):
            updatedDict[entry] = dict[entry]
    return updatedDict
def getAllMatchingChords(notes): #Cycle through evert root note to find all potential chords
    allNotes = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"]
    keyMatchingDict = {}
    for rootNote in allNotes:
        rootArray = getRootNoteArray(rootNote)
        intDict = createIntervalDictionary(rootArray)
        intervals = notesToIntverals(notes, intDict)
        matchingChords = intervalsToChords(intervals)
        keyMatchingDict[rootNote] = matchingChords
    return keyMatchingDict
def getBiggestChordLength(validChords): #This gets the length of the biggest chord contained within each key in the dictionary
    max = 0
    for entry in validChords:
        length = getLengthOfBiggestChordInList(validChords[entry])
        if(length >= max):
            max = length
    return max
def createChordOptions(validChords, max): #Creates the final list of chord options
    chordOptions = {} #Dictionary of highest order chords that fit the given notes, ALl of these will be good answers
    for entry in validChords: #This checks which keys have a chord of max value and adds those chords to the final chord options dictionary
        if(getLengthOfBiggestChordInList(validChords[entry]) == max):
            chordOptions[entry] = validChords[entry][-1]
    return chordOptions

def NotesToChords(raw):
    notes = rawToNotes(raw)
    keyMatchingDict = getAllMatchingChords(notes) #Dictionary of every key and the chords in that key that match the notes
    validChords = trimEmptyDictEntries(keyMatchingDict) #Gets rid of any keys with no matching chords
    max = getBiggestChordLength(validChords)
    chordOptions = createChordOptions(validChords, max)
    return chordOptions #Runs the program, turning a list of chords into a dictionary of keys with godo matching chords
