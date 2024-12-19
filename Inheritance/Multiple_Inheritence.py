class A:
    def sum(self):
        print("hello")

class B:
    def ok(self):
        print("Done")

class C(B,A):
    def d(self):
        print("Ok")

obj=C()
obj.sum()
obj.ok()
obj.d()

'''
hello
Done
Ok
'''