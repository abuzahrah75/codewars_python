def make_readable(seconds):
    return_string = str(seconds//(60*60)).zfill(2) + ":"
    for_min = seconds % (60*60)
    return_string = return_string + str(for_min//60).zfill(2) + ":"
    for_sec = for_min % 60
    return_string = return_string + str(for_sec).zfill(2)
    return return_string


# from best result:
# return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)
print(make_readable(0))
print(make_readable(5))
print(make_readable(60))
print(make_readable(86399))
print(make_readable(359999))
