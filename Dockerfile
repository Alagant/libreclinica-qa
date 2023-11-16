FROM ubuntu:22.04
LABEL maintainer="edenilsonpineda@outlook.com"
ENV DEBIAN_FRONTEND=noninteractive
# Install the required dependencies
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    wget \
    curl \
    python3 \
    python3-venv \
    python3-pip \
    chromium-driver \
    chromium-browser \
    default-jre \
    default-jdk

#Non interactive tzdata install
#RUN ln -fs /usr/share/zoneinfo/America/Mexico_City /etc/localtime
RUN apt-get install -y --no-install-recommends tzdata
RUN dpkg-reconfigure --frontend noninteractive tzdata

# Pandoc requirements
RUN apt install texlive-latex-base pandoc -y
RUN apt install -y cpp-doc gcc-11-locales fonts-noto fonts-freefont-ttf


# From the suggested packages:
RUN apt install texlive-fonts-recommended texlive-latex-extra texlive-fonts-extra texlive-latex-recommended -y
COPY . .

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install ./google-chrome-stable_current_amd64.deb -y
RUN python3 -m venv venv
RUN venv/bin/python -mpip install --upgrade pip
RUN venv/bin/python -mpip install setuptools wheel
RUN venv/bin/python -mpip install --no-cache-dir -r requirements.txt
RUN chmod a+x /entrypoint.sh


ENTRYPOINT [ "./entrypoint.sh" ]