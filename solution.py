def solution(n):
    # Initialize a 2D list x with zeros to act as a memo
    x = [[0 for i in range (n+1)] for j in range(n+1)]
    
    # Set the base case x[0][0] to 1
    x[0][0] = 1

    for stairHeight in range(1, n+1):
        for bricksLeft in range(0, n+1):
            #the height of the current stair has to be one less than the previous one
            x[stairHeight][bricksLeft] = x[stairHeight-1][bricksLeft]
            
            # If there are enough bricks left to make another step, add to the memo
            if bricksLeft >= stairHeight:
                x[stairHeight][bricksLeft] += x[stairHeight-1][bricksLeft-stairHeight]
                
    # Return the number of ways to build stairs with n bricks, minus the invalid solution
    return x[n][n] - 1

                
print(solution(3))  # expected output: 1
print(solution(200))  # expected output: 487067745
