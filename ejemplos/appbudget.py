

class Category:
    def __init__(self,name):
        self.name = name
        self.lista = []

    def deposit(self,amount,description=None):#añadir dinero
        if description == None:
            self.lista.append({'amount':amount,'description':''})
        else:
            self.lista.append({'amount':amount,'description':description})

    def withdraw(self,amount,description=None):#retirar dinero
        if self.check_funds(amount):

            if description == None:
                self.lista.append({'amount':-amount,'description':''})
            else:
                self.lista.append({'amount':-amount,'description':description})
            return True
        else:
            return False

    def transfer(self,amount,budget_category):#transferir cantidad entre categoría
        if self.check_funds(amount):#comprueba si hay dinero
            self.lista.append({'amount':-(amount),'description':f'Transfer to {budget_category.name}'})
            budget_category.deposit(amount,description=f'Transfer from {self.name}')
            return True
        else:
            return False

    def get_balance(self):#total del dinero de la lista
        balance = 0
        for items in self.lista:
            balance += items['amount']
        return balance



    def check_funds(self,amount):#cantidad es menor que el dinero depositado
        return amount<= self.get_balance()

    def __str__(self):
        name = self.name
        s = name.center(30,"*")
        for items in self.lista:
            try:
                left = items['description'][0:23]
            except TypeError:
                left =''
            right = str("{:.2f}".format(items['amount']))
            #Left aligns the result (within the available space) |  #Right aligns the result (within the available space)
            s += f"\n{left:<23}{'€ '+ right:>7} "
        s+= f"\nTotal {name}: €"+ str(self.get_balance())
        return s

def create_spend_chart(categories):
    cadena=''
    #porcetanjes por categoria

    dict_porcentaje = {}
    for ca in categories:
        total=0

        for i in ca.lista:
            if i['amount'] < 0:
                total += abs(i['amount'])

        dict_porcentaje[ca.name] = round(total,2)
    totaldepositos = sum(dict_porcentaje.values())
    porcetanjes_dict ={}
    for k in dict_porcentaje.keys():
        porcetanjes_dict[k]= int(round(dict_porcentaje[k]/totaldepositos,2)*100)
    cadena += 'Percentage spent by categories\n'

    for i in range(100,-10,-10):

        cadena +=f'{i}'.rjust(3)+'|'
        for porcentaje in porcetanjes_dict.values():
            if porcentaje>i:
                cadena += 'o '
            else:
                cadena += '  '
        cadena +='\n'
    cadena += ' '*4+'-'*(len(porcetanjes_dict.values())*3+1)
    cadena +='\n'

    dict_key_list = list(porcetanjes_dict.keys())#indice de categorias

    max_long = max([len(i) for i in dict_key_list])

    for i in range(max_long):
        cadena += ' '*4
        for name in dict_key_list:

            if len(name)>i:
                cadena +=name[i]+' '
            else:
                cadena +='  '
        if i<max_long-1:
            cadena +='\n'


    return cadena


#
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(25,'NY cap')
taxes = Category('Taxes')
taxes.deposit(250, 'deposit')
taxes.withdraw(150, 'deposit')
light = Category('Light')
light.deposit(100, 'deposit')
light.withdraw(30, 'deposit')
# print(food)
# print(clothing)
print('CHART'.center(50,'*'))

print(create_spend_chart([food,clothing,taxes,light]))


# https://www.w3schools.com/python/ref_string_format.asp