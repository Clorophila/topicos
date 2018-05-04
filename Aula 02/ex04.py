#Soneto LVI - Shakespeare:
soneto = [
"Sweet love, renew thy force; be it not said\n",
"Thy edge should blunter be than appetite,\n",
"Which but to-day by feeding is allay'd,\n",
"To-morrow sharpen'd in his former might:\n",
"So, love, be thou; although to-day thou fill\n",
"Thy hungry eyes even till they wink with fullness,\n",
"To-morrow see again, and do not kill\n",
"The spirit of love with a perpetual dullness.\n",
"Let this sad interim like the ocean be\n",
"Which parts the shore, where two contracted new\n",
"Come daily to the banks, that, when they see\n",
"Return of love, more blest may be the view;\n",
"    Else call it winter, which being full of care\n",
"    Makes summer's welcome thrice more wish'd, more rare.\n",
]

import locale
import os
locale.setlocale(locale.LC_ALL,"")

#os.system('cls')

f = open("soneto.txt","w")
f.writelines(soneto)
f.close()

#-------------------------------------
f = open("soneto.txt","r")
c = open("copia_soneto.txt","w+")
c.writelines(f.read())

f.seek(0)
c.seek(0)

arquivo = f.read()
copia = c.read()
print(arquivo)
print(copia)

f.close()
c.close()