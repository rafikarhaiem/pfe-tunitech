FROM php:7.3-apache-stretch
RUN apt-get update && apt-get install -y \
    build-essential \
    vim \
    nano
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
COPY ./vendor /var/www/html/vendor
COPY . /var/www/html
COPY vhost.conf /etc/apache2/sites-available/000-default.conf
COPY start.sh /usr/local/bin/start

RUN docker-php-ext-install pdo pdo_mysql pcntl

RUN chown -R www-data:www-data /var/www/html \
    && chmod u+x /usr/local/bin/start \
    && a2enmod rewrite

CMD ["/usr/local/bin/start"]

