import time
import winsound
import random

def metronome(bpm, bpb, start):
     delay = 0.733333*60.0/bpm
     # div = 60.0
     count = 0
     # status = "On beat"
     print delay
     while start==True:
          rhythmCompare(delay,bpb)
          # print status
          if count % bpb == 0:
               winsound.SND_NOSTOP
               winsound.Beep(1200, int(delay*300))
               print "A"
          else:
               winsound.SND_NOSTOP
               winsound.Beep(600, int(delay*300))
               print "a"
          count = count + 1
          time.sleep(delay)
     
def rhythmCompare(delay,bpb): #to be modified asfter the frequency input is connected
     status = ""
     for i in range(0,int(delay*100),25):
          # if playerNote[0] != playerNote[1] and i%bpb != 0:
          #           status = "Speeding up"
          # elif playerNote[0] != playerNote[1] and i%bpb == 0:
          #      status = "On beat"
          # else:
          #      status = "Slowing down "
          status = "Compare"
          print status
           
def main():
     bpm = input("Enter the tempo (bpm) here: ")
     bpb = input("Enter the number of beats in a measure: ")
     start = True
     # playerNotes = [0,1] Will be updated after frequency input is connected
     for i in range(0,25):
          metronome(bpm, bpb, start)

main()
