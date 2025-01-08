from pi_controller import ProController, Key

pro = ProController(4)

@pro.on_key_press
def press(button: Key):
    print(button)
@pro.on_v_key_press("HOME")
def stop():
    pro.stop()


pro.run()