import re

WeekdayMap = [("Seg", "Segunda"), ("Ter", "Terça"), ("Qua", "Quarta"), ("Qui", "Quinta"), ("Sex", "Sexta"), ("Sab", "Sábado")]

def extrair_lat_long(string):
    # Padrao da expressao regular para encontrar os valores de latitude e longitude
    padrao = r"LatLng\(lat:\s*([-+]?\d+\.\d+),\s*lng:\s*([-+]?\d+\.\d+)\)"
    
    # Procurar o padrao na string fornecida
    match = re.search(padrao, string)
    
    if match:
        # Se encontrou, extrai os valores de latitude e longitude
        latitude = float(match.group(1))
        longitude = float(match.group(2))
        return latitude, longitude
    else:
        # Se nao encontrou, retorna None para indicar que os valores nao foram encontrados
        return None