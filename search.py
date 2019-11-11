# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """

    # list used to store visited nodes/states
    visited = []

    # list to be returned of path to goal
    path = []

    # append to stack
    fringe = util.Stack()

    # insert starting node into fringe stack along with path
    fringe.push((problem.getStartState(), path))

    # check if starting state is the goal state
    if problem.isGoalState(problem.getStartState()):
        fringe.pop()

    # core loop, continues as long as there are unexplored states in the search fringe
    while not fringe.isEmpty():

        # remove node from stack to explore neighbours, update path
        position, path = fringe.pop()

        # mark position as visited
        visited.append(position)

        # check if current state is goal state
        if problem.isGoalState(position):
            return path

        # iterate through possible successors of current state
        for neighbour in problem.getSuccessors(position):

            # checks if neighboring states are explored
            if neighbour[0] not in visited:

                # push in the successor returned from method
                fringe.push((neighbour[0], path + [neighbour[1]]))

    # if while loop ends without return value then no path exists
    return []


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    # list used to store visited nodes/states
    visited = []

    # list to be returned of path to goal
    path = []

    # append to queue
    fringe = util.Queue()

    # insert starting node into fringe queue along with path
    fringe.push((problem.getStartState(), path))

    # check if starting state is the goal state
    if problem.isGoalState(problem.getStartState()):
        fringe.pop()

    # core loop, continues as long as there are unexplored states in the search fringe
    while not fringe.isEmpty():

        # remove node from queue to explore neighbours in layered-like search
        position, path = fringe.pop()

        # mark position as visited
        if position not in visited:
            visited.append(position)

            # check if current state is goal state (How do I tie in the fourCorners heuristic goal?)
            if problem.isGoalState(position):
                # print("This print statement should only appear at the end")
                return path

            # iterate through possible successors of current state
            for neighbour in problem.getSuccessors(position):

                # checks if neighboring states are explored
                if neighbour[0] not in visited:
                    if neighbour[0] not in (item[0] for item in fringe.list):

                    # push in the successor returned from method
                        fringe.push(((neighbour[0]), path + [neighbour[1]]))

    # if while loop ends without return value then no path exists
    return []




def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    # list used to store visited nodes/states
    visited = []

    # list to be returned of path to goal
    path = []

    # append to priority queue
    fringe = util.PriorityQueue()

    # insert starting node into fringe PQ along with path
    fringe.push((problem.getStartState(), path), problem.getCostOfActions(path))

    # check if starting state is the goal state
    if problem.isGoalState(problem.getStartState()):
        fringe.pop()

    # core loop, continues as long as there are unexplored states in the search fringe
    while not fringe.isEmpty():

        # remove node from PQ to explore neighbours, update path
        position, path = fringe.pop()

        # only run successor check if current node is unexplored
        if position not in visited:
            # mark position as visited
            visited.append(position)

            # check if current state is goal state
            if problem.isGoalState(position):
                return path

            # iterate through possible successors of current state
            for neighbour in problem.getSuccessors(position):

                # checks if neighboring states are explored
                if neighbour[0] not in visited:

                    # push in the successor returned from method, along with new actions path cost
                    fringe.push((neighbour[0], path + [neighbour[1]]), problem.getCostOfActions(path + [neighbour[1]]))

    # if while loop ends without return value then no path exists
    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    '''
    from searchAgents import manhattanHeuristic as md
    estimate = md(state, problem)
    return estimate
    '''
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):

    """Search the node that has the lowest combined cost and heuristic first."""

    # getCostofActions gives me the g cost, the total cost of ALL the steps taken to get to a state

    # list used to store visited nodes/states
    visited = []

    # list to be returned of path to goal
    path = []

    # append to priority queue, requires position, path, and heuristic total cost
    fringe = util.PriorityQueue()

    # starting state
    start = problem.getStartState()

    # insert starting node into fringe PQ along with path and heuristic cost
    fringe.push((start, path), problem.getCostOfActions(path) + heuristic(start, problem))

    # check if starting state is the goal state
    if problem.isGoalState(start):
        fringe.pop()

    # core loop, continues as long as there are unexplored states in the search fringe
    while not fringe.isEmpty():

        # remove node from PQ to explore neighbours, update path
        position, path = fringe.pop()

        # mark position as visited, and only run successor check if node is unexplored
        if position not in visited:
            visited.append(position)

            # check if current state is goal state
            if problem.isGoalState(position):
                return path

            # iterate through possible successors of current state
            for neighbour in problem.getSuccessors(position):

                # checks if neighboring states are explored
                if neighbour[0] not in visited:

                    # add the heuristic and the total cost together
                    total = problem.getCostOfActions(path + [neighbour[1]]) + heuristic(neighbour[0], problem)

                    # push in the successor returned from method
                    fringe.push((neighbour[0], path + [neighbour[1]]), total)

    # if while loop ends without return value then no path exists
    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
