def make_car(model_name, manufacturer, **car_info):
    res = {}
    res["manufacturer"] = manufacturer
    res['model'] = model_name
    for key, value in car_info.items():
        res[f"{key}"] = value
    return res 

print(make_car('Offroader', 'Subaru', color = 'blue'))