from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import Descriptors,Crippen,rdMolDescriptors
from rdkit.Chem import PandasTools
import seaborn as sb
import requests

molecule='OC1=CC=CC=C1'
m=Chem.MolFromSmiles(molecule)
mw=rdMolDescriptors.CalcNumRings(m)
rotatable_bonds=rdMolDescriptors.CalcNumRotatableBonds(m)
number_of_atm=rdMolDescriptors.CalcNumAtoms(m)
# img = Draw.MolToImage(m)
# img.save("output.png")
url = "https://raw.githubusercontent.com/PatWalters/practical_cheminformatics_tutorials/main/data/example_compounds.sdf"
r = requests.get(url)
bytes_written = open('example_compounds.sdf', 'w').write(r.text)

mols=[mol for mol in Chem.SDMolSupplier('example_compounds.sdf')]
img=Draw.MolsToGridImage(mols,molsPerRow=4)
img.save('grid_mols.png')
df=PandasTools.LoadSDF('example_compounds.sdf')

df['MW'] = [Descriptors.MolWt(x) for x in df.ROMol]
df['LogP'] = [Crippen.MolLogP(x) for x in df.ROMol]

ax=sb.boxplot(x=df.MW)

# mols2grid.display(mols) 
# print(img2)
# display=open('display.html','wb').write(img2)
print(ax)
# print(mols)
print(rotatable_bonds)
print(number_of_atm)
