POSITIONS = {
    "A" :  0,
    "A#":  1,
    "Bb":  1,
    "B" :  2,
    "C" :  3,
    "C#":  4,
    "Db":  4,
    "D" :  5,
    "D#":  6,
    "Eb":  6,
    "E" :  7,
    "F" :  8,
    "F#":  9,
    "Gb":  9,
    "G" : 10,
    "G#": 11,
    "Ab": 11
}

PITCHES = {
    0:  ["A"],
    1:  ["A#", "Bb"],
    2:  ["B"],
    3:  ["C"],
    4:  ["C#", "Db"],
    5:  ["D"],
    6:  ["D#", "Eb"],
    7:  ["E"],
    8:  ["F"],
    9:  ["F#", "Gb"],
    10: ["G"],
    11: ["G#", "Ab"]
}


class Note:
    """Creates a note object and defines functions for it
    
    Attributes:
        position(int): The position on a scale of the note
        perspective(str,optional): Flat or sharp, defaults to None
    
    """
    
    def __init__(self, position, perspective=None):
        self.position = POSITIONS[position] if isinstance(position, str) else position
        if isinstance(position, str) and len(position) == 2 and not perspective:
            self.perspective = position[1]
        else:
            self.perspective = perspective
    
    def __invert__(self):
        inote = Note(self.position, self.perspective)
        if inote.perspective == "b":
            inote.perspective = "#"
        elif inote.perspective == "#":
            inote.perspective = "b"
        return inote

    def __add__(self, move):
        pos = (self.position + move) % 12
        anote = Note(pos, self.perspective)
        return anote

    def __sub__(self, move):
        pos = (self.position - move) % 12
        snote = Note(pos, self.perspective)
        return snote
    
    def __rshift__(self, other):
        dist = (self.position - other.position) % 12
        return dist
    
    def __lshift__(self, other):
        dist1 = (other.position - self.position) % 12
        return dist1
    
    def __repr__(self):
        return f"Note({self.position}, {self.perspective!r})"
        
    def __str__(self):
        pos = PITCHES[self.position]
        if len(pos) == 1:
            return f"{pos[0]}"
        elif self.perspective == "b":
            return f"{pos[1]}"
        elif self.perspective == "#":
            return f"{pos[0]}"
        else:
            return f"{pos[0]}/{pos[1]}"
    
    
    
                
