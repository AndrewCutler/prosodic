import cmudict

def get_syllable_count(phones):
    count = 0
    for stress in ["0", "1", "2"]:
        for phone in phones:
            if stress in phone:
                count += 1

    return count

def map_stressed_syllables(phones):
    stresses = ''
    for phone in phones:
        if '0' in phone:
            stresses += '0'
        if '1' in phone:
            stresses += '1'
        if '2' in phone:
            stresses += '2'

    return stresses

with open('./all_star.txt', 'r') as file:
    line_meters = []
    for line in file:
        line_meter = ''
        words = [word.lower() for word in line.rstrip().split(' ')]
        for word in words:
            syllable_map = cmudict.dict()[word]
            if (len(syllable_map) > 0):
                line_meter += map_stressed_syllables(syllable_map[0])
            else:
                line_meter += '?' + word + '?'
        line_meters.append(line_meter)

    print(line_meters)