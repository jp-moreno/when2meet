import re

def validate(Time):
    Found_val = re.search("^[a-zA-Z0-9]+:\d\d:\d\d-\d\d:\d\d$", Time)
    if Found_val is None:
        return False
    get_Vals = Found_val.string.split(":", 1)
    times = get_Vals[1].split("-")
    for time in times:
        val = time.split(":")
        if (int(val[0]) > 24) or (int(val[0]) == 24 and int(val[1]) > 0) or (int(val[1]) > 60):
            return False
    return True


def calculateTime(times):
    Avail_time_by_per = {}
    for t in times:
        state = t.split(":", 1)
        if state[0] not in Avail_time_by_per:
            Avail_time_by_per[state[0]] = []
        Avail_time_by_per[state[0]].append(state[1])
    print(times)

    Available_Times = ["00:00-24:00"]
    for per in Avail_time_by_per:
        Time = Avail_time_by_per[per]
        new_times = []
        for time_slot in Time:
            ts = time_slot.split("-")
            for avail_time in Available_Times:
                at = avail_time.split("-")
                if (ts[1] < at[0] and ts[0] > at[1]):
                    break
                else:
                    new_times.append(max(ts[0], at[0]) + "-" + min(ts[1], at[1]))
        Available_Times = new_times
        
    return Available_Times
