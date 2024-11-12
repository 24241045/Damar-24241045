def fahrenheit_ke_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

    # input suru dari pengguna
    f = float(input("masukkan suhu dalam fahrenheit"))
    celsius = fahrenheit_ke_celcius(f)

    print(f"suhu {f}f setara dengan {celsius:.2f}C")