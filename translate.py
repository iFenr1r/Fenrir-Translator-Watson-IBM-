def tradutor(texto,origem,final):
        import json
        from watson_developer_cloud import LanguageTranslatorV2 as LanguageTranslator
        language_translator = LanguageTranslator(
	username='f5eecea1-3055-419e-96a5-e3732b9183c3',
	password='y2JSGI4u47l8')

        translation = language_translator.translate(
            text=texto,
            source=origem,
            target=final)

        traduzido = json.dumps(translation, indent=2, ensure_ascii=False)
        return traduzido
