texto = "Mi número de teléfono es 123-456-7890."
patron_telefono = r"(\d{3})-(\d{3})-(\d{4})"
resultado = re.search(patron_telefono, texto)

if resultado:
    print(f"Teléfono completo: {resultado.group(0)}")
    print(f"Código de área: {resultado.group(1)}")
    print(f"Prefijo: {resultado.group(2)}")
    print(f"Sufijo: {resultado.group(3)}")
