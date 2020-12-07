# hello_world_flask
A Hello World Flask application to be deployed with apache. This is a very simple example of a flask application with a very simple configuration for apache. Has been tested on Ubuntu 20.04 with python3 and anaconda

### Some intructions

* The file **hello_world_flask.conf** sould be copied to "/etc/apache2/sites-available/"

* Need to disable the default apache site
```
sudo a2dissite 000-default.conf
sudo systemctl reload apache2
```

* To enable the application, just do

```
sudo a2ensite hello_world_flask.conf
sudo systemctl reload apache2
```

