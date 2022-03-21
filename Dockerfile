FROM kanekiken44/VortexUB:latest

RUN git clone -b master https://github.com/kanekiken44/VortexUb /home/vortex/ \
    && chmod 777 /home/vortex \
    && mkdir /home/vortex/bin/

# Copies config.env (if exists)
COPY config.env* /home/vortex/

# Setup Working Directory
WORKDIR /home/vortex/

# Finalization
CMD ["python3","-m","Vortex"]
