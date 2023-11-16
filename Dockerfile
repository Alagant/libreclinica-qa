FROM ubuntu:22.04
LABEL maintainer="edenilsonpineda@outlook.com"

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

##WORKDIR /app

COPY . .

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install ./google-chrome-stable_current_amd64.deb -y
RUN python3 -m venv venv
#RUN venv/bin/python -mp venv/bin/activate
RUN venv/bin/python -mpip install --no-cache-dir -r requirements.txt
RUN chmod a+x /entrypoint.sh
RUN ls -la /



ENTRYPOINT [ "./entrypoint.sh" ]