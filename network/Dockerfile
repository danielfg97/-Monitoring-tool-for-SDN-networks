FROM ubuntu:16.04

MAINTAINER Daniel Fernandez Gordo

ARG user
ARG uid
ARG gid

ENV USERNAME ${user}
RUN useradd -m $USERNAME && \
        echo "$USERNAME:$USERNAME" | chpasswd && \
        usermod --shell /bin/bash $USERNAME && \
        usermod  --uid ${uid} $USERNAME && \
        groupmod --gid ${gid} $USERNAME

USER root

WORKDIR /home/${user}

COPY ENTRYPOINT.sh /


RUN apt-get update && apt-get install -y --no-install-recommends \
    sudo \
    curl \
    bridge-utils \
    iproute2 \
    iputils-ping \
    mininet \
    net-tools \
    iperf3 \
    openssh-server \
    openssh-client \
    openvswitch-switch \
    openvswitch-testcontroller \
    tcpdump \
    vim \
    x11-xserver-utils \
    xterm \
    wget \
    wireshark \
 && rm -rf /var/lib/apt/lists/* \
 && chmod +x /ENTRYPOINT.sh

RUN apt-get update && apt-get install -y \
    perl-doc \
    libhtml-parser-perl \
    libio-socket-ssl-perl \
    goldeneye

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \
 && apt install apt-transport-https ca-certificates \
 && echo "deb https://download.mono-project.com/repo/ubuntu stable-xenial main" | tee /etc/apt/sources.list.d/mono-official-stable.list \
 && apt update

RUN apt install -y --fix-missing mono-complete

RUN apt-get install -y tshark tcpdump git


EXPOSE 6633 6653 6640

ENTRYPOINT ["/ENTRYPOINT.sh"]
