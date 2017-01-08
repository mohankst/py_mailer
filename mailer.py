recevers = {}

try:
    email_file = open('mailids.txt', 'r')
    for line in email_file:
        (email, name) = line.split(',')
        recevers[email] = name.strip()

except FileNotFoundError as err:
    print (str(err) + ". So create it")

print (recevers)