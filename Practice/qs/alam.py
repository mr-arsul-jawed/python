from datetime import datetime
import time
import pygame
import os

# Initialize pygame mixer for audio
pygame.mixer.init()

# Function to play the alarm sound
def play_alarm_sound():
    audio_file = 'D:/Music/Allah Hafiz.mp3'
    
    if not os.path.isfile(audio_file):
        print(f"Error: The file '{audio_file}' does not exist.")
        return
    
    try:
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
        print("Playing alarm sound...")
    except pygame.error as e:
        print(f"Error loading audio file: {e}")

# Function to validate the time format (HH:MM:SSAM/PM)
def validate_time_format(alarm_time):
    try:
        datetime.strptime(alarm_time, "%I:%M:%S%p")
        return True
    except ValueError:
        return False

# Get the alarm time from the user
while True:
    alarm_time = input("Enter the time for the alarm (HH:MM:SSAM/PM): \n")
    if validate_time_format(alarm_time):
        break
    else:
        print("Invalid time format! Please enter the time in HH:MM:SSAM/PM format.")

# Extract hour, minute, second, and period from the input
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[8:].upper()

print("Setting up alarm...")

# Check the current time continuously
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")

    # Trigger the alarm when the time matches
    if (alarm_period == current_period and
        alarm_hour == current_hour and
        alarm_minute == current_minute and
        alarm_seconds == current_seconds):
        print("Wake Up!")
        play_alarm_sound()  # Play the alarm sound
        
        # Wait for the alarm sound to finish playing
        while pygame.mixer.music.get_busy():
            time.sleep(1)
        break
    
    time.sleep(1)  # Wait for 1 second before checking the time again
