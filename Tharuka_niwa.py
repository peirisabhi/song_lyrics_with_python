import sys
import time

CYAN = '\033[36m'
RESET = '\033[0m'

print(CYAN + "Tharuka Niwa Lyrics!" + RESET)

lyrics = [
    "තාරුකා නිවා දුර ඈත තනි වෙලා",
    "කොහේ ගියාද දිව්යාංගනා",
    "ජීවිතේ කියා පෙරදාක රැවටිලා",
    "මගේ නොවේද දිව්යාංගනා",
    "නික්මී නොයා මහදේ දොර වසා",
    "හදේ රැඳෙන්න දිව්යාංගනා",
    "ළං වී ඉඳින්න දිව්යාංගනා..."
]

def display_lyrics(line, callback=None):
    for char in line:
        sys.stdout.write(CYAN + char + RESET)
        sys.stdout.flush()
        time.sleep(0.21)
    sys.stdout.write('\n')
    if callback:
        callback()

def sing_song(lines, current_line=0):
    if current_line < len(lines):
        display_lyrics(
            lines[current_line],
            lambda: sing_song(lines, current_line + 1)
        )

sing_song(lyrics)
