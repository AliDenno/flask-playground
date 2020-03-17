# flask-playground
* install flask:
   ```sh
    python -m pip install flask 
   ```
   
* running flask app (only for development purposes):
   ```sh
    $ export FLASK_APP=flashcards.py 
    $ export FLASK_ENV=development 
    $ flask run
      or
    $ python –m flask run 
   ```
   -For windows, use set instead of export-
   
* overview of the app (which methods and functionaliy are available):
  - go to the direcroy and start python in the terminal (IDE terminal or Standalone terminal)
   ```sh
    $ python
    $ import flashcards
    $ flashcards.app.url_map
   ```
