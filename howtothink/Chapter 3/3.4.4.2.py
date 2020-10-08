days_of_the_week=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
starting_day=int(input('What day is today?(0-6)'))
sleeptime=int(input('How many nights have you slept?'))
print('You will return on',days_of_the_week[(starting_day+sleeptime)%len(days_of_the_week)])

