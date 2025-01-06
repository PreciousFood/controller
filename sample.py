from controller import ProController

import evdev
print([evdev.InputDevice(a).name for a in evdev.list_devices()])
pro = ProController(4)

@pro.on_every_loop
def m():
    print(bool(pro.x))

@pro.on_v_key_press("CAPTURE")
def stop():
    pro.stop()

@pro.on_v_key_press("A")
def rumble():
    pro.rumble(100, 0xffff, 0x0000)

pro.run()