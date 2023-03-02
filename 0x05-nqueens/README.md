# N Queens
## Description
The N queens puzzle is the challenge of placing N non-attacking queens on an NxN chessboard. The approach for solving this challenge is presented below.
* Usage: ``nqueens N``
* If the user called the program with the wrong number of arguments, print ``Usage: nqueens N``, followed by a new line, and exit with the status ``1``
* where ``N`` must be an integer ``greater or equal to 4``
    * If ``N`` is not an integer, print ``N must be a number``, followed by a new line and exit with the status ``1``
    * If ``N`` is smaller than ``4``, print ``N must be at least 4``, followed by a new line, and exit with the status ``1``
* The program should print every possible solution to the problem:
    * One solution per line
    * Format: see example
    * You don’t have to print the solutions in a specific order
* You are only allowed to import the sys module
## Approach
The N queens falls into a category of problems termed as ``constraint-satisfaction problems``. These are types of problems with many candidate solutions, the vast majority of which don't satsify the given constraints. ``BACKTRACKING`` is a problem solving techinque the tackles this class of problems without trying all the possibilities. It incrementally builds candidates to solutions, and abandons a candidate, i.e, backtracks as soon as it determines that the candidate cannot possibly be completed to a valid solution.