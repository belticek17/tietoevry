# Visualizer of CI Jobs - Spotify artist's top tracks (home assignment for Tietoevry internship)

## Development:
### Installing requirements:
```bash
pip install -r requirements.txt
```
### Starting the application:
Change your account credentials on line 6 and 7 in:
```bash
app.py
```
The visualizer can be started by this command:
```bash
python3 app.py
```
### Bugs:
The Spotify API has a bug - album's genres return an empty array since its launch.

Done, now just visit http://127.0.0.1:5000/