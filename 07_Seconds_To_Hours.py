# Problem : Convert a number of seconds into hours, minutes and seconds.


Input_Seconds = int(input("Enter : "))

Hours = (Input_Seconds//3600)

# remaining_sec indicates seconds which are left after deducting hrs.
remaining_sec = (Input_Seconds % 3600)  

Minutes = (remaining_sec//60)

Seconds = (remaining_sec % 60)

print(f"{Hours} hour(s), {Minutes} minute(s), {Seconds} second(s)")


