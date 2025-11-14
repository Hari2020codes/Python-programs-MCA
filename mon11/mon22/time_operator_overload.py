class Time:
    def __init__(self, hr, min, sec):
        self.hr = hr
        self.min = min
        self.sec = sec

    def __add__(self, other):
        sec = self.sec + other.sec
        min = self.min + other.min
        hr = self.hr + other.hr

        # handle seconds
        if sec >= 60:
            sec -= 60
            min += 1

        # handle minutes
        if min >= 60:
            min -= 60
            hr += 1

        # handle hours (12-hour format)
        if hr > 12:
            hr -= 12

        return Time(hr, min, sec)

    def __str__(self):
        return f"{self.hr:02d}:{self.min:02d}:{self.sec:02d}"


# Test
n1 = Time(1, 2, 3)
n2 = Time(3, 4, 5)

n3 = n1 + n2

print(n3)

# class Time:
#     def __init__(self,hr,min, sec):
#         self.hr=hr
#         self.min=min
#         self.sec=sec
#     def __add__(self,other):
#         hr3=self.hr+other.hr
#         if hr3>12:
#             hr3=1    
#     #        
#         min3=self.min+other.min
#         if min3>60:
#             min3=1
#             hr3=hr3+1
#             if hr3>12:
#              hr3=1
#      #
#         sec3=self.sec+other.sec
#         if sec3>60:
#             sec3=1
#             min3=min3+1
#             if min3>60:
#                 min3=1
#                 hr3=hr3+1
#                 if hr3>12:
#                     hr3=1
# n1=Time(1,2,3)         
# n2=Time(3,4,5)            
# n3=n1+n2
# print(n3)
            
            