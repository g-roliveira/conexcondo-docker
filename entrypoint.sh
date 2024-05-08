#!/bin/sh
# Executa o script Python
python3 /usr/local/tomcat/wfre.py

# Inicia o servidor Tomcat
exec catalina.sh run
