#!/usr/bin/env python
import cv2
import gi
gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import GObject, Gst, GstRtspServer

def main():
    ip='192.168.88.227'
    rtsp_port_num = 8554 
    video_source="video/RGBT_RGB.mp4"
    
    out_send = cv2.VideoWriter('appsrc is-live=true ! videoconvert ! \
                                omxh264enc bitrate=12000000 ! video/x-h264, \
                                stream-format=byte-stream ! rtph264pay pt=96 ! \
                                udpsink host='+ip+' port='+str(rtsp_port_num)+ ' async=false',
                                cv2.CAP_GSTREAMER, 0, 30, (1920,1080), True)

    if not out_send.isOpened():
        print('VideoWriter not opened')
        exit(0)
 
    server = GstRtspServer.RTSPServer.new()
    server.props.service = "%d" % rtsp_port_num
    server.attach(None)
    
    factory = GstRtspServer.RTSPMediaFactory.new()
    factory.set_launch("(udpsrc name=pay0 port="+str(rtsp_port_num)+" buffer-size=524288 \
                        caps=\"application/x-rtp, media=video, clock-rate=90000, \
                        encoding-name=(string)H264, payload=96 \")")

    factory.set_shared(True)
    server.get_mount_points().add_factory("/test", factory)
 
    print("\n *** Launched RTSP Streaming at rtsp://"+ip+":%d/test ***\n\n" % rtsp_port_num)    
    
    while True :
        cap = cv2.VideoCapture(video_source)
    
        while True:
            ret, mat = cap.read()
            if not ret:
                print("end of video")
                break
            out_send.write(mat)
            cv2.waitKey(30) 
        
if __name__ == '__main__':
    main()