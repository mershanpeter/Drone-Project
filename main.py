import socket
import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.garden.joystick import Joystick   # use packaged garden joystick

# ---------- UDP Client ----------
class DroneUDPClient:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_ip = None
        self.server_port = None

    def connect(self, ip, port):
        self.server_ip = ip
        self.server_port = int(port)

    def is_connected(self):
        return bool(self.server_ip and self.server_port)

    def send(self, msg):
        if self.is_connected():
            try:
                self.sock.sendto(msg.encode(), (self.server_ip, self.server_port))
            except Exception as e:
                print("UDP send error:", e)

# ---------- Styled Button ----------
class StyledButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (0.2, 0.6, 0.9, 1)
        self.color = (1,1,1,1)
        self.font_size = '18sp'
        self.bold = True
        self.size_hint_y = None
        self.height = 50

# ---------- Main App ----------
class DroneApp(App):
    JOYSTICK_INTERVAL = 0.08  # send interval

    def build(self):
        self.udp_client = DroneUDPClient()
        self.last_send = 0
        root = BoxLayout(orientation='vertical', padding=12, spacing=12)

        # Top: IP & Port
        top = GridLayout(cols=3, size_hint_y=None, height='50dp', spacing=8)
        self.ip_input = TextInput(text='192.168.4.1', multiline=False)
        self.port_input = TextInput(text='4210', multiline=False)
        self.connect_btn = StyledButton(text='Connect')
        self.connect_btn.bind(on_press=self.on_connect)
        top.add_widget(self.ip_input)
        top.add_widget(self.port_input)
        top.add_widget(self.connect_btn)
        root.add_widget(top)

        # Status label
        self.status = Label(text='Not connected', size_hint_y=None, height='30dp', color=(0,1,0,1))
        root.add_widget(self.status)

        # Joysticks
        joy_row = BoxLayout(orientation='horizontal', spacing=12, size_hint=(1,0.6))
        self.joy_left = Joystick(size_hint=(0.5,1))
        self.joy_left.bind(pad=self.on_left_joystick)
        self.joy_right = Joystick(size_hint=(0.5,1))
        self.joy_right.bind(pad=self.on_right_joystick)
        joy_row.add_widget(self.joy_left)
        joy_row.add_widget(self.joy_right)
        root.add_widget(joy_row)

        # Control buttons
        btn_row = GridLayout(cols=3, size_hint_y=None, height='60dp', spacing=10)
        btn_takeoff = StyledButton(text='🚀 Takeoff')
        btn_takeoff.bind(on_press=lambda x: self.send_cmd("CMD|START"))
        btn_land = StyledButton(text='🛬 Land')
        btn_land.bind(on_press=lambda x: self.send_cmd("CMD|LAND"))
        btn_emergency = StyledButton(text='❌ EMERGENCY')
        btn_emergency.background_color = (1,0.1,0.1,1)
        btn_emergency.bind(on_press=lambda x: self.send_cmd("CMD|EMERGENCY"))
        btn_row.add_widget(btn_takeoff)
        btn_row.add_widget(btn_land)
        btn_row.add_widget(btn_emergency)
        root.add_widget(btn_row)

        Clock.schedule_interval(self.send_heartbeat, 2.0)
        return root

    def on_connect(self, instance):
        ip = self.ip_input.text.strip()
        port = self.port_input.text.strip()
        if ip and port.isdigit():
            self.udp_client.connect(ip, int(port))
            self.status.text = f"✅ Connected to {ip}:{port}"

    def send_cmd(self, cmd):
        self.udp_client.send(cmd)
        self.status.text = f"Sent: {cmd}"

    def send_heartbeat(self, dt):
        if self.udp_client.is_connected():
            self.udp_client.send("PING")

    def on_left_joystick(self, instance, pad):
        x, y = pad
        now = time.time()
        if now - self.last_send < self.JOYSTICK_INTERVAL: return
        self.last_send = now
        # Throttle
        if abs(y) > 0.1:
            thr = int((y+1)*500+1000)  # Map from -1..1 to 1000..2000
            self.send_cmd(f"THR|{thr}")
        # Yaw
        if abs(x) > 0.1:
            yaw = int(x*400)  # -400..400
            self.send_cmd(f"YAW|{yaw}")

    def on_right_joystick(self, instance, pad):
        x, y = pad
        now = time.time()
        if now - self.last_send < self.JOYSTICK_INTERVAL: return
        self.last_send = now
        # Pitch
        if abs(y) > 0.1:
            pitch = round(y*45,1)
            self.send_cmd(f"PIT|{pitch}")
        # Roll
        if abs(x) > 0.1:
            roll = round(x*45,1)
            self.send_cmd(f"ROL|{roll}")

if __name__ == "__main__":
    Window.clearcolor = (0.05,0.05,0.05,1)
    Window.size = (700,760)
    DroneApp().run()
