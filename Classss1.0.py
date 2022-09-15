class Class1:
    def _init_(self):
        print('Конструктор базового класса')
    def func1(self):
        print('Метод func1() класса Class1')
	
class Class2(Class1):
    def _init_(self):
        print('Конструктор производного класса')
        Class1._init_(self)
    def func1(self):
        print('Метод func1() класса Class2')
        Class1.func1(self)
	        
c = Class2()
c._init_( )
c.func1()