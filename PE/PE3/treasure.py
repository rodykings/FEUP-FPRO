
def treasure(clues):
    current_clue = (0,0)
    past_clues = []
    
    while current_clue in clues and current_clue not in past_clues:
        past_clues.append(current_clue)
        current_clue = clues[current_clue]
    
    return current_clue
