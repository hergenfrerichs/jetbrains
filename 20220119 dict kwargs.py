iris = {}


def add_iris(id_n, species, petal_length, petal_width, **kwargs):
    iris.update({id_n: {'species': species, 'petal_length': petal_length, 'petal_width': petal_width}})
    for key, value in kwargs.items():
        iris[id_n][key] = value
    

add_iris(0, 'Iris versicolor', 4.0, 1.3, petal_hue='pale lilac')
#add_iris(0, 'Iris versicolor', 4.0, 1.3)
print(iris)

#def add_iris(id_n, species, petal_length, petal_width, **kwargs):
 #   for key, value in kwargs.items():
  #      to_be_added = {id_n: {'species': species, 'petal_length': petal_length, 'petal_width': petal_width, key: value}}
   #     iris.update(to_be_added)
