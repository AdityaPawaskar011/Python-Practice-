class Product:
    products={}
    # addproduct=[]

    def addProduct (self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

        # Product.addproduct += [name,price]

        Product.products[name]={
            'price': price,
            'quantity':quantity
        }
        print(Product.products)
        

class Cart():
    your_cart={}
    def addproducttocart(self,name,quantity):
        print(prod.products.get(name).get('quantity'))
        if name in prod.products and quantity <= prod.products.get(name).get('quantity'):
            print(f"{name} is available")
            Cart.your_cart [name]={
            'price':quantity * prod.products.get(name).get('price'),
            'quantity':quantity
        }
        
            updated_qty  =prod.products.get(name).get('quantity') - quantity
            prod.products[name]['quantity'] = updated_qty

            if prod.products.get(name).get('quantity') == 0:
                del prod.products[name]

            
        
        else:
            print(f"{name} is not available")

    def calculate_total(self):
        print(f"Item's in your car: {c.your_cart} ")
        total_bill= sum(item['price'] for item in c.your_cart.values())
        print(f'The total Bill is {total_bill}')

prod=Product()

prod.addProduct('Tomato',30,10)

prod.addProduct('Apple',30,10)

c=Cart()
c.addproducttocart('Apple',10)
c.addproducttocart('Tomato',4)

# print(c.your_cart)
# print(prod.products)

c.calculate_total()
# print(prod.addproduct)



