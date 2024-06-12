# STABLE_TS = {
#     "myMemory": {"name": "MyMemory", "priority": 20},
#     "alibaba": {"name": "Alibaba", "priority": 10},
#     "baidu": {"name": "Baidu", "priority": 10},
#     "modernMt": {"name": "ModernMT", "priority": 20},
#     "iciba": {"name": "Iciba", "priority": 15},
#     "google": {"name": "Google", "priority": 4},
#     "bing": {"name": "Bing", "priority": 5},
#     "lingvanex": {"name": "Lingvanex", "priority": 20},
#     # "yandex": {"name": "Yandex", "priority": 20},
#     "itranslate": {"name": "Itranslate", "priority": 20},
#     "sysTran": {"name": "SysTran", "priority": 20},
#     "argos": {"name": "ArgoS", "priority": 20},
#     "reverso": {"name": "Reverso", "priority": 20},
#     "deepl": {"name": "DeepL", "priority": 5},
#     "cloudTranslation": {"name": "Cloud Translation", "priority": 10},
#     "qqTranSmart": {"name": "QQ Translate Smart", "priority": 5},
#     "translateCom": {"name": "Translate Com", "priority": 15},
#     "sogou": {"name": "Sogou", "priority": 13},
#     "qqFanyi": {"name": "QQ Fanyi", "priority": 10},
#     "papago": {"name": "Papago", "priority": 15},
#     "youdao": {"name": "Youdao", "priority": 15},
#     "iflyrec": {"name": "iFlyrec", "priority": 30},
#     "caiyun": {"name": "Caiyun", "priority": 15},
# }
STABLE_TS = [
    {"id":"myMemory", "name": "MyMemory", "priority": 20},
    {"id":"alibaba", "name": "Alibaba", "priority": 10},
    {"id":"baidu", "name": "Baidu", "priority": 10},
    {"id":"modernMt", "name": "ModernMT", "priority": 20},
    {"id":"iciba", "name": "Iciba", "priority": 15},
    {"id":"google", "name": "Google", "priority": 4},
    {"id":"bing", "name": "Bing", "priority": 5},
    {"id":"lingvanex", "name": "Lingvanex", "priority": 20},
    # {"id":"yandex", "name": "Yandex", "priority": 20},
    {"id":"itranslate", "name": "Itranslate", "priority": 20},
    {"id":"sysTran", "name": "SysTran", "priority": 20},
    {"id":"argos", "name": "ArgoS", "priority": 20},
    {"id":"reverso", "name": "Reverso", "priority": 20},
    {"id":"deepl", "name": "DeepL", "priority": 5},
    {"id":"cloudTranslation", "name": "Cloud Translation", "priority": 10},
    {"id":"qqTranSmart", "name": "QQ Translate Smart", "priority": 5},
    {"id":"translateCom", "name": "Translate Com", "priority": 15},
    {"id":"sogou", "name": "Sogou", "priority": 13},
    {"id":"qqFanyi", "name": "QQ Fanyi", "priority": 10},
    {"id":"papago", "name": "Papago", "priority": 15},
    {"id":"youdao", "name": "Youdao", "priority": 15},
    {"id":"iflyrec", "name": "iFlyrec", "priority": 30},
    {"id":"caiyun", "name": "Caiyun", "priority": 15},
]
SUPPORTED_LANGUAGES = [
    "English",
    "Chinese Simplified",
    "Chinese Traditional",
    "Russian",
    "Japanese",
    "Korean",
    "Czech",
    "Danish",
    "German",
    "Spanish",
    "French",
    "Indonesian",
    "Italian",
    "Hungarian",
    "Dutch",
    "Polish",
    "Portuguese",
    "Swedish",
    "Turkish",
]

LANG_MAP = {
    "myMemory": {
        "Czech": "cs-CZ",
        "Danish": "da-DK",
        "German": "de-DE",
        "English": "en-ZA",
        "Spanish": "es-US",
        "French": "fr-FR",
        "Hungarian": "hu-HU",
        "Indonesian": "id-ID",
        "Italian": "it-IT",
        "Japanese": "ja-JP",
        "Korean": "ko-KR",
        "Dutch": "nl-NL",
        "Polish": "pl-PL",
        "Portuguese": "pt-PT",
        "Russian": "ru-RU",
        "Swedish": "sv-SE",
        "Turkish": "tr-TR",
        "Chinese Simplified": "zh-CN",
        "Chinese Traditional": "zh-TW",
    },
    "alibaba": {
        "Czech": "cs",
        "Danish": "da",
        "German": "de",
        "English": "en",
        "Spanish": "es",
        "French": "fr",
        "Hungarian": "hu",
        "Indonesian": "id",
        "Italian": "it",
        "Japanese": "ja",
        "Korean": "ko",
        "Dutch": "nl",
        "Polish": "pl",
        "Portuguese": "pt",
        "Russian": "ru",
        "Swedish": "sv",
        "Turkish": "tr",
        "Chinese Simplified": "zh",
        "Chinese Traditional": "zh-tw",
    },
    "baidu": {
        "Czech": "cs",
        "German": "de",
        "English": "en",
        "Hungarian": "hu",
        "Indonesian": "id",
        "Italian": "it",
        "Dutch": "nl",
        "Polish": "pl",
        "Portuguese": "pt",
        "Russian": "ru",
        "Turkish": "tr",
        "Chinese Simplified": "zh",
    },
    "modernMt": {
        "Czech": "cs",
        "Danish": "da",
        "German": "de",
        "English": "en",
        "Spanish": "es-ES",
        "French": "fr",
        "Hungarian": "hu",
        "Indonesian": "id",
        "Italian": "it",
        "Japanese": "ja",
        "Korean": "ko",
        "Dutch": "nl",
        "Polish": "pl",
        "Portuguese": "pt-PT",
        "Russian": "ru",
        "Swedish": "sv",
        "Turkish": "tr",
        "Chinese Simplified": "zh-CN",
        "Chinese Traditional": "zh-TW",
    },
    "iciba": {
        "Czech": "cs",
        "Danish": "da",
        "German": "de",
        "English": "en",
        "Spanish": "es",
        "French": "fr",
        "Hungarian": "hu",
        "Indonesian": "id",
        "Italian": "it",
        "Japanese": "ja",
        "Korean": "ko",
        "Dutch": "nl",
        "Polish": "pl",
        "Portuguese": "pt",
        "Russian": "ru",
        "Swedish": "sv",
        "Turkish": "tr",
        "Chinese Simplified": "zh",
    },
    "google": {
        "Czech": "cs",
        "Danish": "da",
        "German": "de",
        "English": "en-US",
        "Spanish": "es",
        "French": "fr",
        "Hungarian": "hu",
        "Indonesian": "id",
        "Italian": "it",
        "Japanese": "ja",
        "Korean": "ko",
        "Dutch": "nl",
        "Polish": "pl",
        "Portuguese": "pt",
        "Russian": "ru",
        "Swedish": "sv",
        "Turkish": "tr",
        "Chinese Simplified": "zh-CN",
        "Chinese Traditional": "zh-TW",
    },
    "bing": {
        "Czech": "cs",
        "Danish": "da",
        "German": "de",
        "English": "en",
        "Spanish": "es",
        "French": "fr-CA",
        "Hungarian": "hu",
        "Indonesian": "id",
        "Italian": "it",
        "Japanese": "ja",
        "Korean": "ko",
        "Dutch": "nl",
        "Polish": "pl",
        "Portuguese": "pt-PT",
        "Russian": "ru",
        "Swedish": "sv",
        "Turkish": "tr",
        "Chinese Simplified": "zh-Hans",
        "Chinese Traditional": "zh-Hant",
    },
    "lingvanex": {
        "Czech": "cs_CZ",
        "Danish": "da_DK",
        "German": "de_DE",
        "English": "en_GB",
        "Spanish": "es_ES",
        "French": "fr_FR",
        "Hungarian": "hu_HU",
        "Indonesian": "id_ID",
        "Italian": "it_IT",
        "Japanese": "ja_JP",
        "Korean": "ko_KR",
        "Dutch": "nl_NL",
        "Polish": "pl_PL",
        "Portuguese": "pt_PT",
        "Russian": "ru_RU",
        "Swedish": "sv_SE",
        "Turkish": "tr_TR",
        "Chinese Simplified": "zh-Hans_CN",
    },
    "itranslate": {
        "Czech": "cs",
        "Danish": "da",
        "German": "de",
        "English": "en-US",
        "Spanish": "es-US",
        "French": "fr-FR",
        "Hungarian": "hu",
        "Indonesian": "id",
        "Italian": "it",
        "Japanese": "ja",
        "Korean": "ko",
        "Dutch": "nl",
        "Polish": "pl",
        "Portuguese": "pt-PT",
        "Russian": "ru",
        "Swedish": "sv",
        "Turkish": "tr",
        "Chinese Simplified": "zh-CN",
        "Chinese Traditional": "zh-TW",
    },
    "sysTran": {
        "Czech": "cs",
        "Danish": "da",
        "German": "de",
        "English": "en",
        "Spanish": "es",
        "French": "fr",
        "Hungarian": "hu",
        "Indonesian": "id",
        "Italian": "it",
        "Japanese": "ja",
        "Korean": "ko",
        "Dutch": "nl",
        "Polish": "pl",
        "Portuguese": "pt",
        "Russian": "ru",
        "Swedish": "sv",
        "Turkish": "tr",
        "Chinese Simplified": "zh",
    },
    "argos": {
        "Czech": "cs",
        "Danish": "da",
        "German": "de",
        "English": "en",
        "Spanish": "es",
        "French": "fr",
        "Hungarian": "hu",
        "Indonesian": "id",
        "Italian": "it",
        "Japanese": "ja",
        "Korean": "ko",
        "Dutch": "nl",
        "Polish": "pl",
        "Portuguese": "pt",
        "Russian": "ru",
        "Swedish": "sv",
        "Turkish": "tr",
        "Chinese Simplified": "zh",
    },
    "reverso": {
        "Czech": "cs",
        "Danish": "da",
        "German": "de",
        "English": "en",
        "Spanish": "es",
        "French": "fr",
        "Hungarian": "hu",
        "Indonesian": "id",
        "Italian": "it",
        "Japanese": "ja",
        "Korean": "ko",
        "Dutch": "nl",
        "Polish": "pl",
        "Portuguese": "pt",
        "Russian": "ru",
        "Swedish": "sv",
        "Turkish": "tr",
        "Chinese Simplified": "zh",
    },
    "deepl": {
        "Czech": "cs",
        "Danish": "da",
        "German": "de",
        "English": "en",
        "Spanish": "es",
        "French": "fr",
        "Hungarian": "hu",
        "Indonesian": "id",
        "Italian": "it",
        "Japanese": "ja",
        "Korean": "ko",
        "Dutch": "nl",
        "Polish": "pl",
        "Portuguese": "pt",
        "Russian": "ru",
        "Swedish": "sv",
        "Turkish": "tr",
        "Chinese Simplified": "zh",
    },
    "cloudTranslation": {
        "German": "de",
        "English": "en-us",
        "Spanish": "es",
        "French": "fr",
        "Indonesian": "id",
        "Italian": "it",
        "Japanese": "ja",
        "Korean": "ko",
        "Dutch": "nl",
        "Polish": "pl",
        "Portuguese": "pt",
        "Russian": "ru",
        "Turkish": "tr",
        "Chinese Simplified": "zh-cn",
        "Chinese Traditional": "zh-tw",
    },
    "qqTranSmart": {
        "Czech": "cs",
        "Danish": "da",
        "German": "de",
        "English": "en",
        "Spanish": "es",
        "French": "fr",
        "Hungarian": "hu",
        "Indonesian": "id",
        "Italian": "it",
        "Japanese": "ja",
        "Korean": "ko",
        "Dutch": "nl",
        "Polish": "pl",
        "Portuguese": "pt-PT",
        "Russian": "ru",
        "Swedish": "sv",
        "Turkish": "tr",
        "Chinese Simplified": "zh",
    },
    "translateCom": {
        "English": "en-gb",
        "French": "fr-ca",
        "German": "de",
        "Italian": "it",
        "Portuguese": "pt-br",
        "Russian": "ru",
        "Spanish": "es-la",
        "Japanese": "ja",
        "Chinese Simplified": "zh",
        "Chinese Traditional": "zh-TW",
        "Korean": "ko",
        "Polish": "pl",
        "Dutch": "nl",
        "Indonesian": "id",
        "Swedish": "sv",
        "Danish": "da",
        "Czech": "cs",
        "Turkish": "tr",
        "Hungarian": "hu",
    },
    "sogou": {
        "Polish": "pl",
        "Danish": "da",
        "German": "de",
        "Russian": "ru",
        "French": "fr",
        "Korean": "ko",
        "Dutch": "nl",
        "Czech": "cs",
        "Portuguese": "pt",
        "Japanese": "ja",
        "Swedish": "sv",
        "Spanish": "es",
        "Hungarian": "hu",
        "English": "en",
        "Italian": "it",
        "Chinese Simplified": "zh-CHS",
    },
    "qqFanyi": {
        "English": "en",
        "Chinese Simplified": "zh",
        "French": "fr",
        "Spanish": "es",
        "Italian": "it",
        "German": "de",
        "Turkish": "tr",
        "Russian": "ru",
        "Portuguese": "pt",
        "Indonesian": "id",
    },
    "papago": {
        "German": "de",
        "English": "en",
        "Spanish": "es",
        "French": "fr",
        "Indonesian": "id",
        "Italian": "it",
        "Japanese": "ja",
        "Korean": "ko",
        "Portuguese": "pt",
        "Russian": "ru",
        "Chinese Simplified": "zh-CN",
        "Chinese Traditional": "zh-TW",
    },
    "youdao": {
        "German": "de",
        "English": "en",
        "Spanish": "es",
        "French": "fr",
        "Indonesian": "id",
        "Japanese": "ja",
        "Korean": "ko",
        "Portuguese": "pt",
        "Russian": "ru",
        "Chinese Simplified": "zh-CHS",
    },
    "iflyrec": {
        "German": "de",
        "English": "en",
        "Spanish": "es",
        "French": "fr",
        "Italian": "it",
        "Japanese": "ja",
        "Korean": "ko",
        "Russian": "ru",
        "Chinese Simplified": "zh",
    },
    "caiyun": {
        "English": "en",
        "Spanish": "es",
        "French": "fr",
        "Japanese": "ja",
        "Korean": "ko",
        "Russian": "ru",
        "Chinese Simplified": "zh",
    },
}