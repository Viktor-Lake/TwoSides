from core.note_types.note import note

class hold_note(note):
    duration = None
    
    def __init__(self):
        self.note_type = "hold"
        self.duration = 0
    
    def __str__(self):
        return f"hold note at {self.coord} for {self.duration}ms"