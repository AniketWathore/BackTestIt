from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import re

class TextToStrategy:
    def __init__(self):
        # Use T5 for code gen or fine-tune on trading dataset
        self.tokenizer = AutoTokenizer.from_pretrained('t5-small')
        self.model = AutoModelForSeq2SeqLM.from_pretrained('t5-small')
        self.generator = pipeline('text2text-generation', model=self.model, tokenizer=self.tokenizer)
    
    def parse_text(self, text: str, start_date: str, end_date: str):
        # Extract keywords: e.g., re.findall(r'EMA(\d+)', text)
        indicators = re.findall(r'(EMA|SMA|RSI)(\d+)', text)
        actions = re.findall(r'(buy|sell|crossover)', text.lower())
        
        # Generate code snippet
        prompt = f"Convert trading strategy '{text}' to Python using TA-Lib for dates {start_date} to {end_date}"
        code = self.generator(prompt, max_length=100)[0]['generated_text']
        
        # Exec to create strategy func (sandbox for safety)
        strategy_func = self._safe_exec(code)
        return lambda data: strategy_func(data)  # Returns signals