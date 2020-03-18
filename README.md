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

* usual communication model in MVC or MTV (Model-Template-View):
![grafik](https://user-images.githubusercontent.com/6619191/76877882-4fa61180-6874-11ea-97e1-88b7d18722c2.png)


* running flask app without using a package (production environment):
   * download the code on the server 
   ```sh
    $ pip3 install -r requirements.txt
    $ sudo apt install gunicorn3
    $ gunicorn3 -D flashcards:app
    now the deamon is running on port 8000
    we need to use nginx tp have a reverse proxy
    $ cd /etc/nginx/sites-available/
    get settings from : https://gunicorn.org/#deployment
    change server_name and access_log 
    $ sudo nano default 
      server {
          listen 80;
          server_name example.org;
          access_log  /var/log/nginx/example.log;

          location / {
              proxy_pass http://127.0.0.1:8000;
              proxy_set_header Host $host;
              proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
             }
     }
    
    $ sudo service nginx restart  
   ```
