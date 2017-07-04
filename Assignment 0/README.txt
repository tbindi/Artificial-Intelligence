Let’s fix the implementation and mathematical abstraction to make it much
faster, and then use it to solve N-queens.

1. Spend some time familiarizing yourself with the code. Write down the precise
abstraction that the program is using. In other words, what is the set of valid
states, the successor function, the cost function, the goal state definition,
 and the initial state?

--> Code Abstraction:
    1. Set of Valid States: Everything is considered a valid state in the
    successors function.
    2. Successors Function: Successor function is a list comprehension that
    takes a row and a column using 2 for loops and then adds a piece to a
    given board.
    3. Cost Function: In this puzzle the cost of adding a piece or moving
    from one state space to the next is always constant.
    4. Goal Function: The goal state function is where there are N pieces and
     each board or column has only one piece that is not colliding with each
     other.
    5. Initial State: The initial state function is where the board is empty
    and it just has 0.

2. Is the algorithm using BFS or DFS? Switch to the opposite, and explain
exactly how to modify the code to do this. What happens now for N=4 and N=8?

--> The algorithm is using DFS (Stack Implementation of the variable fringe).
 To convert it to BFS we have to just change the statement: fringe.pop() to
 fringe.pop(0) which makes it to be the queue. This will make it run faster
 for N=4 because it is getting a new state for the successors function to
 move forward to. For N=8 it still takes forever to run.

3. The successor function in the code is defined in a very simplistic way,
including generating states that have N+1 rooks on them, and allowing “moves”
that involve not adding a rook at all. Create a new successors() function
called successors2() that fixes these two problems. Now does the choice of
BFS or DFS matter? Why or why not?

--> The new successor function has 2 condition check before the piece gets
     added to the board. They are:
    1. If the board already has a piece where it wants to place. (board[r][c]
     != 1 , this is nothing but "moves" that involve not adding a rook at all.)
    2. If the board has less than N pieces then add a piece. ( This makes
    sure that the piece count does not go beyond N ).

    It matters because the fringe in the case of DFS takes less time to
    arrive at the solution than BFS. DFS takes the top element in the stack
    which is solved most recently to compute next set of states. Whereas BFS
    takes the one solved earlier to compute and takes to compute the next set
    of states. In other words DFS will help in eliminating false states
    sooner than in BFS.

4. Even with the modifications so far, N=8 is still very slow. Recall from
Section 2.8 that we could define our state space and successor functions in a
smarter way, to reduce the search space to be more tractable. Describe your
new abstraction, and then modify the code to implement it with a new
successors function called successors3(). Feel free to make other code
improvements as well. What is the largest value of N your new version can run
on within about 1 minute?

--> Reducing the State Space and Defining Successor Function:
    1. State Space: In Successors 3 function, I ignore the particular Row or
    Column if there is already a piece added. I also check if there is
    already a piece in a particular r,c. I also check if the number of pieces
    are less than N once the piece is added.
    2. Once I add the piece after these conditions, I quit adding (break
    at line 105). This means that I have found a promising state where I can
    continue. I am assuming that I can add one piece at a time for each state
    space to arrive at the solution.
    3. The new version of successors function can run for a value of N=240
    within 1 minute.


Tip: In Linux, you can use the timeout command to kill a program after a
specified time period: timeout 1m python nrooks.py

5. Now, modify your code so that it solves and displays solutions for both the
N-rooks and N-queens problem, using the enhancements above. What is the
largest value of N that your new version can solve within 1 minute?

--> The new Successors function that can run for queens problem is
successors_queen and the goal should be changed to is_goal_queen because the
goal state and successors function for Queens problem has been modified a bit.

The new version of successor function can solve N-Queens for value N=13
within a minute.
