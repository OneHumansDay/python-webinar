import random;

#public List<string> GetDays() {}
def get_days():
    #List<string days = new List<string>()
    days = ['mon', 'tues', 'wed', 'thurs', 'fri', 'sat', 'sun']
    return days

def get_random_report():
    weather = ['sunny', 'lovely', 'cold']
    return weather[random.randint(0, len(weather) - 1)]

def main():
    days = get_days();

    for day in days:
        report = get_random_report()
        print("On {0} it will be {1}.".format(day, report))

main();