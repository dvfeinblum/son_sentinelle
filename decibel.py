# Borrowed (with love) from 
# https://stackoverflow.com/a/70514219

import pyaudio
from pprint import pprint
from math import log10
import audioop

from utils.plot import Plot

p = pyaudio.PyAudio()
WIDTH = 2
RATE = int(p.get_default_input_device_info()['defaultSampleRate'])
DEVICE = p.get_default_input_device_info()['index']
rms = 1
pprint(p.get_default_input_device_info())


def callback(in_data, frame_count, time_info, status):
    global rms
    rms = audioop.rms(in_data, WIDTH) / 32767
    return in_data, pyaudio.paContinue


if __name__ == "__main__":
    stream = p.open(format=p.get_format_from_width(WIDTH),
                    input_device_index=DEVICE,
                    channels=1,
                    rate=RATE,
                    input=True,
                    output=False,
                    stream_callback=callback)

    stream.start_stream()

    p = Plot(0.1)

    while stream.is_active() and p.can_step:
        db = 20 * log10(rms) + 54
        print(f"RMS: {rms} DB: {db}")
        p.take_step(db)

    stream.stop_stream()
    stream.close()

    p.show(block=True)
