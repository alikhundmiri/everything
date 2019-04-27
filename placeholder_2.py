import enchant
d = enchant.Dict("en_US")
print(d.check("idoob"))
print(d.check("falls"))
print(d.suggest("idoob"))
