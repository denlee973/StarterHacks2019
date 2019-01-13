import time
import winsound
import random

def metronome(bpm, bpb, start, playerNote):
     delay = 0.733333*60.0/bpm
     # div = 60.0
     count = 0
     # status = "On beat"
     print delay
     while start==True:
          rhythmCompare(delay, playerNote,bpb)
          # print status
          if count % bpb == 0:
               winsound.SND_NOSTOP
               winsound.Beep(1200, int(delay*300))
          else:
               winsound.SND_NOSTOP
               winsound.Beep(600, int(delay*300))
          count = count + 1
          time.sleep(delay)
     
def rhythmCompare(delay, playerNote,bpb):
     status = ""
     for i in range(0,int(delay*1000),25):
          if playerNote[0] != playerNote[1] and i%bpb != 0:
                    status = "Speeding up"
          elif playerNote[0] != playerNote[1] and i%bpb == 0:
               status = "On beat"
          else:
               status = "Slowing down "
          print status

           
def main():
     bpm = input("Enter the tempo (bpm) here: ")
     bpb = input("Enter the number of beats in a measure: ")
     start = True
     for i in range(0,25):
          metronome(bpm, bpb, start, playerNotes)

main()
