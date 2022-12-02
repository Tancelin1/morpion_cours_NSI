#! /usr/bon/env python
# -*- coding: utf-8 -*-

import pygame
import morpionprogram as progra

joueur_1 = input("Qui est le joueur 1 ?")
joueur_2 = input("Qui est le joueur 2 ?")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
surf = pygame.display.set_mode((900, 600))
surf.fill(WHITE)
case1 = []
case2 = []
case3 = []
case4 = []
case5 = []
case6 = []
case7 = []
case8 = []
case9 = []
position_x = 0
position_y = 0
run = True
tour = 0
surf = pygame.display.set_mode((900, 600))
surf.fill(WHITE)

def coordonne_x():
    """Permet de définir les coordonnées x d'une case.
    """
    coor_x = position_x // 300
    return coor_x

def coordonne_y():
    """Permet de définir les coordonnées x d'une case.
    """
    coor_y = position_y // 200
    return coor_y

def croix_case_00(color = BLUE):
    """Permet de définir la croix dans la case (0, 0)
    """
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 150, (coordonne_y() + 1) * 100), ((coordonne_x() + 1) * 150 + 150, (coordonne_y() + 1) * 100 + 100), 5)
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 150 , (coordonne_y() + 1) * 100), ((coordonne_x() + 1) * 150 - 150, (coordonne_y() + 1) * 100 - 100), 5)
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 150, (coordonne_y() + 1) * 100), ((coordonne_x() + 1) * 150 + 150, (coordonne_y() + 1) * 100 - 100), 5)
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 150, (coordonne_y() + 1) * 100), ((coordonne_x() + 1) * 150 - 150, (coordonne_y() + 1) * 100 + 100), 5)


def croix_case_10(color = BLUE):
    """Permet de définir la croix dans la case (1, 0)
    """
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 225, (coordonne_y() + 1) * 100), ((coordonne_x() + 1) * 225 + 150, (coordonne_y() + 1) * 100 + 100), 5)
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 225 , (coordonne_y() + 1) * 100), ((coordonne_x() + 1) * 225 - 150, (coordonne_y() + 1) * 100 - 100), 5)
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 225, (coordonne_y() + 1) * 100), ((coordonne_x() + 1) * 225 + 150, (coordonne_y() + 1) * 100 - 100), 5)
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 225, (coordonne_y() + 1) * 100), ((coordonne_x() + 1) * 225 - 150, (coordonne_y() + 1) * 100 + 100), 5)

def croix_case_20(color = BLUE):
    """Permet de définir la croix dans la case (2, 0)
    """
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 250, (coordonne_y() + 1) * 100), ((coordonne_x() + 1) * 250 + 150, (coordonne_y() + 1) * 100 + 100), 5)
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 250 , (coordonne_y() + 1) * 100), ((coordonne_x() + 1) * 250 - 150, (coordonne_y() + 1) * 100 - 100), 5)
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 250, (coordonne_y() + 1) * 100), ((coordonne_x() + 1) * 250 + 150, (coordonne_y() + 1) * 100 - 100), 5)
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 250, (coordonne_y() + 1) * 100), ((coordonne_x() + 1) * 250 - 150, (coordonne_y() + 1) * 100 + 100), 5)


def croix_case_01(color = BLUE):
    """Permet de définir la croix dans la case (0, 1)
    """
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 150, (coordonne_y() + 1) * 150), ((coordonne_x() + 1) * 150 + 150, (coordonne_y() + 1) * 150 + 100), 5)
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 150 , (coordonne_y() + 1) * 150), ((coordonne_x() + 1) * 150 - 150, (coordonne_y() + 1) * 150 - 100), 5)
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 150, (coordonne_y() + 1) * 150), ((coordonne_x() + 1) * 150 + 150, (coordonne_y() + 1) * 150 - 100), 5)
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 150, (coordonne_y() + 1) * 150), ((coordonne_x() + 1) * 150 - 150, (coordonne_y() + 1) * 150 + 100), 5)


def croix_case_11(color = BLUE):
    """Permet de définir la croix dans la case (1, 1)
    """
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 225, (coordonne_y() + 1) * 150), ((coordonne_x() + 1) * 225 + 150, (coordonne_y() + 1) * 150 + 100), 5)
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 225 , (coordonne_y() + 1) * 150), ((coordonne_x() + 1) * 225 - 150, (coordonne_y() + 1) * 150 - 100), 5)
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 225, (coordonne_y() + 1) * 150), ((coordonne_x() + 1) * 225 + 150, (coordonne_y() + 1) * 150 - 100), 5)
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 225, (coordonne_y() + 1) * 150), ((coordonne_x() + 1) * 225 - 150, (coordonne_y() + 1) * 150 + 100), 5)

def croix_case_21(color = BLUE):
    """Permet de définir la croix dans la case (2, 1)
    """
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 250, (coordonne_y() + 1) * 150), ((coordonne_x() + 1) * 250 + 150, (coordonne_y() + 1) * 150 + 100), 5)
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 250 , (coordonne_y() + 1) * 150), ((coordonne_x() + 1) * 250 - 150, (coordonne_y() + 1) * 150 - 100), 5)
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 250, (coordonne_y() + 1) * 150), ((coordonne_x() + 1) * 250 + 150, (coordonne_y() + 1) * 150 - 100), 5)
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 250, (coordonne_y() + 1) * 150), ((coordonne_x() + 1) * 250 - 150, (coordonne_y() + 1) * 150 + 100), 5)

def croix_case_02(color = BLUE):
    """Permet de définir la croix dans la case (0, 2)
    """
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 150, (coordonne_y() + 1) * 167), ((coordonne_x() + 1) * 150 + 150, (coordonne_y() + 1) * 167 + 100), 5)
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 150 , (coordonne_y() + 1) * 167), ((coordonne_x() + 1) * 150 - 150, (coordonne_y() + 1) * 167 - 100), 5)
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 150, (coordonne_y() + 1) * 167), ((coordonne_x() + 1) * 150 + 150, (coordonne_y() + 1) * 167 - 100), 5)
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 150, (coordonne_y() + 1) * 167), ((coordonne_x() + 1) * 150 - 150, (coordonne_y() + 1) * 167 + 100), 5)


def croix_case_12(color = BLUE):
    """Permet de définir la croix dans la case (1, 2)
    """
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 225, (coordonne_y() + 1) * 167), ((coordonne_x() + 1) * 225 + 150, (coordonne_y() + 1) * 167 + 100), 5)
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 225 , (coordonne_y() + 1) * 167), ((coordonne_x() + 1) * 225 - 150, (coordonne_y() + 1) * 167 - 100), 5)
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 225, (coordonne_y() + 1) * 167), ((coordonne_x() + 1) * 225 + 150, (coordonne_y() + 1) * 167 - 100), 5)
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 225, (coordonne_y() + 1) * 167), ((coordonne_x() + 1) * 225 - 150, (coordonne_y() + 1) * 167 + 100), 5)

def croix_case_22(color = BLUE):
    """Permet de définir la croix dans la case (2, 2)
    """
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 250, (coordonne_y() + 1) * 167), ((coordonne_x() + 1) * 250 + 150, (coordonne_y() + 1) * 167 + 100), 5)
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 250 , (coordonne_y() + 1) * 167), ((coordonne_x() + 1) * 250 - 150, (coordonne_y() + 1) * 167- 100), 5)
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 250, (coordonne_y() + 1) * 167), ((coordonne_x() + 1) * 250 + 150, (coordonne_y() + 1) * 167 - 100), 5)
    pygame.draw.line(surf, color, ((coordonne_x() + 1) * 250, (coordonne_y() + 1) * 167), ((coordonne_x() + 1) * 250 - 150, (coordonne_y() + 1) * 167 + 100), 5)

def rond_00(color = GREEN):
    """Permet de définir un rond dans la case (0, 0).
    """
    pygame.draw.circle(surf, color, ((coordonne_x() + 1) * 150, (coordonne_y() + 1) * 100), 95, 2)

def rond_10(color = GREEN):
    """Permet de définir un rond dans la case (1, 0).
    """
    pygame.draw.circle(surf, color, ((coordonne_x() + 1) * 225, (coordonne_y() + 1) * 100), 95, 2)

def rond_20(color = GREEN):
    """Permet de définir un rond dans la case (2, 0).
    """
    pygame.draw.circle(surf, color, ((coordonne_x() + 1) * 250, (coordonne_y() + 1) * 100), 95, 2)

def rond_01(color = GREEN):
    """Permet de définir un rond dans la case (0, 1).
    """
    pygame.draw.circle(surf, color, ((coordonne_x() + 1) * 150, (coordonne_y() + 1) * 150), 95, 2)

def rond_11(color = GREEN):
    """Permet de définir un rond dans la case (1, 1).
    """
    pygame.draw.circle(surf, color, ((coordonne_x() + 1) * 225, (coordonne_y() + 1) * 150), 95, 2)

def rond_21(color = GREEN):
    """Permet de définir un rond dans la case (2, 1).
    """
    pygame.draw.circle(surf, color, ((coordonne_x() + 1) * 250, (coordonne_y() + 1) * 150), 95, 2)

def rond_02(color = GREEN):
    """Permet de définir un rond dans la case (0, 2).
    """
    pygame.draw.circle(surf, color, ((coordonne_x() + 1) * 150, (coordonne_y() + 1) * 167), 95, 2)

def rond_12(color = GREEN):
    """Permet de définir un rond dans la case (1, 2).
    """
    pygame.draw.circle(surf, color, ((coordonne_x() + 1) * 225, (coordonne_y() + 1) * 167), 95, 2)

def rond_22(color = GREEN):
    """Permet de définir un rond dans la case (2, 2).
    """
    pygame.draw.circle(surf, color, ((coordonne_x() + 1) * 250, (coordonne_y() + 1) * 167), 95, 2)

while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1, 0, 0):
                position_x = pygame.mouse.get_pos()[0]
                position_y = pygame.mouse.get_pos()[1]
                if coordonne_x() == 0 and coordonne_y() == 0:
                    if len(case1) == 0:
                        tour = tour + 1
                        if tour % 2 == 1:
                            croix_case_00()
                            case1.append(1)
                        else:
                            rond_00()
                            case1.append(2)
                elif coordonne_x() == 1 and coordonne_y() == 0:
                    if len(case2) == 0:
                        tour = tour + 1
                        if tour % 2 == 1:
                            croix_case_10()
                            case2.append(1)
                        else:
                            rond_10()
                            case2.append(2)
                elif coordonne_x() == 2 and coordonne_y() == 0:
                    if len(case3) == 0:
                        tour = tour + 1
                        if tour % 2 == 1:
                            croix_case_20()
                            case3.append(1)
                        else:
                            rond_20()
                            case3.append(2)
                elif coordonne_x() == 0 and coordonne_y() == 1:
                    if len(case4) == 0:
                        tour = tour + 1
                        if tour % 2 == 1:
                            croix_case_01()
                            case4.append(1)
                        else:
                            rond_01()
                            case4.append(2)
                elif coordonne_x() == 1 and coordonne_y() == 1:
                    if len(case5) == 0:
                        tour = tour + 1
                        if tour % 2 == 1:
                            croix_case_11()
                            case5.append(1)
                        else:
                            rond_11()
                            case5.append(2)
                elif coordonne_x() == 2 and coordonne_y() == 1:
                    if len(case6) == 0:
                        tour = tour + 1
                        if tour % 2 == 1:
                            croix_case_21()
                            case6.append(1)
                        else:
                            rond_21()
                            case6.append(2)
                elif coordonne_x() == 0 and coordonne_y() == 2:
                    if len(case7) == 0:
                        tour = tour + 1
                        if tour % 2 == 1:
                            croix_case_02()
                            case7.append(1)
                        else:
                            rond_02()
                            case7.append(2)
                elif coordonne_x() == 1 and coordonne_y() == 2:
                    if len(case8) == 0:
                        tour = tour + 1
                        if tour % 2 == 1:
                            croix_case_12()
                            case8.append(1)
                        else:
                            rond_12()
                            case8.append(2)
                elif coordonne_x() == 2 and coordonne_y() == 2:
                    if len(case9) == 0:
                        tour = tour + 1
                        if tour % 2 == 1:
                            croix_case_22()
                            case9.append(1)
                        else:
                            rond_22()
                            case9.append(2)
                if not progra.vide(case1, case2, case3, case4, case5, case6, case7, case8, case9):
                    if progra.aligner_j1(case1, case2, case3):
                        print("Félicitation " + str(joueur_1))
                    elif progra.aligner_j1(case4, case5, case6):
                        print("Félicitation " + str(joueur_1))
                    elif progra.aligner_j1(case7, case8, case9):
                        print("Félicitation " + str(joueur_1))
                    elif progra.aligner_j2(case1, case2, case3):
                        print("Félicitation " + str(joueur_2))
                    elif progra.aligner_j2(case4, case5, case6):
                        print("Félicitation " + str(joueur_2))
                    elif progra.aligner_j2(case7, case8, case9):
                        print("Félicitation " + str(joueur_2))
                    elif progra.aligner_j1(case1, case4, case7):
                        print("Félicitation " + str(joueur_1))
                    elif progra.aligner_j1(case2, case5, case8):
                        print("Félicitation " + str(joueur_1))
                    elif progra.aligner_j1(case3, case6, case9):
                        print("Félicitation " + str(joueur_1))
                    elif progra.aligner_j2(case1, case4, case7):
                        print("Félicitation " + str(joueur_2))
                    elif progra.aligner_j2(case2, case5, case8):
                        print("Félicitation " + str(joueur_2))
                    elif progra.aligner_j2(case3, case6, case9):
                        print("Félicitation " + str(joueur_2))
                    elif progra.aligner_j1(case1, case5, case9):
                        print("Félicitation " + str(joueur_1))
                    elif progra.aligner_j1(case3, case5, case7):
                        print("Félicitation " + str(joueur_1))
                    elif progra.aligner_j2(case1, case5, case9):
                        print("Félicitation " + str(joueur_2))
                    elif progra.aligner_j2(case3, case5, case7):
                        print("Félicitation " + str(joueur_2))
                    else:
                        print("Match nul dommage :/")
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RETURN :
                pygame.quit()
                quit()
    pygame.draw.line(surf, BLACK, (0, 200), (900, 200), 2)
    pygame.draw.line(surf, BLACK, (0, 400), (900, 400), 2)
    pygame.draw.line(surf, BLACK, (300, 0), (300, 600), 2)
    pygame.draw.line(surf, BLACK, (600, 0), (600, 600), 2)
    pygame.display.flip()

pygame.quit()


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
