def set_lang(lang):
    global load_img, settings
    if lang == "EN":
        load_img = "Load image"
        settings = "Settings"
    elif lang == "ES":
        load_img = "Cargar imagen"
        settings = "Ajustes"