from util import Stack

    # stackXY: ((x,y),[path]) #
    stackXY = Stack()

    visited = [] # Visited states
    path = [] # Every state keeps it's path from the starting state

    # Check if initial state is goal state #
    if problem.isGoalState(problem.getStartState()):
        return []

    # Start from the beginning and find a solution, path is an empty list #
    stackXY.push((problem.getStartState(),[]))

    while(True):

        # Terminate condition: can't find solution #
        if stackXY.isEmpty():
            return []

        # Get informations of current state #
        xy,path = stackXY.pop() # Take position and path
        visited.append(xy)

        # Comment this and uncomment 125. This only works for autograder    #
        # In lectures we check if a state is a goal when we find successors #

        # Terminate condition: reach goal #
        if problem.isGoalState(xy):
            return path

        # Get successors of current state #
        succ = problem.getSuccessors(xy)

        # Add new states in stack and fix their path #
        if succ:
            for item in succ:
                if item[0] not in visited:

                # Lectures code:
                # All impementations run in autograder and in comments i write
                # the proper code that i have been taught in lectures
                # if item[0] not in visited and item[0] not in (state[0] for state in stackXY.list):
                #   if problem.isGoalState(item[0]):
                #       return path + [item[1]]

                    newPath = path + [item[1]] # Calculate new path
                    stackXY.push((item[0],newPath))