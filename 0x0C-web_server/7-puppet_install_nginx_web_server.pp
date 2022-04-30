# Ussing puppet - intall Server Nginx and confugure rediret_me
# Install Ngin
exec {'Install_nginx':
  provider => shell,
  command  => 'sudo apt-get -y update ;\
               sudo apt-get -y install nginx ;\
               sudo chown -R ubuntu /var/www ;\
               sudo service nginx start',
}
# Configure redirect_me
exec {'Configure_redirect':
  provider => shell,
  command  => 'echo "Hello World" > /var/www/html/index.nginx-debian.html ;\
               sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/github.com\/mrgiulls permanent;/" /etc/nginx/sites-available/default ;\
               sudo service nginx restart',
}