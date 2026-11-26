from vpython import (
    color,
    canvas,
    vector,
    sphere,
    cylinder,
    slider,
    wtext,
    rate,
    cos,
    sin,
)

scene = canvas(title="Circular Motion Simulation", wideltaTh=800, height=450)

center = vector(0, 0, 0)
sphere(pos=center, radius=0.35, color=color.gray(0.6))

ball = sphere(
    pos=vector(5, 0, 0),
    radius=0.6,
    color=color.cyan,
    make_trail=True,
)
arm = cylinder(
    pos=center,
    axis=ball.pos - center,
    radius=0.07,
    color=color.yellow,
)

deltaT = 0.01
angle = 0.0

radius_slider = slider(min=1, max=10, value=5.0, bind=lambda s: reset())
radius_text = wtext(text=" Radius r: 5.0 m\n")

angular_speed_slider = slider(min=0.5, max=6.0, value=2.0, bind=lambda s: reset())
angular_speed_text = wtext(text=" Angular Speed w: 2.0 rad/s\n")

tangential_velocity_text = wtext(text="")
centripetal_acceleration_text = wtext(text="")

def reset():
    global angle
    radius_text.text = f" Radius r: {radius_slider.value:.1f} m\n"
    angular_speed_text.text = f" Angular Speed w: {angular_speed_slider.value:.1f} rad/s\n"

    tangential_velocity = angular_speed_slider.value * radius_slider.value
    tangential_velocity_text.text = f" Tangential Velocity v: {tangential_velocity:.2f} m/s\n"

    centripetal_acceleration = (tangential_velocity ** 2) / radius_slider.value
    centripetal_acceleration_text.text = f"Centripetal Acceleration a: {centripetal_acceleration:.2f} m/s2"

    angle = 0.0
    r = radius_slider.value
    ball.clear_trail()
    ball.pos = vector(r * cos(angle), r * sin(angle), 0)
    arm.axis = ball.pos - center


reset()

while True:
    rate(100)
    angle += angular_speed_slider.value * deltaT
    r = radius_slider.value
    ball.pos = vector(r * cos(angle), r * sin(angle), 0)
    arm.axis = ball.pos - center