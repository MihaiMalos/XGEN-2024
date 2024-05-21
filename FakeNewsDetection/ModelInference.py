from transformers import RobertaTokenizer, RobertaModel
import torch
from torch import cuda
from tqdm import tqdm
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

# Load the tokenizer
tokenizer = RobertaTokenizer.from_pretrained("./model/tokenizer")

# Load the model
model = RobertaClass()
model.load_state_dict(torch.load('./model/fake_news.bin'))
model.to(device)
model.eval()

sentence = "(Reuters) - A lottery drawing to settle a tied Virginia legislative race that could shift the statehouse balance of power has been indefinitely postponed, state election officials said on Tuesday, after the Democratic candidate mounted a legal fight. The decision to put off the high-stakes lotto, originally scheduled for Wednesday, marks the latest twist in a dramatic election recount that at one point showed Democrat Shelly Simonds beating Republican incumbent David Yancey by a single vote.  A victory by Simonds would shift Republicansâ€™ slim control of the 100-member House of Delegates to an even 50-50 split with the Democrats, forcing the two parties into a rare power-sharing arrangement. A day after Simonds emerged as the victor of a recount, a three-judge panel ruled that a disputed ballot should be counted for Yancey. That decision left the two candidates tied with 11,608 votes each in a district that encompasses the shipping hub of Newport News in southeastern Virginia, setting the stage for the equivalent of a coin toss to pick a final winner. Simonds asked a state court to reconsider on Tuesday, arguing that the disputed ballot was wrongly included. An image filed in court showed that the ballot had bubbles filled in beside both names, with a slash mark by Simondsâ€™ name. The voter selected Republicans for other offices. Simonds told reporters that the case had implications not only for her contest but for the integrity of state elections as a whole, saying that without a court ruling in her favor, â€œrecounts would become a never-ending spiral of courtroom challenges.â€ The chairman of the Virginia Board of Elections, James Alcorn, said in a statement that while holding a lottery would be in keeping with state law, such a move should be considered â€œan action of last resort.â€ He added: â€œAny substantive concerns regarding the election or recount should be resolved before a random drawing is conducted.â€    Yanceyâ€™s campaign did not immediately respond to requests for comment. The Virginia House Republican Caucus said in a statement that it was reviewing the new court filings. â€œWe believe the court acted appropriately and that the integrity of the process is without question,â€ spokesman Parker Slaybaugh said. Virginia Department of Elections spokeswoman Andrea Gaines said in an email that no new date for a drawing has been set"


inputs = tokenizer(sentence, return_tensors="pt").to(device)
with torch.no_grad():
    data = inputs
    ids = data['input_ids'].to(device, dtype=torch.long)
    mask = data['attention_mask'].to(device, dtype=torch.long)

    outputs = model(ids, mask)
    print(torch.argmax(outputs).item())

# Convert logits to probabilities
