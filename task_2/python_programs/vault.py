class Vault:
    def __init__(self, galleons=0, sickels=0, knuts=0):
        self.galleons=galleons
        self.sickels=sickels
        self.knuts=knuts
    
    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickels} Sickels, {self.knuts} Knuts"

    def __add__(self, other):
        galleons=self.galleons + other.galleons
        sickels=self.sickels + other.sickels
        knuts=self.sickels + other.knuts
        return Vault(galleons, sickels, l=knuts )

    
potter=Vault(100, 50, 30)
print(potter)

weasly=Vault(80, 50, 30)
print(weasly)

galleons=potter.galleons + weasly.galleons
sickels=potter.sickels + weasly.sickels
knuts=potter.sickels + weasly.knuts

# total=Vault(galleons, sickels, knuts)
total=potter+weasly
print(total)