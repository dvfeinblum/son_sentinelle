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
    # Set up stream to mic
    stream = p.open(format=p.get_format_from_width(WIDTH),
                    input_device_index=DEVICE,
                    channels=1,
                    rate=RATE,
                    input=True,
                    output=False,
                    stream_callback=callback)

    stream.start_stream()

    # fetching data every 0.08s
    plot = Plot(0.08)

    try:
        while stream.is_active():
            db = 20 * log10(rms) + 54
            print(f"t: {plot.t} DB: {db} RMS: {rms}")
            plot.take_step(db)
    except KeyboardInterrupt:
        print("Wrapping stuff up")
        plot.dump_data()
        stream.stop_stream()
        stream.close()
        exit()
