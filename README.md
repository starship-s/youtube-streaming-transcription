# youtube-streaming-transcription
A Docker container which uses Google Cloud Platform's Speech-to-Text to provide live machine transcription of a YouTube livestream.

## What is this for?
While YouTube does provide live subtitling for some livestreams, I found no available way to extract those subtitles for use in other applications.  This container could also easily be modified to support any platform which streams audio through a web browser.

## How to use this container
Once you have build the Docker container, you can spin up an instance using the YouTube video id (the part that comes after v=) as a parameter.