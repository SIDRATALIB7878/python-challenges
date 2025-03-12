import streamlit as st
import time
import datetime
import threading
import pygame

# Initialize pygame mixer for sound
pygame.mixer.init()

def play_sound(sound_file):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

def alarm_thread(alarm_time, sound_file):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            st.session_state['alarm_triggered'] = True
            play_sound(sound_file)
            break
        time.sleep(1)

def main():
    st.title("⏰ Streamlit Alarm Clock")
    
    # Initialize session state variables
    if 'alarms' not in st.session_state:
        st.session_state['alarms'] = []
    if 'alarm_triggered' not in st.session_state:
        st.session_state['alarm_triggered'] = False
    
    # User input for alarm time
    alarm_time = st.text_input("Set alarm time (HH:MM:SS):", "07:30:00")
    sound_file = st.file_uploader("Upload a custom alarm sound (MP3)", type=["mp3"])
    
    if st.button("Set Alarm"):
        if sound_file is not None:
            sound_path = f"temp_sound.mp3"
            with open(sound_path, "wb") as f:
                f.write(sound_file.read())
            st.session_state['alarms'].append((alarm_time, sound_path))
            threading.Thread(target=alarm_thread, args=(alarm_time, sound_path), daemon=True).start()
            st.success(f"Alarm set for {alarm_time}")
        else:
            st.error("Please upload a sound file.")
    
    # Snooze button
    if st.session_state['alarm_triggered']:
        if st.button("Snooze for 5 minutes"):
            snooze_time = (datetime.datetime.strptime(alarm_time, "%H:%M:%S") + datetime.timedelta(minutes=5)).strftime("%H:%M:%S")
            threading.Thread(target=alarm_thread, args=(snooze_time, sound_path), daemon=True).start()
            st.session_state['alarm_triggered'] = False
            st.success(f"Alarm snoozed until {snooze_time}")
    
    # Display active alarms
    st.subheader("Active Alarms")
    for alarm in st.session_state['alarms']:
        st.write(f"⏰ Alarm set for {alarm[0]}")
    
if __name__ == "__main__":
    main()
