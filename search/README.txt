Heuristic for Question 6:
In question 6 , I first calculate the distance of the nearest corner from the current position and take the manhattan distance between the current position and the nearest corner.Then I subsequently calculate the manhattan distance to the 2nd nearest corner.Then from the 2nd corner I calculate the distance to the nearest corner from the 2nd consumed corner.In this way I calculate the min manhattan from the present position covering all the subsequent positions .This is the minimum distance that the pacman would take in order to reach the goal state.Here the goal state is to reach at each of the corners position.




Heuristic for Question 7 :
In question 7 , I first used the manhattan distance of the farthest node.But that herustic was not optimal and was expanding more nodes(got a score of 3/4 when I used manhattan distance).Then I used the maze distance which takes into account the walls as well while calulating the distance.The heuristic that I get from maze distance was more optimal as it was expanding lesser nodes.The heuristic that I get from using maze distance would be consistent because in order to reach from present state (which has all the food) to the goal state (which has no food) we will have to reach the food that is the farthest from the present distance.So the cost would be atleast equal to the maze distance of the farthest food from the current position.After using the manhattan distance I got a score of 5/4 and hence the solution was more optimal.




Estimated Time I spent on homework : 17 - 18 hours