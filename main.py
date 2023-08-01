import mbuild, mbot2
while True:
    state = mbuild.quad_rgb_sensor.get_offset_track(index = 1)
    if state >= -20 and state <= 20:
        mbot2.forward(200)
    else:
        mbot2.turn(-state/2.5)
