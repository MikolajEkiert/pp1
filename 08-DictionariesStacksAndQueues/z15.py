icao={"A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo",
    "F": "Foxtrot", "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliet",
    "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November", "O": "Oscar",
    "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango",
    "U": "Uniform",
    "V": "Victor", "W": "Whiskey", "X": "X-ray", "Y": "Yankee", "Z": "Zulu",
    "a": "alpha", "b": "bravo", "c": "charlie",
    "d": "delta", "e": "echo", "f": "foxtrot", 
    "g": "golf", "h": "hotel", "i": "india", "j": "juliet", "k": "kilo", 
    "l": "lima", "m": "mike", "n": "november", "o": "oscar", "p": "papa", 
    "q": "quebec", "r": "romeo", "s": "sierra", "t": "tango", "u": "uniform", 
    "v": "victor", "w": "whiskey", "x": "x-ray", "y": "yankee", "z": "zulu"}
with open('ICAO.txt', 'w') as f:
    for k,v in icao.items():
        f.write(f'{k} {v} \n')