from simple_color import Color

color =  Color(ignore=True)
damage = 4
color_healthbar = ''
HEALTH = 10 - damage

if HEALTH <=3: color_healthbar = 'red'
elif HEALTH >=7 : color_healthbar = 'green'
else: color_healthbar = 'yellow'
print(color.paint(f'_{".+"*HEALTH}._', color_healthbar, 'black') + '')