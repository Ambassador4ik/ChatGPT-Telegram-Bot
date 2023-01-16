from yaml import safe_load


class Data:
    def __init__(self, path):
        # Load tokens from config.yml
        with open(path) as f:
            cfg = safe_load(f)
        telegram_tokens = cfg['Telegram']
        self.telegram_app_hash = telegram_tokens['TelegramAppHash']
        self.telegram_app_id = telegram_tokens['TelegramAppId']

        openai_tokens = cfg['OpenAI']
        self.openai_token = openai_tokens['Token']


config = Data('config.yml')
