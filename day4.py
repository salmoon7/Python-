#dictionaries in JavaScript
#declare a company dictionary

company={
    "a":"Madison group",
    "b":"Patemine Hdc"
}
print(type(company))
print(company)
print(company['a'])
print(company.get('a'))


#Looping over a dictionary

for key in company:
    print(f"{key}     ->     {company[key]}")
    
