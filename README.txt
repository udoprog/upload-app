This file is for you to describe the upload-app application. Typically
you would include information such as the information below:

Installation and Setup
======================

Install ``upload-app`` using easy_install::

    easy_install upload-app

Make a config file as follows::

    paster make-config upload-app config.ini

Tweak the config file as appropriate and then setup the application::

    paster setup-app config.ini

Then you are ready to go.
This is a simple uploading application written in Pylons (http://pylonshq.com) which binds to a local linux filesystem with no database backend at all.
It uses REMOTE_USER (Http basic authentication supplied by the server) to tell if a user is logged in or not (that is the reason there is no 'Logout' button).

Basically, it is designed to run begind a reverse proxy.

Example configuration for nginx follows:

<pre>
server {
  listen 80;
  rewrite /(.*) https://toolchain.eu/$1 last;
}

server {
  listen 443;
  server_name toolchain.eu;
  client_max_body_size 500M;
  
  rewrite ^/$ /upload/ last;
  
  location /static/ {
    internal;
    expires 1h;
    alias /path/to/upload/directory/;
  }
  
  location /upload/login {
    auth_pam              "Upload";
    auth_pam_service_name "nginx";
    
    root /var/www/upload-app/uploadapp/public;
    
    rewrite ^/upload/(.*)$ /$1 break;
    
    # host/port combination where upload-app is running locally
    proxy_pass http://127.0.0.1:5000;
    proxy_redirect default;
    
    proxy_set_header   REMOTE_USER      $remote_user;
    proxy_set_header   Host             $host;
    proxy_set_header   X-Real-IP        $remote_addr;
    proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
  }
  
  location /upload/ {
    root /var/www/upload-app/uploadapp/public;
    
    rewrite ^/upload/(.*)$ /$1 break;
    
    proxy_pass http://127.0.0.1:5000;
    proxy_redirect default;
    
    proxy_set_header   REMOTE_USER      $remote_user;
    proxy_set_header   Host             $host;
    proxy_set_header   X-Real-IP        $remote_addr;
    proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
  }
  
  ssl on;
  ssl_certificate /etc/nginx/host.pem;
  ssl_certificate_key /etc/nginx/host.pem;
}
</pre>

Please note that this uses pam to authenticate users, this is my /etc/pam.d/nginx file:
<pre>
@include common-auth
</pre>

common-auth is a directive (or rather a set of pam directives) which comes bundled with debian.

=== Usage ===
In most situations, upload-app tries to mimic the way a normal filesystems works with permissions, there is a special library routine written for this called 'doas' which spawns a child process that performs user-specific tasks like creating directories, removing files (etc...) which makes sure that filesystem-level permissions will not be ignored.
There is also a specific library called lib/fakeuser.py which makes it more simple to handle authenticated user permissions.

Some things are also simulated:
If a user is not logged in, the user config['uploadapp.nobody'] is used automatically (see lib/base.py for the implementation).
If a directory is not readable by current user (either through user, group or other permission), it will not be listed - same goes with files.
If a directory is readable by others, it will be readable by nobody, same goes with writable.
Execute permissions does not make much sense unless you are familiar with how a linux filesystem works, the implementation for upload-app might change in the future to reflect this, but for now just use the darn thing.

=== Warning ===
ONE MAJOR DOWNSIDE with this approach is that the webserver has to run as a user priviliged to setuid to all server users. The easiest way to do this is by running as root, but this is a MAJOR DO AT YOUR OWN RISK. I will not be held responsible for remote code exploits. You have been warned.
