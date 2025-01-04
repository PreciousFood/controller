from controller import ProController

pro = ProController(0, min_pause_time=5)

@pro.on_every_loop
def m():
    print(bool(pro.x))

@pro.on_v_key_press("CAPTURE")
def stop():
    pro.stop()

pro.run()