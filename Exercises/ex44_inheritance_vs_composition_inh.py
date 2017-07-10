""" Object oriented design - inheritance & composition concepts
"Most of the uses of inheritance can be simplified or replaced with composition, and multiple inheritance should be avoided at all costs."

Implicit inheritance:"""
class Parent(object):
	def implicit(self):
		print "PARENT implicit()"
		
class Child(Parent):
		pass # denotes an empty block of code
		
dad = Parent()
son = Child()

dad.implicit()
son.implicit()

# Override inheritance:
class Parent(object):
	def override(self):
		print "PARENT override()"
		
class Child(Parent):
	def override(self):
		print "CHILD override()"
		
dad = Parent()
son = Child()

dad.override()
son.override()

# Override alteration inheritance:
class Parent(object):
	def altered(self):
		print "PARENT altered()"
		
class Child(Parent):
	def altered(self):	
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered() # "call super with arguments Child and self, then call the function altered on whatever it returns"
		print "CHILD, AFTER PARENT altered()"
		
dad = Parent()
son = Child()

dad.altered()
son.altered()