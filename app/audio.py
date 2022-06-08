import pyaudio


audio = pyaudio.PyAudio()
FORMAT = pyaudio.paInt16
CHUNK = 1024
RATE = 44100
BITS_PER_SAMPLE = 16
CHANNELS = 1
DEVICE_NAMES = [
    "default",
    # "pulse",
    # "USB Audio Device: - (hw:2,0)",
]


device_index = 1
for i in range(audio.get_device_count()):
    dev = audio.get_device_info_by_index(i)
    name = dev["name"]
    print(i, name)
    if name in DEVICE_NAMES:
        print("Using audio device", i, name, dev)
        device_index = i


def genHeader(sampleRate, bitsPerSample, channels, samples):
    datasize = 10240000  # Some veeery big number here instead of: #samples * channels * bitsPerSample // 8
    o = bytes("RIFF", "ascii")  # (4byte) Marks file as RIFF
    o += (datasize + 36).to_bytes(
        4, "little"
    )  # (4byte) File size in bytes excluding this and RIFF marker
    o += bytes("WAVE", "ascii")  # (4byte) File type
    o += bytes("fmt ", "ascii")  # (4byte) Format Chunk Marker
    o += (16).to_bytes(4, "little")  # (4byte) Length of above format data
    o += (1).to_bytes(2, "little")  # (2byte) Format type (1 - PCM)
    o += (channels).to_bytes(2, "little")  # (2byte)
    o += (sampleRate).to_bytes(4, "little")  # (4byte)
    o += (sampleRate * channels * bitsPerSample // 8).to_bytes(4, "little")  # (4byte)
    o += (channels * bitsPerSample // 8).to_bytes(2, "little")  # (2byte)
    o += (bitsPerSample).to_bytes(2, "little")  # (2byte)
    o += bytes("data", "ascii")  # (4byte) Data Chunk Marker
    o += (datasize).to_bytes(4, "little")  # (4byte) Data size in bytes
    return o


wav_header = genHeader(RATE, BITS_PER_SAMPLE, CHANNELS, CHUNK)


def generateAudio():
    stream = audio.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        input_device_index=device_index,
        output=True,
        frames_per_buffer=CHUNK,
    )
    yield wav_header
    while True:
        yield stream.read(CHUNK)
