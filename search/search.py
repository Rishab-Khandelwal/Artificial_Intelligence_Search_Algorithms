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
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())

    if problem.isGoalState(problem.getStartState()):
        #print "Goal State found"
        return []
    else:
        #print "Not found need to search"
        visited = set()
        s = util.Stack()
        direction = []
        s.push((problem.getStartState(),[]))
        #print "s after pushing is ", s
        while not s.isEmpty():
            nextWholeNode = s.pop()
            #print "After Pop node is ", nextWholeNode
            nextNode = nextWholeNode[0]
            #print "nextNode is ", nextNode[0]
            visited.add(nextNode)
            direction = nextWholeNode[1]
            if problem.isGoalState(nextNode):
                break
            else:
                neighbourNodes = problem.getSuccessors(nextNode)
                for node in neighbourNodes:
                    nodeDirection = node[1]
                    childList = direction[:]
                    childList.append(nodeDirection)
                    #direction.append(nodeDirection)
                    if node[0] not in visited:
                        s.push((node[0],childList))


    #print "Direction is" ,direction
    return direction                


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())

    if problem.isGoalState(problem.getStartState()):
        #print "Goal state found"
        return []
    else:
        #print "Not found , we need to search"
        visited = set()
        q = util.Queue()
        q.push((problem.getStartState(),[]))
        while not q.isEmpty():
            nextWholeNode = q.pop()
            nextNode = nextWholeNode[0]
            visited.add(nextNode)
            direction = nextWholeNode[1]

            if problem.isGoalState(nextNode):
                break
            else:
                neighbourNodes = problem.getSuccessors(nextNode)
                for node in neighbourNodes:
                    if node[0] not in visited:
                        nodeDirection = node[1]
                        childList = direction[:]
                        childList.append(nodeDirection)
                        visited.add(node[0])
                        q.push((node[0],childList))


    #print "Direction is " , direction

    return direction

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    if problem.isGoalState(problem.getStartState()):
        return []
    else:
        visited = set()
        pq = util.PriorityQueue()
        pq.push((problem.getStartState(),[],0),0)
        direction = []

        while not pq.isEmpty():
            nextWholeNode = pq.pop()
            nextNode = nextWholeNode[0]
            cost = nextWholeNode[2]
            direction = nextWholeNode[1]
            if nextNode in visited:
                continue
            else:
                visited.add(nextNode)

            if problem.isGoalState(nextNode):
                break
            else:
                neighbourNodes = problem.getSuccessors(nextNode)
                for node in neighbourNodes:
                    nodeDirection= node[1]
                    childList= direction[:]
                    childList.append(nodeDirection)
                    Totalcost = cost + node[2]
                    pq.push((node[0],childList,Totalcost),Totalcost)

    print direction
    return direction

    '''else:
        visited = set()
        pq = util.PriorityQueue()
        pq.push((problem.getStartState() ,[],0),0)

        while not pq.isEmpty():
            nextWholeNode = pq.pop()
            nextNode = nextWholeNode[0]
            visited.add(nextNode)
            direction = nextWholeNode[1]
            queueNodes = []
            cost = nextWholeNode[2]
            queueSet = set()
            if problem.isGoalState(nextNode):
                break
            else:
                neighbourNodes =problem.getSuccessors(nextNode)
                arr = pq.heap
                #print "Heap is" ,arr
                for a in arr:
                    queueSet.add(a[0]) 
                for node in neighbourNodes:
                    if node[0] not in visited and node[0] not in queueSet:
                        nodeDirection = node[1]
                        childList = direction[:]
                        Totalcost =  cost + node[2]
                        childList.append(nodeDirection)
                        visited.add(node[0])
                        pq.update((node[0],childList,Totalcost),Totalcost)
                        #queueSet.add(node[0])
                    
        
        return direction'''
  

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    if problem.isGoalState(problem.getStartState()):
        return []
    else:
        visited = set()
        pq = util.PriorityQueue()
        pq.push((problem.getStartState(),[],0),0)

        while not pq.isEmpty():
            #print "I reaced here"
            nextWholeNode = pq.pop()
            nextNode = nextWholeNode[0]

            direction = nextWholeNode[1]
            
            if nextNode in visited:
                continue
            else:
                visited.add(nextNode)
            cost = nextWholeNode[2] 
            #print "I reaced here2"
            if problem.isGoalState(nextNode):
                break
            else:
                #print "I reaced here4"
                #print "Next node is" , nextNode
                neighbourNodes = problem.getSuccessors(nextNode)
                #print "I reaced here3"
                for node in neighbourNodes:
                    nodeDirection = node[1]
                    childList = direction[:]
                    childList.append(nodeDirection)
                    CombinedCost = node[2] + cost
                    TotalCost = CombinedCost + heuristic(node[0], problem) 
                    pq.push((node[0] , childList,CombinedCost),TotalCost)
    return direction


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
