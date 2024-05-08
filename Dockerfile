FROM tomcat:9.0-jre8-temurin-jammy

RUN apt-get update && \
    apt-get install -y unzip ffmpeg python3; \
	rm -rf /var/lib/apt/lists/*

ENV WEBRUN_HOME=/usr/local/tomcat/settings

RUN mkdir -p ${WEBRUN_HOME}/systems

COPY . /tmp

RUN mv /tmp/ROOT.war /usr/local/tomcat/webapps/ && \
    mv /tmp/context.xml /usr/local/tomcat/conf/ && \
    mv /tmp/Conexcondo.wfre /usr/local/tomcat/settings/systems/ && \
    mv /tmp/Conexcondo.jar /usr/local/tomcat/settings/systems/ && \
    mv /tmp/config/ /usr/local/tomcat/settings/ && \
    mv /tmp/wfre.py /usr/local/tomcat/wfre.py  && \
    mv /tmp/entrypoint.sh /usr/local/bin/entrypoint.sh

ENTRYPOINT ["entrypoint.sh"]

CMD ["catalina.sh", "run"]