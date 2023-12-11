# OpenCV RTSP Streaming Sever
## Libraries Installation
    `
    $ sudo apt update
    $ sudo apt-get install libgstrtspserver-1.0-0 gstreamer1.0-rtsp
    `
    For gst-rtsp-server (and other GStreamer stuff) to be accessible in
    Python through gi.require_version(), it needs to be built with
    gobject-introspection enabled (libgstrtspserver-1.0-0 is already).
    Yet, we need to install the introspection typelib package:
    `
    $ sudo apt-get install libgirepository1.0-dev
    $ sudo apt-get install gobject-introspection gir1.2-gst-rtsp-server-1.0
    `
## Usage
    1. Open stream_server.py file.
    2. Change `ip` with your dest IP address to stream. 
    3. Change `rtsp_port_num` with your RTSP port. 
    4. Change `video_source` with your video source (file, camera).
    5. `python stream_server.py`