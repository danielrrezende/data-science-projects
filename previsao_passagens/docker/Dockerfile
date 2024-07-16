FROM vonbraunlabs/php:7.4-apache-composer-redis-extended

COPY composer.json ./
COPY composer.lock ./
RUN set -ex \
    && mkdir -p /usr/share/man/man1/ /usr/share/man/man3/ /usr/share/man/man7/ \
    && apt-get update \
    && apt-get install -y mariadb-client \
    && printf "\n" | pecl install mongodb apcu \
    && docker-php-ext-enable mongodb apcu \
    && composer install --no-dev \
    && a2enmod headers \
    && if [ -f "/var/www/html/.htaccess" ]; then rm -f "/var/www/html/.htaccess" ; fi

COPY ports.conf /etc/apache2/
COPY 000-default.conf /etc/apache2/sites-enabled/
COPY index.php ./
COPY config/application.php ./config/application.php
COPY tools/genrsa.sh ./tools/genrsa.sh
RUN pwd
RUN ./tools/genrsa.sh
COPY src ./src/
RUN mkdir twig
COPY twig/template ./twig/template
RUN mkdir twig/cache && chmod 777 twig/cache/
COPY .htaccess ./
RUN set -ex \
    && install -d -m 0755 -o www-data -g www-data /var/www/html/logs \
    && install -d -m 0755 -o www-data -g www-data /var/www/html/ehook/logs

EXPOSE 8085

VOLUME ["/var/www/html/ehook/logs", "/var/www/html/logs"]
