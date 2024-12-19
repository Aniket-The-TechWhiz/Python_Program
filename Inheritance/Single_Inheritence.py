class A:
    def sum(self):
        print("hello")

class B(A):
    def ok(self):
        print("Done")

obj=B()
obj.sum()
obj.ok()