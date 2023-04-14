class Store :
    def __init__(self, name):
        self.name = name
        self.product_list = []
    
    def add_product(self, new_product) :
        self.product_list.append(new_product)
        return self

    def sell_product(self, id) :
        for index, product in enumerate(self.product_list) :
            if product.id == id :
                print("This Product is SOLD :-----------------------------------------------")
                product.print_info()
                print("---------------------------------------------------------------------")
                self.product_list.pop(index)
        return self

    def show_all_products(self):
        for product in self.product_list:
            product.print_info()

    def inflation(self, percent_increase):
        for product in self.product_list:
            product.update_price(percent_increase, True)
        return self
    
    def set_clearance(self, category, percent_discount) :
        for product in self.product_list :
            if product.category == category :
                product.update_price(percent_discount, False)