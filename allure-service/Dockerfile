FROM alpine:3.18.4

COPY . .

# Install Allure command-line tools
RUN apk update && apk add --no-cache \
    bash \
    curl \
    openjdk11 \
    unzip \
    wget && \
    curl -o allure.zip -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.24.1/allure-commandline-2.24.1.zip && \
    unzip allure.zip && \
    rm allure.zip && \
    mv allure-2.24.1 /allure && \
    ln -s /allure/bin/allure /usr/bin/allure

RUN allure --version

# Expose the default port for Allure server
EXPOSE 5050

RUN chmod a+x ./entrypoint.sh

# Start Allure server within /allure-results
ENTRYPOINT [ "./entrypoint.sh"]