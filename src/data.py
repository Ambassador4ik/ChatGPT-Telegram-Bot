from yaml import safe_load


class Data:
    current_token: int = -1
    token_count: int

    def __init__(self, path):
        # Load tokens from config.yml
        with open(path) as f:
            cfg = safe_load(f)
        telegram_tokens = cfg['Telegram']
        self.telegram_app_hash = telegram_tokens['TelegramAppHash']
        self.telegram_app_id = telegram_tokens['TelegramAppId']

        openai_tokens = cfg['OpenAI']
        self.openai_tokens = openai_tokens['Tokens']
        self.token_count = len(self.openai_tokens)

    def next_token(self):
        self.current_token += 1
        if self.current_token >= self.token_count:
            self.current_token = 0
        return self.openai_tokens[self.current_token]


config = Data('config.yml')
