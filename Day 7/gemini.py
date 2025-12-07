def solve_manifold_timelines(map_str):
    lines = [line for line in map_str.split('\n') if line.strip()]
    
    # Parse map into a coordinate dictionary for easy lookup
    # key: (row, col), value: char
    grid = {}
    start_pos = None
    
    height = len(lines)
    width = 0
    
    for r, line in enumerate(lines):
        width = max(width, len(line))
        for c, char in enumerate(line):
            grid[(r, c)] = char
            if char == 'S':
                start_pos = (r, c)
                
    if not start_pos:
        return "Error: No starting point 'S' found."

    # DP State: dictionary mapping (row, col) -> count of timelines
    # We use a dictionary (or Counter) because the grid might be sparse
    active_timelines = {start_pos: 1}
    
    total_completed_timelines = 0
    
    # Process row by row
    for r in range(height - 1):
        next_timelines = {}
        
        for (curr_r, curr_c), count in active_timelines.items():
            if curr_r != r: continue # Should not happen if we process row by row
            
            # Look strictly at the cell BELOW the current position
            # to decide behavior, as per the "Manifold" mechanics.
            
            target_r = r + 1
            target_c = curr_c
            target_cell = grid.get((target_r, target_c), '.') # Default to empty if out of bounds?
            
            if target_cell == '^':
                # SPLITTER: Timeline splits Left and Right
                # Left path
                left_pos = (target_r, target_c - 1)
                next_timelines[left_pos] = next_timelines.get(left_pos, 0) + count
                
                # Right path
                right_pos = (target_r, target_c + 1)
                next_timelines[right_pos] = next_timelines.get(right_pos, 0) + count
                
            else:
                # EMPTY SPACE (or others): Continue straight
                # Note: We assume the particle lands ON the target cell
                straight_pos = (target_r, target_c)
                next_timelines[straight_pos] = next_timelines.get(straight_pos, 0) + count

        active_timelines = next_timelines
        
        # Optimization: If the map is huge, we can delete the old row from memory, 
        # but re-assigning `active_timelines` essentially handles this.

    # Sum all counts in the final active row
    total_timelines = sum(active_timelines.values())
    return total_timelines

# ---------------------------------------------------------
# PASTE YOUR FULL MAP BETWEEN THE TRIPLE QUOTES BELOW
# ---------------------------------------------------------
input_map = open('Day 7/test.txt').read().strip()

# Calculate
result = solve_manifold_timelines(input_map)
print(f"Total active timelines: {result}")