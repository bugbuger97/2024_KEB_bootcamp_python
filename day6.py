# def desc():
#     def w():
#         print("w")
#     print("a")
#     return w
#
# desc() # a -> w()는 출력 되지 않음.

def desc(f):
    def study():
        print("study")
        f()
    return study
@desc
def something():
    print("do something~")

# anything = desc(something)
# anything()

something()