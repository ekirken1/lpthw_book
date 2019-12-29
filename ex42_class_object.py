# class is-a object
## animal is-a object (yes, sort of confusing). look at the extra credit.
class animal(object):
    pass

## dog is-a animal
class dog(animal):
    
    def __init__(self, name):
        ## dog has-a name
        self.name = name

## cat is-a animal
class cat(animal):

    def __init__(self, name):
        ## cat has-a name
        self.name = name

## person is-a object
class person(object):

    def __init__(self, name):
        ## person has-a name
        self.name = name

    ## person has-a pet (of some kind)
    self.pet = None

## employee is-a person
class employee(person):

    def __init__(self, name, salary):
        ## employee has-a name
        super(employee, self).__init__(name)
        ## employee has-a salary
        self.salary = salary 

## fish is-a object
class fish(object):
    pass

## salmon is-a fish
class salmon(fish):
    pass

## halibut is-a fish
class halibut(fish):
    pass

## object is-a class
## rover is-a dog 
rover = dog("Rover")

## satan is-a cat
satan = cat("Satan")

## mary is-a person
mary = person("Mary")

## mary has-a satan is-a cat
## mary has-a cat named Satan
## mary is-a person who has-a pet satan is-a cat
mary.pet = satan

## frank is-a employee who has-a 120000 salary
frank = employee("Frank", 120000)

## flipper is-a fish
flipper = fish()

## crouse is-a salmon is-a fish
crouse = salmon()

## object is-a class is-a class
## harry is-a halibut is-a fish
harry = halibut()