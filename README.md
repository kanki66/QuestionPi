# QuestionPi
Connect to the server, ask your question, the host can read the questions

python -m pip install fastapi uvicorn[standard]

type to enter virtuell enviroment:
$ env\Scripts\activate

to exit:
$ deactivate

to fire up server:
$ uvicorn main:app --reload

connect with SQL:
https://www.fastapitutorial.com/blog/database-connection-fastapi/

usefull tut: https://kinsta.com/de/blog/fastapi/

autorun shell script rpi: https://www.instructables.com/Raspberry-Pi-Launch-Python-script-on-startup/

country=US # Your 2-digit country code
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
network={
    ssid="YOUR_NETWORK_NAME"
    psk="YOUR_PASSWORD"
    key_mgmt=WPA-PSK
}