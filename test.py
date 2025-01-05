from evdev import ecodes, InputDevice, ff, list_devices
import time

# Find first EV_FF capable event device (that we have permissions to use).
pro = InputDevice(list_devices()[0])

rumble = ff.Rumble(strong_magnitude=0x0000, weak_magnitude=0xffff)
effect_type = ff.EffectType(ff_rumble_effect=rumble)
duration_ms = 1000

effect = ff.Effect(
    ecodes.FF_RUMBLE, -1, 0,
    ff.Trigger(0, 0),
    ff.Replay(duration_ms, 0),
    effect_type
)

repeat_count = 1
effect_id = pro.upload_effect(effect)
pro.write(ecodes.EV_FF, effect_id, repeat_count)
time.sleep(duration_ms / 1000)
time.sleep(2)
pro.write(ecodes.EV_FF, effect_id, 0)
time.sleep(5)
pro.erase_effect(effect_id)