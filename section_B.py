# No 2(i)

student_name = str(input ("Enter the student's name   :"))
student_number = str(input ("Enter the student's number  :"))
programming = int(input ("Enter Programming  marks  :"))
data_science = int(input ("Enter Data science marks  :"))
computer_applications = int(input ("Enter computer applications marks  :"))
average_mark = (programming + data_science + computer_applications)/3

print (f"the Average mark is {average_mark :.3f}" )


# # No 2(ii)

# milesDriven = int (input ("Enter the number of miles driven  :"))
# gallonsOfGasUsed = float (input ("Enter the number of gallons used  :"))
# MPG =(milesDriven/gallonsOfGasUsed) 
# print (f"cars miles-per-gallons used is {MPG}")


#No 2 (iii)
def odd_numbers():
    for num in range(1,101):
        if num % 2!=0:
            print(num)
odd_numbers()



