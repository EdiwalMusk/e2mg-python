import fileinput

import torch
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter()

embedded = torch.randn(4, 50)

meta = list(map(lambda x: x.strip(), fileinput.FileInput("./vocba2.csv")))
writer.add_embedding(embedded, metadata=meta)

writer.close()
