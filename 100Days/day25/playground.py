# def binarysearch(arr, n, k):
#     h = n
#     l = 0


    # def bns(a, high, low, k):
    #     if high >= low:
    #         mid = (high + low) // 2
    #
    #         if a[mid] == k:
    #             return mid
    #         elif a[mid] > k:
    #             bns(a, mid - 1, low, k)
    #         else:
    #             bns(a, high, mid + 1, k)
    #     else:
    #         return -1

    # return (bns(arr, h, l, k))

# print(binarysearch(arr=[1,2,3,4,5], n=5, k=4))


# def add(*args):
#     print(args)
#     for i in args:
#         print(i)
#     print(type(args))
#
# # add(2,2,4)
#
#
# class Car:
#
#     def __init__(self, **kw):
#         self.make = kw["make"]
#         self.model = kw.get("model")
#
#
# my_car = Car(make="nissan")
#
# print(my_car.model)

x = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

s = "IIIV"
for i in s:
    print(x[i])
