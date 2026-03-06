from transformers import MarianMTModel, MarianTokenizer


class Translator:

    def __init__(self):

        model_name = "Helsinki-NLP/opus-mt-mul-en"

        self.tokenizer = MarianTokenizer.from_pretrained(model_name)
        self.model = MarianMTModel.from_pretrained(model_name)

    def translate_to_english(self, text):

        inputs = self.tokenizer(text, return_tensors="pt", padding=True)

        translated = self.model.generate(**inputs)

        output = self.tokenizer.decode(
            translated[0],
            skip_special_tokens=True
        )

        return output
