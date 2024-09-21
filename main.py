import os
import time

import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('audio.wav')
sound.play()

def pause():
  pygame.mixer.pause()
  
pause()

def play():
  # Play the sound
  pygame.mixer.unpause()
  while True:
    # Start taking user input and doing something with it
    stop_playback = int(input("Press 2 anytime to stop playback and go back to the menu: "))
    if stop_playback == 2:
      pause()
      return
    else:
      continue

while True:
  # clear the screen 
  os.system("clear")
  # Show the menu
  print("🎵 MyPOD Music Player")
  print()
  time.sleep(1)
  print("Press 1 to Play")
  time.sleep(1)
  print("Press 2 to Exit")
  time.sleep(1)
  print()

  # take user's input
  print("Press anything else to see the menu again")
  userInput = int(input())
  
  # check whether you should call the play() subroutine depending on user's input
  if userInput == 1:
    play()
  elif userInput == 2:
    exit()
  else:
    continue
