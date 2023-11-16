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
#RUN apt install -y fonts-texgyre libdigest-hmac-perl libgssapi-perl colord gdbm-l10n gvfs libcrypt-ssleay-perl librsvg2-bin libsub-name-perl libbusiness-isbn-perl
#RUN apt install -y libauthen-ntlm-perl libunicode-map8-perl libunicode-string-perl xml-twig-tools texlive-latex-recommended texlive-xetex texlive-luatex
#RUN apt install -y pandoc-citeproc texlive-latex-extra context wkhtmltopdf groff ghc nodejs php ruby r-base-core libjs-mathjax libjs-katex
#RUN apt install -y citation-style-language-styles perl-doc libterm-readline-gnu-perl make libtap-harness-archive-perl poppler-utils
#RUN apt install -y ghostscript fonts-ipafont-mincho fonts-ipafont-gothic fonts-arphic-ukai fonts-arphic-uming fonts-nanum debhelper gv perl-tk xpdf
#RUN apt install -y xzdec texlive-latex-base-doc mesa-utils nickle
# python-nautilus?

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