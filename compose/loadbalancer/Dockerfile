FROM nginx:stable-alpine

COPY /compose/loadbalancer/nginx.conf /etc/nginx/nginx.conf
COPY /compose/loadbalancer/502.html /etc/nginx/error/502.html
COPY /compose/loadbalancer/403.html /etc/nginx/error/403.html