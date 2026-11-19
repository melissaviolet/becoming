from lesson_11 import city_country

def test_city_country():
    c_c = city_country("paris", "france")
    assert c_c == "Paris, France"

def test_city_country_population():
    c_c_p = city_country("berlin", "germany", 5000000)
    assert c_c_p == "Berlin, Germany - Population 5000000"