calculate_grade=int(input("Enter a numeric grade from 0 to 100:"))
# Match-case
match calculate_grade:
 case calculate_grade if 90<= calculate_grade <=100:
   print("grade: A")
 case calculate_grade if 80<= calculate_grade <90:
   print("grade: B")
 case calculate_grade if 70<= calculate_grade <80:
   print("grade: C")
 case calculate_grade  if  60<= calculate_grade <70:
   print("grade: D")
 case calculate_grade if 0<= calculate_grade <60:
   print("grade: F")
 case _:
   print("Enter numerical grade from 0 to 100 only!")
