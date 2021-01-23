#Contents of Dockerfile
FROM ubuntu

 
# Essential tools and xvfb
RUN apt-get update && apt-get install -y \
    software-properties-common \
    unzip \
    curl \
    xvfb \
    wget \
    ffmpeg

# Firefox browser to run the script
RUN apt-get install -y firefox
 

 
# python
RUN apt-get update && apt-get install -y \
    python \
    python-setuptools \
    python3-pip

  
WORKDIR /usr/local/bin	

# bring accross python scripts
COPY requirements.txt /usr/local/bin
COPY uBlock0@raymondhill.net.xpi /usr/local/bin
COPY __main__.py .
COPY stream_audio.py .
COPY translate_text.py .
COPY open_webpage.py .
COPY aniki-581d42db82da.json /usr/local/bin
COPY geckodriver /usr/local/bin
COPY .env /usr/local/bin
COPY aniki-289104-firebase-adminsdk-kuhg2-93690e9ccb.json /usr/local/bin


RUN apt install libasound-dev portaudio19-dev libportaudio2 -y \
  && apt-get -qq update && apt-get install -y pulseaudio \
  && apt install python3-pyaudio -y

RUN apt-get -qq update && apt-get install -y pulseaudio

RUN apt install python3-pyaudio -y
	
RUN pip3 install --upgrade pip	\
  && pip3 install --upgrade setuptools \
  && pip3 install -r requirements.txt
#RUN pip3 install --upgrade setuptools
#RUN pip3 install -r requirements.txt

COPY dockerrun.sh /usr/local/bin/dockerrun.sh 
COPY daemon.conf /etc/pulse
RUN chmod +x /usr/local/bin/dockerrun.sh 
#CMD ["dockerrun.sh"]
