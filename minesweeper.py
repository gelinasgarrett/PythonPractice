

# Mine sweeper func accepts bomb position indexes, the number of rows, and number of columns
def mine_sweeper(bombs, num_rows, num_cols):
  #An empty array of zeros is created from the num of rows and columns
  field = [[0 for i in range(num_cols)] for j in range(num_rows)]

  #Bomb positions and +1s are added, bomb positions are updated after every loop of the entire
  # block... This allows for proper updating of nearby bomb neighbors
  for bomb_loc in bombs:
    #Iterated bomb locations are assigned to as -1 each pass
    (bomb_row, bomb_col) = bomb_loc
    field[bomb_row][bomb_col] = -1

    #row_range and col_range counts the elements near a bomb... The range + col loop will
    # find all positions immediately around a bomb
    
    #row distance is checked + updated
    for i in range(bomb_row -1, bomb_row +2):
      current_i = i
      #column distance is checked + updated
      for j in range(bomb_col -1, bomb_col + 2):
        current_j = j
        # If all 3 conditions are met, it means that the index is in range of a bomb and updates its mark
        if (0 <= i < num_rows and 0 <= j < num_cols and field[i][j] != -1):
          #The current position is updated +1... (If this loop runs again and adds a bomb position near a current '1',
          #   the field will again be updated until all nearby bombs are accounted for. 3 bombs in immediate vicinity will
          #     create elements with '3' if necessary
          field[i][j] += 1
  return field

print(mine_sweeper([[0,0],[1,2],[2,3]], 5,5))