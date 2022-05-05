<div align="center">

# Challenge-Rocketbot

![GitHub repo size](https://img.shields.io/github/repo-size/AucaCoyan/challenge-rocketbot)
![Lines of code](https://img.shields.io/tokei/lines/github/AucaCoyan/challenge-rocketbot)
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/AucaCoyan/challenge-rocketbot)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Hacer un bot para comparar los beneficios de usar rocketbot como herramienta

</div>

## Parte 1: el rocketbot

Construir un Robot en Rocketbot que procese la información del excel adjunto, con las siguientes reglas:

- Si el estado del proceso (Columna J) es `Regularizado`, subir la información al formulario Formulario Auditoria con la información correspondiente.
- Si el estado del proceso es `Atrasado`, enviar un mail al responsable. El mail debe indicar el proceso, el estado, la observación y la fecha de compromiso.
- Los estados `Pendientes`, deben ser ignorados.
- El robot debe cumplir con buenas prácticas y usar al menos dos sub robots. Para el trabajo de excel, puedes usar los comandos de xlsx en Archivos o Excel en integración con aplicaciones.

### Recursos:

- Link de descarga de Rocketbot: https://www.rocketbot.com/es/studio/#downloads
- Página para solicitud de licencia: license.rocketbot.co
- Cursos nivel 1: https://academy.rocketbot.co/cursos/rocketbot-suite-level-1/
- Módulo Fechas: https://market.rocketbot.co/module/Fechas
- Activación de licencia: Video adjunto
- Marketplace: https://market.rocketbot.co

## Parte 2: el bot equivalente de Python

Construir un robot en Python que realice las mismas actividades que la parte 1.

Recursos de interés:

- Selenium: https://selenium-python.readthedocs.io/
- Xlwings: https://docs.xlwings.org/en/stable/quickstart.html
- Openpyxl: https://openpyxl.readthedocs.io/en/stable/
