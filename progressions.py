#Some experiments regarding chord progressins

def CreateListOfProgressions():
    listOfProgressions = ["I-V-IV-iv", "iim7-V7-Imaj7"]
    tempList = []
    for element in listOfProgressions:
        individualProgression = element.split("-")
        tempList.append(individualProgression)
    return(tempList)

def buildChordTypes():
    romanNumerals = ["I", "II", "III", "IV", "V", "VI", "VII"]
    chordTypes = []
    for rm in romanNumerals:
        chordTypes.append(rm)
        chordTypes.append(rm.lower())
        chordTypes.append(rm+"7")
        chordTypes.append(rm.lower()+"7")
        chordTypes.append(rm + "maj7")

    #print(chordTypes)
    return chordTypes

def FindScaleKeys(tonic):
    allKeys = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    tonicIndex = allKeys.index(tonic)
    allKeys = allKeys[tonicIndex:-1] + allKeys[0: tonicIndex+1]
    scaleKeys = allKeys[0] +  allKeys[2] +  allKeys[4] +  allKeys[5] +  allKeys[7] +  allKeys[9] + allKeys[11]
    #print(scaleKeys)
    return scaleKeys

def ConvertChordsToScaleDegrees(currentProgression, tonic):
    chordTypeDict = {"Major": "", "Minor" : "", "7" : "7", "Major 7":"maj7", "Minor 7":"m7", "Minor Major 7":"mMaj7",  "Major Minor 7":"Mm7", "Augmented":"aug", "Diminished": "dim", "Sus 2":"sus2", "Sus 4":"sus4"} #THis dictionary pairs chord names with their scale degree symbols
    romanNumeralDict = {0: "I", 1: "II", 2: "III", 3: "IV", 4: "V", 5:"VI", 6:"VII"}
    scaleKeys = FindScaleKeys(tonic)
    scaleDegreeProgression = []
    for chord in currentProgression:
        scaleDegree = ""
        if not chord:
            scaleDegree = ""
        else:
            if(chord[1] == "Minor" or chord[1] == "Minor Major 7" or chord[1] == "Diminished"):
                scaleDegree += romanNumeralDict[scaleKeys.index(chord[0])].lower() + chordTypeDict[chord[1]]
            else:
                scaleDegree = romanNumeralDict[scaleKeys.index(chord[0])] + chordTypeDict[chord[1]]
        scaleDegreeProgression.append(scaleDegree)
    #print(scaleDegreeProgression)
    return scaleDegreeProgression

def ConvertScaleDegreesToChords(currentProgression, tonic):
    #Input looks like this (["I7", "Vaug", "IVm7", "vi"], "C")
    romanNumeralDict = {0: "I", 1: "II", 2: "III", 3: "IV", 4: "V", 5: "VI", 6: "VII"}
    modifierDict = {0: "I", 1: "II", 2: "III", 3: "IV", 4: "V", 5: "VI", 6: "VII"}
    romanNumeralDict = {v: k for k, v in romanNumeralDict.items()}
    matchingStrings = ["dim", "aug", "VII", "vii", "III", "iii", "VI", "vi", "IV", "iv", "II", "ii", "m7", "V", "v", "I", "i", "7", ] #This is ordered in string size so the largest strins always get prioritized
    scaleKeys = FindScaleKeys(tonic)
    #print(scaleKeys)
    scaleDegreeProgression = []
    for chord in currentProgression:
        chordType = ""
        modifiers = ""
        for str in matchingStrings:
            if(str in chord):
                if(str.upper() in romanNumeralDict.keys()):

                    chordType += (scaleKeys[romanNumeralDict[str.upper()]])
                    chordType += "" if str.isupper() else "m"
                    chord = chord.replace(str, "")
                else:
                     modifiers += str
                     chord = chord.replace(str, "")

        scaleDegreeProgression.append(chordType + " " + modifiers)
    print(scaleDegreeProgression)
    return scaleDegreeProgression

def MatchingIndices(currentProgression, potentialProgression):
    #This function needs to check whether or not the currentProgression appears in the potentialProgression at any point
    for i in range(len(potentialProgression) - len(currentProgression) + 1):
        for chord in currentProgression:
            if(chord != potentialProgression[currentProgression.index(chord) + i] and chord != ""):
                return False
        return True

#print(MatchingIndices(["I", "", "V", ""], ["I", "IV", "V", "vi"]))

def SuggestChords(currentProgression, tonic):
    #Find the tonic of the current chords, if we are given the tonic then that is the only one
    potentialTonics = []
    if(tonic == "unknown"):
        print("THIS CASE HAS NOT BEEN ACCOUNTED FOR YET")
        return None
        #potentialTonics = FindPotentialTonics()
    else:
        potentialTonics.append(tonic)

    scaleDegreeProgression = []
    for tonic in potentialTonics:
        scaleDegreeProgression.append(ConvertChordsToScaleDegrees(currentProgression, tonic))

    currentProgression = scaleDegreeProgression
    listOfProgressions = CreateListOfProgressions()

    potentialProgressions = []
    for element in currentProgression: #Most of the time this is just one element, its only a real loop if there is no root and more htan one potential tonic
        for progression in listOfProgressions:
            if(len(progression) >= len(element)):
                if(MatchingIndices(element, progression)):
                    potentialProgressions.append(progression)

    chordNameProgression = []
    for progression in potentialProgressions:
        chordNameProgression.append(ConvertScaleDegreesToChords(currentProgression, tonic))

    potentialProgressions = chordNameProgression

    print(potentialProgressions)
    return potentialProgressions

#DEBUG TESTING
#SuggestChords takes in a list in which each entry is a list containing the note and quality, and the root of the progression
#SuggestChords([["C", "Major"], ["G", "7"], []], "C")
