from rdkit import Chem
from rdkit.Chem import Descriptors, Lipinski, Crippen, rdMolDescriptors, Draw


mol = Chem.MolFromSmiles("CC(=O)Oc1ccccc1C(=O)O")  # Aspirin


properties = {
    "MW": Descriptors.MolWt(mol), #molar weight of the molecule
    "LogP": Crippen.MolLogP(mol), # LogP, Lipophility of the molecule
    "TPSA": rdMolDescriptors.CalcTPSA(mol), # polar surface area
    "HBD": Lipinski.NumHDonors(mol), # Hydrogen bond donor, tendancy of a molecule to give away its hydrogen
    "HBA": Lipinski.NumHAcceptors(mol),# Hydrogen bond acceptor, tendancy of a molecule to accept an hydrogen
    "RotB": Lipinski.NumRotatableBonds(mol), # flexibility of the molecule
}

for s,props in properties.items():
    print(f"{s}:{props}")

# img=Draw.MolToImage(mol)
# img.save('aspirin.png')
