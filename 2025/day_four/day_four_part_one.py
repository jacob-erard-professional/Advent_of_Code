def surround_with_x(text, border_char='x'):
    if isinstance(text, str):
        lines = text.split('\n')
    else:
        lines = text
    
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    
    if not lines:
        return ""
    
    max_length = max(len(line) for line in lines)
    
    top_border = border_char * (max_length + 2)
    
    bordered_lines = [top_border]
    for line in lines:
        padded_line = line.ljust(max_length)
        bordered_lines.append(border_char + padded_line + border_char)
    
    bottom_border = border_char * (max_length + 2)
    bordered_lines.append(bottom_border)
    
    return '\n'.join(bordered_lines)

def parse_to_2d_array(text):
    """
    Parse text into a 2D array where each character is an element.
    
    Args:
        text: The input text string
    
    Returns:
        A 2D list where grid[row][col] is a character
    """
    lines = text.split('\n')
    
    # Remove empty lines at start and end
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    
    # Convert each line to a list of characters
    grid = [list(line) for line in lines]
    
    return grid

with open('day_four/day_four_data.txt', 'r') as f:
    data = f.read()
data = surround_with_x(data)
data = parse_to_2d_array(data)

def get_roll_count(data, row, col):
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            new_row = row + dr
            new_col = col + dc
            if data[new_row][new_col] == "@":
                count +=1
    
    return count


total=0
for i in range (1, len(data)-1):
    for j in range(1, len(data[0])-1):
        if data[i][j] == "@" and get_roll_count(data, i, j) < 4:
            total += 1
print(total)
