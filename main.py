class BaseContact:
    def __init__(self, imie, nazwisko, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email

    def __str__(self):
        return f"Imie: {self.imie} Nazwisko: {self.nazwisko} Email: {self.email}"
    

    @property
    def label_length(self):
        return f"{len(self.imie)} {len(self.nazwisko)}"
    
    def contact(self):
        if isinstance(self, BaseConBusinessContacttact):
            print(f"Wybieram numer służbowy {self.telefon_sluzbowy} i dzwonię do {self.imie} {self.nazwisko}")
        else:
            print(f"Wybieram numer {self.telefon} i dzwonię do {self.imie} {self.nazwisko}")



class BaseConBusinessContacttact(BaseContact):
    
    def __init__(self, stanowisko, firma, telefon_sluzbowy, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.stanowisko = stanowisko
       self.firma = firma
       self.telefon_sluzbowy = telefon_sluzbowy

    def __str__(self):
        return f"Imie: {self.imie} Nazwisko: {self.nazwisko} Email: {self.email}  Telefon Prywatny: {self.telefon}  Firma: {self.firma}  Stanowisko: {self.stanowisko} Telefon sluzbowy: {self.telefon_sluzbowy}"

def create_contacts(typ, ilosc):
    from faker import Faker
    fake = Faker()

    if typ == "Base":
        for i in range(0, ilosc):
            business_card = BaseContact(imie=fake.first_name(), nazwisko=fake.last_name(), telefon=fake.phone_number(), email=fake.email())
            business_card.contact()

    elif typ == "Business":
        for i in range(0, ilosc):
             business_card = BaseConBusinessContacttact(imie=fake.first_name(), nazwisko=fake.last_name(), telefon=fake.phone_number(), email=fake.email(), firma=fake.company(), telefon_sluzbowy=fake.phone_number(), stanowisko=fake.job())
             business_card.contact()
    else:
        print("Zły typ wizytówki, do wyboru 'Base', 'Business' ")


create_contacts("Business", 10)