
Dependenci cintrol
---------
- Pipenv

Code cuqality utils:
------

- Flake9 - for control. command: flake ./
- Black - for code format. command: black ./
- Isort - for imports control. command: isort ./
- pre-commit-config.yaml - specific file to chek stage code cuqality before pushing.

Installed packs:
------

- django 4.0.6
- requests 2.28.1
- response 0.2.0
- djangorestframework 3.13.1 - must be add to installed apps
- django-stubs 1.12.0
- django-debug-toolbar (last version)
- django-extensions 3.2.0 - must be add to installed apps

### Directory descriptions
> authentication: 
  >- Main project models includ custom User model
>- services - mixin file with get_user() method

> config:
  >- main prodject settings

> core:
>- some prodject models
>- api - basic logig
>- serializers for project models 

> Exchange_rates:
>- some practice with collect requst resilts in objects

> shared:
>- mixin classes