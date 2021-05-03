# Algorytmy heurystyczne - projekt
## Treść zadania:
>Zostałeś poproszony o stworzenie programu, który będzie wizualizował ścieżkę między wejściem, a wyjściem labiryntów różnego rozmiaru.

## Użyte biblioteki:
```
python -m pip install pygame
python -m pip install matplotlib
python -m pip install anytree
```
## Uruchomienie:
```
python main.py
```
# Implementacja:
## Generowanie labiryntów - zrandomizowany algorytm Kruskala:
- wygenerowanie wierzchołków indeksowanych numerycznie oraz krawędzi między każdym wierzchołkiem
- lista krawędzi zostaje przetasowana, dzięki czemu otrzymuje za każdym razem losowy labirynt
- na podstawie wylosowanych krawędzi sprawdzamy, czy dwa wierzchołki należą do tego samego drzewa, jeśli nie to pierwszy wierzchołek zostaje rodzicem drugiego
- labirynt jest przedstawiony jako tablica dwuwymiarowa
## Rozwiązywanie labiryntów - Algorytm A*:
- labirynt jest przedstawiony jako tablica, gdzie dana liczba odpowiada rodzajowi pola:
  - 0, biały - puste pole możliwe do przejścia
  - 1, czarny - ściana niemożliwa do przejścia
  - 2, zielony - pole już sprawdzone przez algorytm oraz dodane do ścieżki
  - 3, czerwony - pole czekające w kolejce na sprawdzenie
  - 4, niebieski - pole ostatecznie znalezionej ścieżki
- algorytm przeszukuje możliwe do przejścia pola obliczając wartość funkcji celu: funkcja kosztu (dotychczas przebyta odległość) + funkcja heurystyczna
- W algorytmie zawarte są 3 różne funkcje heurystyczne, które zostają wybrane ręcznie:
  - odległość sprawdzanego pola do pola docelowego w osi x + w osi y
  - bezpośrednia odległość sprawdzanego pola do pola docelowego
  - w zależności od wymiarów labiryntu:
    - jeśli labirynt jest szerszy to odległość w osi x do pola docelowego
    - jeśli labirynt jest wyższy to odległość w osi y do pola docelowego
## Wizualizacja - pygame:
- labirynt rysowany jest za pomocą prostokątów
- każda komórka danych reprezentujących labirynt , które są przedstawione jako tablica dwuwymiarowa, jest kwadratem danego koloru
![Alt Text](https://github.com/kkosteck/ALHE-maze/blob/main/maze.gif)
