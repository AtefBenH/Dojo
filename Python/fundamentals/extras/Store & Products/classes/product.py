class Product:
    count = 0
    def __init__(self, name, category, price) :
        self.id = Product.count
        Product.count+=1
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased) :
        if is_increased == True :
            self.price += self.price*percent_change
        else:
            self.price -= self.price*percent_change
    
    def print_info(self):
        print(f"Product id : {self.id} Product name : {self.name} | Category : {self.category} | Price : {self.price}")
    
