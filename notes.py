import sys
import pygame
import pygame.midi
from pygame.midi import midi_to_ansi_note
from music21 import chord
import BasicRecognition

pygame.init()
pygame.midi.init()
 # list all midi devices
for x in range( 0, pygame.midi.get_count() ):
    print (pygame.midi.get_device_info(x))

# open a specific midi device
inp = pygame.midi.Input(1)


def number_to_note(number):
    notes = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']
    return notes[number%12]

held_notes = []
previousName = ""
# run the event loop
while True:
    if inp.poll():
        # no way to find number of messages in queue
        # so we just specify a high max value

        #print (inp.read(1000))
        shell = inp.read(1)
        event = shell[0]
        data = event[0]
        timestamp = event[1]
        note_status = data[0]
        note_number = data[1]
        velocity = data[2]
        #print("timestamp: ",timestamp)
        #print("note_number: ",note_number)
        #print("velocity: ",velocity)
        #print ("numtonote: ", number_to_note(note_number), "velocity: ",velocity)
        #print("midi to ansi note: ", midi_to_ansi_note(note_number))
        note_name = midi_to_ansi_note(note_number)
        if (note_status == 144):
            held_notes.append(note_name)
            temp_notes = []
            for note in held_notes:
                note = note[:-1].lower()
                temp_notes.append(note)
            potentialChords = BasicRecognition.NotesToChords(temp_notes)
            if(inp.poll() == False):
                if(potentialChords != previousName):
                    chordString = ""
                    chordList = []
                    for chord in potentialChords:
                        chordList.append(chord.upper() + " " + potentialChords[chord])
                    print(*chordList, sep = ", or ")
                    previousName = potentialChords

                #print("Currently held notes ", held_notes)
        if (note_status == 128):
            held_notes.remove(note_name)


    # wait 10ms - this is arbitrary, but wait(0) still resulted
    # in 100% cpu utilization
    pygame.time.wait(50)
