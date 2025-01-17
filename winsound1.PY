import winsound
import time
def play_note(frequency, duration):
    winsound.Beep(frequency, duration)
notes = [
    392, 392, 440, 392, 523, 493, 0, 392, 392, 440, 392, 523, 493, 0,
    392, 392, 784, 659, 523, 493, 440, 0, 587, 587, 523, 493, 466, 440
]
durations = [
    500, 500, 500, 500, 500, 1000, 500, 500, 500, 500, 500, 1000,
    500, 500, 500, 500, 500, 1000, 500, 500, 500, 500, 500, 1000,
    ]
for i in range(len(notes)):
    if notes[i] != 0:
        play_note(notes[i], durations[i])
    else:
        time.sleep(durations[i] / 1000.0)
