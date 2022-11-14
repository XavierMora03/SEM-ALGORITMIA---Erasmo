import pygame as pg
import numpy as np


class MapaNode:
    def __init__(self, position, cost, parent=None):
        self.position = position
        self.cost = cost
        self.parent = parent

    def __eq__(self, other):
        return self.position[0] == other.position[0] and self.position[1] == other.position[1]


class Dijkstra(object):
    def run(self, mapa, start, end):
        mapa = mapa.astype(np.float64)

        unique, counts = np.unique(mapa, return_counts=True)
        nodosEnUno = counts[1]
        path = []
        vectorOfVisited = []
        vectorOFLabeled = []
        mapaRows, mapaCols = np.shape(mapa)
        visited = np.zeros(mapa.shape)
        costs = np.zeros(mapa.shape)
        vectorOFLabeled.append(MapaNode(start[::-1], 0))
        endNode = MapaNode(end[::-1], 0)

        movements = [[-1, -1, 1.4],
                     [0, -1, 1],
                     [1, -1, 1.4],
                     [-1, 0, 1],
                     [1, 0, 1],
                     [-1, 1, 1.4],
                     [0, 1, 1],
                     [1, 1, 1.4]]

        while(len(vectorOfVisited) != nodosEnUno):
            currentNode = vectorOFLabeled.pop(0)

            movements = [[-1, -1, 1.4],
                         [0, -1, 1],
                         [1, -1, 1.4],
                         [-1, 0, 1],
                         [1, 0, 1],
                         [-1, 1, 1.4],
                         [0, 1, 1],
                         [1, 1, 1.4]]
            
            for movement in movements:
                # create adjacent position
                newPosition = [currentNode.position[0]+movement[0],
                               currentNode.position[1]+movement[1]]
                adjacentNode = MapaNode(
                    newPosition, currentNode.cost+movement[2], currentNode)

                if newPosition[0] < 0 or newPosition[1] < 0 or newPosition[1] > mapaCols or newPosition[0] >= mapaRows:
                    continue
                elif mapa[newPosition[0]][newPosition[1]] == 0:
                    continue
                elif visited[newPosition[0]][newPosition[1]] == 1:
                    continue
                else:
                    # searh on labeled list
                    vectorOFLabeled.append(adjacentNode)
                    encontrado = False
                    for labeled in vectorOFLabeled:
                        if labeled == adjacentNode:
                            encontrado = True
                            if(labeled.cost > adjacentNode.cost):
                                labeled.cost = adjacentNode.cost
                                costs[newPosition[0]][newPosition[1]
                                                      ] = adjacentNode.cost

                                labeled.parent = currentNode
                    if not encontrado:
                        # add node to labeled
                        vectorOFLabeled.append(adjacentNode)
                        costs[newPosition[0]][newPosition[1]
                                              ] = adjacentNode.cost

            vectorOfVisited.append(currentNode)
            if(currentNode == endNode):
                break
            # mark the node as visited
            visited[currentNode.position[0]][currentNode.position[1]] = 1
            vectorOFLabeled = sorted(vectorOFLabeled, key=lambda x: x.cost)

        # reverse in order to know the way
        for visitedNode in vectorOfVisited:
            if visitedNode == endNode:
                endNode = visitedNode
                break

        while endNode is not None:
            path.append(endNode.position)
            endNode = endNode.parent

        return path, visited, costs


pg.init()

# load the map
mapaAlg = np.load('./mapaProfundidad.npy')
width, heigth = mapaAlg.shape

BLACK = pg.Color('black')
WHITE = pg.Color('white')
GREEN = pg.Color('green')
RED = pg.Color('red')
BLUE = pg.Color('blue')

# ligth shade of the button
color_ligth = (170, 170, 170)
color_dark = (100, 100, 100)
smallfont = pg.font.SysFont('arial', 30)
text = smallfont.render("search", True, RED)

# pixel sizes of button
title_size = 10

start_point = [10, 3]
goal_point = [43, 43]

topPadding = 50
search = Dijkstra()

# defining screen dimentions
screen = pg.display.set_mode((width*title_size, heigth*title_size+topPadding))

# size of the acutal interface
background = pg.Surface((width*title_size, heigth*title_size))
buttons = pg.Surface((width*title_size, 50))
# displaying the map

for y in range(0, heigth):
    for x in range(0, width):
        rect = (x*title_size, y * title_size, title_size, title_size)
        if(mapaAlg[y, x] == 0):
            color = BLACK
        else:
            color = WHITE

        if(x == start_point[0] and y == start_point[1]):
            color = GREEN
        if(x == goal_point[0] and y == goal_point[1]):
            color = RED
        pg.draw.rect(background, color, rect)


# game execution

game_exit = False

while not game_exit:
    mouse = pg.mouse.get_pos()
    for event in pg.event.get():
        if(event.type == pg.QUIT):
            game_exit = True
        if event.type == pg.MOUSEBUTTONDOWN:
            if 10 <= mouse[0] <= 150 and 1 <= mouse[1] <= 40:
                way, mapvisited, costos = search.run(
                    mapaAlg, start_point, goal_point)
                for point in way:
                    rect = (point[1]*title_size, point[0] *
                            title_size, title_size, title_size)
                    pg.draw.rect(background, BLUE, rect)

    # if mouse if hovering our button
    if 0 <= mouse[0] <= 140 and 10 <= mouse[1] <= 40:
        pg.draw.rect(buttons, color_ligth, [10, 10, 140, 30])
    else:
        pg.draw.rect(buttons, color_dark, [10, 10, 140, 30])

    screen.fill((0, 0, 0))
    screen.blit(buttons, (0, 0))
    screen.blit(background, (0, 50))
    screen.blit(text, (10, 10))
    pg.display.flip()

pg.display.quit()
