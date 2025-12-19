# chai = "Ginger Chai"

# def prepare_chai(order):
#     print(f"Preparing {order}...")
#     print(f"{order} is ready!")
    

# prepare_chai(chai)
# print(chai)

chai = [1, 2, 3]

def edit_chai(cup):
    cup[1] = 42
    print("Inside function:", cup)
    
edit_chai(chai)
print(chai)


def make_chai(tea, milk, sugar):
    print(f"Making chai with {tea}, {milk}, and {sugar}")
    
    
make_chai("Green Tea", "Almond Milk", "Honey")
make_chai(tea="Black Tea", sugar="Sugar", milk="Whole Milk")

def special_chai(*ingredients, **extras):
    print("Ingredients:", ingredients)
    print("Extras:", extras)
    
special_chai("Black Tea", "Cardamom", milk="Oat Milk", sugar="Brown Sugar")


def chai_order(order=[]): # Caution: mutable default argument
    order.append("Masala")
    print("Current order:", order)
    
chai_order()
chai_order()