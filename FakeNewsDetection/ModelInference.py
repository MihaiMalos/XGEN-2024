from transformers import RobertaTokenizer, RobertaModel
import torch
from torch import cuda
from tqdm import tqdm
from torchinfo import summary
device = 'cuda' if cuda.is_available() else 'cpu'

class RobertaClass(torch.nn.Module):
    def __init__(self):
        super(RobertaClass, self).__init__()
        self.l1 = RobertaModel.from_pretrained("roberta-base")
        self.pre_classifier = torch.nn.Linear(768, 768)
        self.dropout = torch.nn.Dropout(0.3)
        self.classifier = torch.nn.Linear(768, 2)

    def forward(self, input_ids, attention_mask, token_type_ids=None):
        output_1 = self.l1(input_ids=input_ids, attention_mask=attention_mask)
        hidden_state = output_1[0]
        pooler = hidden_state[:, 0]
        pooler = self.pre_classifier(pooler)
        pooler = torch.nn.ReLU()(pooler)
        pooler = self.dropout(pooler)
        output = self.classifier(pooler)
        return output


class RobertaInference:
    def __init__(self):
        self._tokenizer = RobertaTokenizer.from_pretrained("./model/tokenizer")

        self._model = RobertaClass()
        self._model.load_state_dict(torch.load('./model/fake_news.bin', map_location=device))
        self._model.to(device)
        self._model.eval()

    def run(self, sentence):
        words = sentence.split()
        truncated_words = words[:370]
        sentence = ' '.join(truncated_words)
        inputs = self._tokenizer(sentence, return_tensors="pt").to(device)
        with torch.no_grad():
            data = inputs
            ids = data['input_ids'].to(device, dtype=torch.long)
            mask = data['attention_mask'].to(device, dtype=torch.long)

            outputs = self._model(ids, mask)

            return "Real" if torch.argmax(outputs).item() == 1 else "Fake"
