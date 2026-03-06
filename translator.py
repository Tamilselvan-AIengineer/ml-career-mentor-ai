"""
translator.py — Multi-language support for the EduAI platform.
Wraps a translation API (Google Translate / LibreTranslate / LLM-based).
"""
from dataclasses import dataclass

SUPPORTED_LANGUAGES = {
    "en": "English",
    "ta": "Tamil",
    "hi": "Hindi",
    "fr": "French",
    "de": "German",
    "es": "Spanish",
    "zh": "Chinese (Simplified)",
    "ar": "Arabic",
    "pt": "Portuguese",
    "ja": "Japanese",
}


@dataclass
class TranslationResult:
    original: str
    translated: str
    source_lang: str
    target_lang: str
    confidence: float = 1.0


class Translator:
    """
    Translation wrapper.
    Replace `_call_api` with your preferred provider:
      - Google Cloud Translation
      - DeepL
      - LibreTranslate (self-hosted)
      - LLM prompt-based translation
    """

    def __init__(self, provider: str = "mock", api_key: str = ""):
        self.provider = provider
        self.api_key = api_key

    def translate(self, text: str, target_lang: str, source_lang: str = "auto") -> TranslationResult:
        translated = self._call_api(text, target_lang, source_lang)
        return TranslationResult(
            original=text,
            translated=translated,
            source_lang=source_lang,
            target_lang=target_lang,
        )

    def _call_api(self, text: str, target_lang: str, source_lang: str) -> str:
        """Replace this with a real API call."""
        if self.provider == "mock":
            lang_name = SUPPORTED_LANGUAGES.get(target_lang, target_lang)
            return f"[{lang_name} translation of: {text[:80]}{'...' if len(text)>80 else ''}]"

        # Example: Google Translate
        # from google.cloud import translate_v2 as google_translate
        # client = google_translate.Client()
        # result = client.translate(text, target_language=target_lang)
        # return result["translatedText"]

        raise NotImplementedError(f"Provider '{self.provider}' not configured.")

    def batch_translate(self, texts: list[str], target_lang: str) -> list[TranslationResult]:
        return [self.translate(t, target_lang) for t in texts]

    @staticmethod
    def supported_languages() -> dict[str, str]:
        return SUPPORTED_LANGUAGES
