FROM mariadb:latest

ENV MYSQL_DATABASE=FormulaNone
ENV MYSQL_USER=Tubes
ENV MYSQL_PASSWORD=Tubes
ENV MYSQL_ROOT_PASSWORD=Tubes

COPY db/ /docker-entrypoint-initdb.d/

EXPOSE 3306