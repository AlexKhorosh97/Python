from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 15", "+79993897666"))
catalog.append(Smartphone("Samsung", "Galaxy", "+79378889999"))
catalog.append(Smartphone("Nokia", "3110", "+79585883663"))
catalog.append(Smartphone("Google", "Pixel 5", "+79456789012"))
catalog.append(Smartphone("Dexp", "9 Pro", "+7396580877"))

for phone in catalog:
    print(f"{phone.phone_brand} - {phone.model}. {phone.phone_number}")