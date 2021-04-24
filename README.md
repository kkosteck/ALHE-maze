# Algorytmy heurystyczne - projekt
## Treść zadania:
>Zostałeś poproszony o stworzenie programu, który będzie wizualizował ścieżkę między wejściem, a wyjściem labiryntów różnego rozmiaru.

## Użyte biblioteki:
```
python -m pip install matplotlib
python -m pip install anytree
```

## Generowanie labiryntów:
Randomized Kruskal's Algorithm:
- wygenerowanie wierzchołków indeksowanych numerycznie oraz krawędzi między każdym wierzchołkiem
- lista krawędzi zostaje przetasowana, dzięki czemu otrzymuje za każdym razem losowy labirynt
- na podstawie wylosowanych krawędzi sprawdzamy, czy dwa wierzchołki należą do tego samego drzewa, jeśli nie to pierwszy wierzchołek zostaje rodzicem drugiego
- labirynt jest przedstawiony jako tablica dwuwymiarowa
