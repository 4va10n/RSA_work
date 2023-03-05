def get_data():
    data = []
    for i in range(21):
        with open(f"Frames/Frame{i}", 'r') as fin:
            raw_str = fin.read()
            n, e, c = int(raw_str[:256], 0x10), int(
                raw_str[256:512], 0x10), int(raw_str[512:], 0x10)
            data.append((n, e, c))
    #print(data)
    return data