# Mediapop Django Middlewares

Middlewares used for mediapop's projects.


### Real IP
* Nginx:
```
set_real_ip_from 127.0.0.1;
real_ip_header X-Forwarded-For;
real_ip_recursive on;
```
* Django:
```
MIDDLEWARE_CLASSES = (
    # ...
    'mediapop.middleware.realip.RealIP',
    # ...
)
```
