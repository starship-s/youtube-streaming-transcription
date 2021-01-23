import os
import sys
# import pyaudio
from threading import Thread


from open_webpage import open_video_stream
from stream_audio import transcribe

if __name__ == '__main__':
    os.system('pulseaudio -D')

    # class textcolors:
    #     if not os.name == 'nt':
    #         blue = '\033[94m'
    #         green = '\033[92m'
    #         warning = '\033[93m'
    #         fail = '\033[91m'
    #         end = '\033[0m'
    #     else:
    #         blue = ''
    #         green = ''
    #         warning = ''
    #         fail = ''
    #         end = ''

    # p = pyaudio.PyAudio()l

    # print(textcolors.blue + "Available devices:\n" + textcolors.end)
    # for i in range(0, p.get_device_count()):
    # info = p.get_device_info_by_index(i)
    # print(textcolors.green + str(info["index"]) + textcolors.end + ": \t %s \n \t %s \n" % (
    # info["name"], p.get_host_api_info_by_index(info["hostApi"])["name"]))

    t1 = Thread(target=open_video_stream, args=(sys.argv[1],))

    t1.start()

    transcribe(sys.argv[1])
