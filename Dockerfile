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
    chromium-browser

WORKDIR /app

COPY . .

RUN apt-get install ./executables/google-chrome-stable_current_amd64.deb -y --no-install-recommends
RUN python3 -m venv venv
RUN . venv/bin/activate
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod a+x ./entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh" ]