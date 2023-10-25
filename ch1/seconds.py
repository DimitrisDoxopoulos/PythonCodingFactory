# day - time counter

# giving seconds
total_seconds = 105310

# calculating the number of days
days = total_seconds // (24 * 60 * 60)

# calculating the remaining seconds
remaining_seconds = total_seconds - (days * 24 * 60 *60)

#number of hours
hours = remaining_seconds // (60 * 60)

# Calculating the remaining seconds again
remaining_seconds = remaining_seconds - (hours * 60 *60)

# calculating the minutes
minutes = remaining_seconds // 60

# Once more with feeling
remaining_seconds = remaining_seconds - (minutes * 60)

# Et Voila!
print(f"{total_seconds} seconds is {days} days, {hours} hours and {remaining_seconds} seconds")
