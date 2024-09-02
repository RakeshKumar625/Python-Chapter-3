letter = ''' Dear <|name|>,
you are selected ! 
<|Date|> '''

print(letter.replace("<|name|>","Rakesh").replace("<|Date|>","23 december 2024"))