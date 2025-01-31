class PROMPT:
    def __init__(self,
                 model='general',
                 instruction_text=None,
                 request_text=None,
                 max_tokens=None,
                 temperature=None):

        self.model = model
        self.instruction_text = instruction_text
        self.request_text = request_text
        self.generation_options = {"max_tokens": max_tokens,
                                   "temperature": temperature}

    def set_generation_options(self, max_tokens=7400, temperature=0.5):
        self.generation_options['max_tokens'] = max_tokens
        self.generation_options['temperature'] = temperature

    def set_instruction_text(self, instruction_text):
        self.instruction_text = instruction_text

    def generate_prompt(self, request_text):
        self.request_text = request_text
        result = {
            "model": self.model,
            "instruction_text": self.instruction_text,
            "request_text": self.request_text,
            "generation_options": self.generation_options
        }
        return result
