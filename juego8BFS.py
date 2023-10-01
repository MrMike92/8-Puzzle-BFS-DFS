"""MIT License
Copyright (c) 2023 MrMike92
Se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia de este software y de los archivos de documentación asociados (el "Software"), para tratar el Software sin restricciones, incluyendo, sin limitación, los derechos de uso, copia, modificación, fusión, publicación, distribución, sublicencia y/o venta de copias del Software, y para permitir a las personas a las que se les proporcione el Software a hacerlo, sujeto a las siguientes condiciones:
El aviso de copyright anterior y este aviso de permiso se incluirán en todas las copias o porciones sustanciales del Software.
EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA, INCLUYENDO PERO NO LIMITADO A LAS GARANTÍAS DE COMERCIABILIDAD, ADECUACIÓN PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO LOS AUTORES O TITULARES DE LOS DERECHOS DE AUTOR SERÁN RESPONSABLES POR CUALQUIER RECLAMO, DAÑO U OTRA RESPONSABILIDAD, YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O DE OTRO MODO, DERIVADA DE, FUERA DE O EN CONEXIÓN CON EL SOFTWARE O EL USO U OTROS TRATOS EN EL SOFTWARE."""

import random
from collections import deque

class Puzzle:
    def __init__(self, goal_state):
        self.goal_state = goal_state
        self.initial_state = self.generate_random_initial_state()
        
    def generate_random_initial_state(self):
        # Generar una lista con los números del 0 al 8 de manera aleatoria
        numbers = list(range(9))
        random.shuffle(numbers)

        # Convertir la lista en una matriz 3x3
        initial_state = [numbers[i:i+3] for i in range(0, 9, 3)]
        return initial_state

    def print_board(self, board):
        for row in board:
            print(" ".join(map(str, row)))
        print()

    def swap_position(self, board, number):
        for i in range(3):
            for j in range(3):
                if board[i][j] == number:
                    for k in range(3):
                        for l in range(3):
                            if board[k][l] == 0:
                                board[i][j], board[k][l] = board[k][l], board[i][j]
                                return

    def get_valid_moves_in_order(self, board):
        valid_moves = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    if j > 0:
                        valid_moves.append((i, j - 1, "Izquierda "))
                    if i > 0:
                        valid_moves.append((i - 1, j, "Arriba "))
                    if j < 2:
                        valid_moves.append((i, j + 1, "Derecha "))
                    if i < 2:
                        valid_moves.append((i + 1, j, "Abajo "))

        valid_moves.sort(key=lambda x: ("Izquierda ", "Arriba ", "Derecha ", "Abajo ").index(x[2]))

        return valid_moves

    def solve(self):
        queue = deque([(self.initial_state, 1, 0, "")])
        visited = set()
        move_number = 2
        last_board = None  # Variable para rastrear el último tablero visitado

        while queue:
            state, parent, depth, move = queue.popleft()
            visited.add(tuple(map(tuple, state)))

            if state == self.goal_state:
                return (depth, parent, move)

            valid_moves = self.get_valid_moves_in_order(state)

            for i, j, move_str in valid_moves:
                new_state = [row[:] for row in state]
                self.swap_position(new_state, state[i][j])
                new_move = move + move_str
                new_node = (new_state, move_number, depth + 1, new_move)
                if tuple(map(tuple, new_state)) not in visited:
                    queue.append(new_node)
                    visited.add(tuple(map(tuple, new_state)))
                    print(f"({move_number}, {parent}, {depth + 1}, {move_str})")
                    self.print_board(new_state)
                    last_board = new_state  # Actualiza el último tablero visitado
                    move_number += 1
        if last_board is not None:
            print("\nÚltimo tablero visitado:")
            self.print_board(last_board)

        return None

# Tablero objetivo
goal_board = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
# Crear una instancia del juego
puzzle = Puzzle(goal_board)
# Resolver el juego utilizando BFS
result = puzzle.solve()

if result:
    depth, move_number, moves = result[0], result[1], result[2]
    print("¡Solución encontrada!")
    print(f"Movimientos realizados: {moves}\n")
    print("Número de movimiento realizado:", move_number)
    print("Profundidad:", depth)
    print("Tablero inicial:")
    puzzle.print_board(puzzle.initial_state)
    print("Tablero final:")
    puzzle.print_board(puzzle.goal_state)  # Imprimir el tablero de solución
else:
    print("Tablero inicial:")
    puzzle.print_board(puzzle.initial_state)
    print("No se encontró una solución.\n")