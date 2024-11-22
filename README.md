# Tetris Game in Python

Dies ist eine einfache Implementierung des klassischen Tetris-Spiels in Python mit der `pygame`-Bibliothek. Das Spiel unterstützt Level, steigende Schwierigkeitsgrade und die grundlegenden Tetris-Funktionen.

## Funktionsweise

Das Spiel funktioniert auf einem 10x20-Raster, wobei die Spieler die Tetrominos (Tetris-Blöcke) steuern, um sie in eine sinnvolle Anordnung zu bringen. Wenn eine Reihe vollständig ausgefüllt ist, wird sie gelöscht, und der Spieler erhält Punkte.

### Steuerung
- **Pfeiltaste nach links**: Bewege das aktuelle Tetromino nach links.
- **Pfeiltaste nach rechts**: Bewege das aktuelle Tetromino nach rechts.
- **Pfeiltaste nach unten**: Bewege das aktuelle Tetromino nach unten (beschleunigt den Fall).
- **Pfeiltaste nach oben**: Drehe das aktuelle Tetromino um 90 Grad.

### Level und Schwierigkeit
- Zu Beginn startet das Spiel auf Level 1.
- Die Geschwindigkeit, mit der die Tetrominos fallen, erhöht sich mit jedem erreichten Punktestand.
- Das Level wird mit der Punktzahl des Spielers erhöht.

### Spielende
Das Spiel endet, wenn das Spielfeld so voll ist, dass das neue Tetromino nicht mehr in das Spielfeld eingefügt werden kann. Nach dem Spiel wird "Game Over" angezeigt, und du kannst das Spiel neu starten.

## Installation

Stelle sicher, dass Python 3.x und die `pygame`-Bibliothek auf deinem Computer installiert sind.

### 1. Python 3.x installieren

Falls noch nicht geschehen, lade Python von der offiziellen Seite herunter und installiere es: [python.org](https://www.python.org/downloads/).

### 2. Pygame installieren

Installiere die `pygame`-Bibliothek mit pip:

```bash
pip install pygame
```

## Ausführen des Spiels

1. Lade das Repository herunter oder klone es:

```bash
git clone https://github.com/dein-benutzername/tetris-python.git
cd tetris-python
```

2. Führe das Spiel aus:

```bash
python3 tetris.py
```

## Code-Details

### Hauptfunktionen

1. **`Tetris` Klasse**:
   - Diese Klasse verwaltet das Spielfeld, die Tetrominos und das Spielgeschehen.
   - Sie enthält Methoden zur Validierung von Bewegungen, zum Drehen der Formen und zum Löschen von Linien.

2. **`draw_grid` Funktion**:
   - Zeichnet das Spielfeld und das aktuell fallende Tetromino.

3. **`main` Funktion**:
   - Die Hauptspiel-Schleife. Sie kümmert sich um die Eingabe der Benutzersteuerung und aktualisiert das Spielgeschehen regelmäßig.
   - Sie verwaltet auch das Timing für die Geschwindigkeit der fallenden Tetrominos.

### Farben und Formen
- Die Tetrominos haben verschiedene Farben, die zufällig ausgewählt werden.
- Jede Form hat eine spezifische Matrix, die ihre Struktur darstellt.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert – siehe die [LICENSE](LICENSE) Datei für Details.
