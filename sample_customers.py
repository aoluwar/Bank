import random

first_names = [
    "Chinedu", "Aisha", "Emeka", "Ngozi", "Ifeanyi", "Kemi", "Sani", "Funke", "Yusuf", "Bola",
    "Chinasa", "Gbenga", "Fatima", "Obinna", "Olamide", "Blessing", "Josephine", "Seun", "Mustapha", "Uche",
    "Olumide", "Adanna", "Ibrahim", "Temitope", "Chisom", "Hauwa", "Ijeoma", "Samuel", "Adaeze", "Farouk",
    "Ireti", "Kolade", "Nnamdi", "Halima", "Ebuka", "Bukola", "Abiola", "Opeyemi", "Kunle", "Precious"
]

last_names = [
    "Okafor", "Bello", "Eze", "Nwosu", "Ubah", "Adeyemi", "Musa", "Ogunleye", "Abdullahi", "Tinubu",
    "Amadi", "Awolowo", "Ibrahim", "Kalu", "Ajayi", "Agbaje", "Okon", "Ojo", "Dantata", "Iwobi",
    "Ojo", "Adetayo", "Mohammed", "Afolabi", "Uzodinma", "Yahaya", "Obi", "Balogun", "Mohammed", "Okoye",
    "Oseni", "Ahmed", "Jide", "Garba", "Ezekwesili", "Ogunbiyi", "Enenche", "Oshodi", "Makanjuola", "Oduye"
]

def random_phone():
    return "0{}{}{}".format(
        random.choice([7,8,9]),
        random.randint(0,9),
        str(random.randint(10000000,99999999))
    )

nigerian_customers = []
for i in range(1000):
    fn = random.choice(first_names)
    ln = random.choice(last_names)
    name = f"{fn} {ln}"
    email = f"{fn.lower()}.{ln.lower()}{i}@example.com"
    phone = random_phone()
    nigerian_customers.append({
        "name": name,
        "email": email,
        "phone": phone
    })