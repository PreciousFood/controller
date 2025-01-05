from controller import ProController

pro = ProController(0, min_pause_time=5)

@pro.on_every_loop
def m():
    pass

@pro.on_v_key_press("CAPTURE")
def stop():
    pro.stop()

@pro.on_v_key_press("A")
def rumble():
    pro.rumble(100, 0xffff, 0x0000)

pro.run()