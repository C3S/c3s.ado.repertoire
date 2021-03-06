ARG ENVIRONMENT
ARG WORKDIR
ARG DEBUGGER_WINPDB
ARG DEBUGGER_PTVSD


#==============================================================================
# Base Images (Jessie)
#==============================================================================

#--- BASE ---------------------------------------------------------------------

### production
FROM debian:jessie-slim AS jessie_base_production
# set workdir
ARG WORKDIR
ENV WORKDIR $WORKDIR
ENV PATH $PATH:$WORKDIR
RUN mkdir -p $WORKDIR
WORKDIR $WORKDIR
# configure apt
ENV DEBIAN_FRONTEND noninteractive
# install base packages
RUN apt-get update && apt-get install -y --no-install-recommends \
        locales \
        ssl-cert \
        ca-certificates \
        libmagic1 \
    && rm -rf /var/lib/apt/lists/*
# configure language
RUN localedef -i en_US -f UTF-8 en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

### staging
FROM jessie_base_production AS jessie_base_staging

### testing
FROM jessie_base_staging AS jessie_base_testing

### development
FROM jessie_base_testing AS jessie_base_development
# install development packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    && apt-get install -y --no-install-recommends \
        git \
        htop \
        iputils-ping \
        net-tools \
        vim \
        nano \
    && rm -rf /var/lib/apt/lists/*

### result
FROM jessie_base_${ENVIRONMENT} AS jessie_base


#--- base -> PYTHON -----------------------------------------------------------

### production
FROM jessie_base AS jessie_python_production
# install python
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y --no-install-recommends \
    && apt-get install -y --no-install-recommends \
        curl \
        python \
    && rm -rf /var/lib/apt/lists/*
# install pip
RUN curl -s https://bootstrap.pypa.io/pip/2.7/get-pip.py | python
# create virtual environment
RUN pip install virtualenv
RUN python -m virtualenv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
ENV VIRTUAL_ENV=/opt/venv
# set default entrypoint and cmd for CLI script
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["cli --help"]

### staging
FROM jessie_python_production AS jessie_python_staging

### testing
FROM jessie_python_staging AS jessie_python_testing

### development
FROM jessie_python_testing AS jessie_python_development

### result
FROM jessie_python_${ENVIRONMENT} AS jessie_python


#--- base -> python -> TRYTOND ------------------------------------------------

### production
FROM jessie_python AS jessie_trytond_production
# install database packages
RUN for i in $(seq 1 8); do mkdir -p "/usr/share/man/man${i}"; done \
    && apt-get update && apt-get install -y --no-install-recommends \
        postgresql-client-9.4  \
        sqlite3 \
        libxslt1.1 \
        graphviz \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /usr/share/man/*

### staging
FROM jessie_trytond_production AS jessie_trytond_staging

### testing
FROM jessie_trytond_staging AS jessie_trytond_testing

### development
FROM jessie_trytond_testing AS jessie_trytond_development

### result
FROM jessie_trytond_${ENVIRONMENT} AS jessie_trytond


#--- base -> python -> ECHOPRINT ----------------------------------------------

### production
FROM jessie_python AS jessie_echoprint_production
RUN for i in $(seq 1 8); do mkdir -p "/usr/share/man/man${i}"; done \
    && apt-get update && apt-get install -y --no-install-recommends \
        default-jre-headless \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /usr/share/man/*
RUN mkdir /opt/echoprint-data

### staging
FROM jessie_echoprint_production AS jessie_echoprint_staging

### testing
FROM jessie_echoprint_staging AS jessie_echoprint_testing

### development
FROM jessie_echoprint_testing AS jessie_echoprint_development

### result
FROM jessie_echoprint_${ENVIRONMENT} AS jessie_echoprint


#--- base -> python -> WORKER -------------------------------------------------

### production
FROM jessie_python AS jessie_worker_production
RUN apt-get update && apt-get install -y --no-install-recommends \
        cron \
        libav-tools \
        libtag1-vanilla \
    && rm -rf /var/lib/apt/lists/*
RUN ln -s /usr/bin/avconv /usr/local/bin/ffmpeg

### staging
FROM jessie_worker_production AS jessie_worker_staging

### testing
FROM jessie_worker_staging AS jessie_worker_testing
# install database packages
RUN for i in $(seq 1 8); do mkdir -p "/usr/share/man/man${i}"; done \
    && apt-get update && apt-get install -y --no-install-recommends \
        postgresql-client-9.4  \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /usr/share/man/*

### development
FROM jessie_worker_testing AS jessie_worker_development

### result
FROM jessie_worker_${ENVIRONMENT} AS jessie_worker


#--- base -> python -> COMPILE ------------------------------------------------

FROM jessie_python AS jessie_compile
# install libs
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        git \
        python-dev \
        # pip: lxml \
            libxml2-dev \
            libxslt-dev \
        # pip: psycopg2 \
            libpq-dev \
        # pip: pyOpenSSL \
            libssl-dev \
            libffi-dev \
        # pip: pytaglib \
            libtag1-dev \
        # echoprint-codegen \
            libboost-dev \
            zlib1g-dev \
        # echoprint-server
            libbz2-dev \
            wget \
    && rm -rf /var/lib/apt/lists/*


#==============================================================================
# Compilation Images
#==============================================================================

#--- [COMPILE] PYTHON ---------------------------------------------------------

### production
FROM jessie_compile AS jessie_python_production_compiled
RUN pip install \
    click==7.1.2

### staging
FROM jessie_python_production_compiled AS jessie_python_staging_compiled

### testing
FROM jessie_python_staging_compiled AS jessie_python_testing_compiled
RUN pip install \
    autoapi==2.0.1 \
    coverage==5.5 \
    flake8==3.9.1 \
    nose==1.3.7 \
    nose2==0.10.0 \
    pytest==4.6.11 \
    sphinx==1.8.5 \
    sphinx_rtd_theme==0.5.2 \
    tox==3.23.0

### development
FROM jessie_python_testing_compiled AS jessie_python_development_compiled
RUN pip install \
    pdbpp==0.10.2

ARG DEBUGGER_PTVSD
RUN if [ ${DEBUGGER_PTVSD} -ne 0 ]; then pip install \
        ptvsd==4.3.2; \
    fi
ARG DEBUGGER_WINPDB
RUN if [ ${DEBUGGER_WINPDB} -ne 0 ]; then pip install \
        winpdb==1.3.6; \
    fi

### result
FROM jessie_python_${ENVIRONMENT}_compiled AS jessie_python_compiled

#--- [COMPILE] python -> ECHOPRINT --------------------------------------------

### production
FROM jessie_python_compiled AS jessie_echoprint_production_compiled

# install tokyo cabinet (from https://github.com/jon-eckstein/docker-echoprint-server)
RUN wget https://fallabs.com/tokyocabinet/tokyocabinet-1.4.48.tar.gz
RUN tar xvf tokyocabinet-1.4.48.tar.gz
RUN mkdir /opt/tokyocabinet/
RUN cd tokyocabinet-1.4.48 && ./configure --prefix=/opt/tokyocabinet/ && make && make install

# install tokyo tyrant
RUN wget https://fallabs.com/tokyotyrant/tokyotyrant-1.1.41.tar.gz
RUN tar xvf tokyotyrant-1.1.41.tar.gz
RUN mkdir /opt/tokyotyrant
RUN cd tokyotyrant-1.1.41 && ./configure --prefix=/opt/tokyotyrant/ --with-tc=/opt/tokyocabinet && make && make install

# install python packages
RUN pip install \
    web.py==0.51 \
    pyechonest==9.0.0

### staging
FROM jessie_echoprint_production_compiled AS jessie_echoprint_staging_compiled

### testing
FROM jessie_echoprint_staging_compiled AS jessie_echoprint_testing_compiled

### development
FROM jessie_echoprint_testing_compiled AS jessie_echoprint_development_compiled

### result
FROM jessie_echoprint_${ENVIRONMENT}_compiled AS jessie_echoprint_compiled

#--- [COMPILE] python -> TRYTOND ----------------------------------------------

### production
FROM jessie_python_compiled AS jessie_trytond_production_compiled
# trytond mandatory
RUN pip install \
    lxml==4.6.3 \
    polib==1.1.1 \
    python-dateutil==2.8.1 \
    python-sql==1.2.1 \
    relatorio==0.9.2
# trytond optional
RUN pip install \
    "proteus<3.5.0" \
    interlude==1.3.1 \
    mock==3.0.5 \
    py-bcrypt==0.4 \
    psycopg2==2.8.6 \
    pydot==1.4.1 \
    python-Levenshtein==0.12.2 \
    PyWebDAV==0.9.8 \
    simplejson==3.17.2
# additional
RUN pip install \
    hurry.filesize==0.9 \
    pyOpenSSL==20.0.1 \
    pytz==2021.1 \
    requests==2.25.1 \
    vatnumber==1.2

### staging
FROM jessie_trytond_production_compiled AS jessie_trytond_staging_compiled

### testing
FROM jessie_trytond_staging_compiled AS jessie_trytond_testing_compiled

### development
FROM jessie_trytond_testing_compiled AS jessie_trytond_development_compiled

### result
FROM jessie_trytond_${ENVIRONMENT}_compiled AS jessie_trytond_compiled


#--- [COMPILE] python -> trytond -> PYRAMID -----------------------------------

### production
FROM jessie_trytond_compiled AS jessie_pyramid_production_compiled
RUN pip install \
    colander==1.8.3 \
    cornice==4.0.1 \
    cornice-swagger==0.7.0 \
    cryptacular==1.4.1 \
    Pillow==6.2.2 \
    deform==2.0.6 \
    pyramid==1.10.8 \
    pyramid-beaker==0.8 \
    pyramid-chameleon==0.3 \
    pyramid-mailer==0.15.1 \
    python-magic==0.4.22 \
    waitress==1.4.4

### staging
FROM jessie_pyramid_production_compiled AS jessie_pyramid_staging_compiled

### testing
FROM jessie_pyramid_staging_compiled AS jessie_pyramid_testing_compiled
RUN pip install \
    raven==6.10.0 \
    selenium==3.141.0 \
    WebTest==2.0.35

### development
FROM jessie_pyramid_testing_compiled AS jessie_pyramid_development_compiled
RUN pip install \
    pyramid-debugtoolbar==4.9

### result
FROM jessie_pyramid_${ENVIRONMENT}_compiled AS jessie_pyramid_compiled


#--- [COMPILE] python -> WORKER -----------------------------------------------

### production
FROM jessie_python_compiled AS jessie_worker_production_compiled
# compile echoprint-codegen
RUN git clone https://github.com/spotify/echoprint-codegen.git /opt/echoprint-codegen \
    && git -C /opt/echoprint-codegen checkout v4.12 \
    && make -C /opt/echoprint-codegen/src \
    && chmod 755 /opt/echoprint-codegen/echoprint-codegen
# install pip packages
RUN pip install  \
    "proteus<3.5.0" \
    pyechonest==9.0.0  \
    pydub==0.25.1  \
    pytaglib==1.4.6  \
    requests==2.25.1

### staging
FROM jessie_worker_production_compiled AS jessie_worker_staging_compiled

### testing
FROM jessie_worker_staging_compiled AS jessie_worker_testing_compiled

### development
FROM jessie_worker_testing_compiled AS jessie_worker_development_compiled

### result
FROM jessie_worker_${ENVIRONMENT}_compiled AS jessie_worker_compiled


#==============================================================================
# Service Images
#==============================================================================

#--- DATABASE -----------------------------------------------------------------

FROM postgres:9.6.16 AS database


#--- WEBSERVER ----------------------------------------------------------------

FROM jwilder/nginx-proxy AS webserver


#--- BROWSER ------------------------------------------------------------------

FROM selenium/standalone-firefox AS browser


#--- base -> python -> FINGERPRINTING -----------------------------------------

FROM jessie_echoprint AS fingerprint
COPY --from=jessie_echoprint_compiled /opt/tokyocabinet/bin/* /bin/
COPY --from=jessie_echoprint_compiled /opt/tokyocabinet/lib/libtokyocabinet.* /lib/
COPY --from=jessie_echoprint_compiled /opt/tokyotyrant/bin/* /bin/
COPY --from=jessie_echoprint_compiled /opt/tokyotyrant/lib/libtokyotyrant.* /lib/
COPY --from=jessie_echoprint_compiled /opt/tokyotyrant/lib/ttskel* /lib/
COPY --from=jessie_echoprint_compiled /opt/venv /opt/venv


#--- base -> python -> WORKER -------------------------------------------------

FROM jessie_worker AS worker
COPY --from=jessie_worker_compiled /opt/echoprint-codegen/echoprint-codegen /usr/local/bin/echoprint-codegen
COPY --from=jessie_worker_compiled /opt/venv /opt/venv
COPY worker.cron /etc/cron.d/worker


#--- base -> python -> trytond -> ERPSERVER -----------------------------------

FROM jessie_trytond AS erpserver
COPY --from=jessie_trytond_compiled /opt/venv /opt/venv


#--- base -> python -> trytond -> WEBAPI --------------------------------------

FROM jessie_trytond AS webapi
COPY --from=jessie_pyramid_compiled /opt/venv /opt/venv


#--- base -> python -> trytond -> WEBGUI --------------------------------------

FROM webapi AS webgui


#--- base -> python -> DOCUMENTATION ------------------------------------------

FROM jessie_compile AS documentation
COPY --from=jessie_trytond_compiled /opt/venv /opt/venv
COPY --from=jessie_pyramid_compiled /opt/venv /opt/venv
COPY --from=jessie_worker_compiled /opt/venv /opt/venv
