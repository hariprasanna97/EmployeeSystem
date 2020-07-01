"""
This script trains sentence transformers with a triplet loss function.
You can get the dataset by running examples/datasets/generate_settings_triplet_data.py
"""

from sentence_transformers import SentenceTransformer, SentencesDataset, LoggingHandler, losses, models
from torch.utils.data import DataLoader
from sentence_transformers.readers import TripletReader
from sentence_transformers.evaluation import TripletEvaluator
from datetime import datetime

import csv
import logging



logging.basicConfig(format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO,
                    handlers=[LoggingHandler()])

model_path="Albert_output_Epochs_20/training_stsbenchmark_albert-Epcohs_20"

#You can specify any huggingface/transformers pre-trained model here, for example, bert-base-uncased, roberta-base, xlm-roberta-base
#model_name = 'distilbert-base-nli-stsb-mean-tokens'


### Create a torch.DataLoader that passes training batch instances to our model
train_batch_size = 32
triplet_reader = TripletReader('datasets/settings-query-triplets', s1_col_idx=0, s2_col_idx=1, s3_col_idx=2, delimiter=',', quoting=csv.QUOTE_MINIMAL, has_header=True)
output_path = "output/training-settings-queries-"+model_name+"-"+datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
num_epochs = 1


model = SentenceTransformer(model_path)


logging.info("Read Triplet train dataset")
train_data = SentencesDataset(examples=triplet_reader.get_examples('train.csv'), model=model)
train_dataloader = DataLoader(train_data, shuffle=True, batch_size=train_batch_size)
train_loss = losses.TripletLoss(model=model)

logging.info("Read Settings Triplet dev dataset")
dev_data = SentencesDataset(examples=triplet_reader.get_examples('validation.csv', 1000), model=model)
dev_dataloader = DataLoader(dev_data, shuffle=False, batch_size=train_batch_size)
evaluator = TripletEvaluator(dev_dataloader)


warmup_steps = int(len(train_data)*num_epochs/train_batch_size*0.1) #10% of train data


# Train the model
model.fit(train_objectives=[(train_dataloader, train_loss)],
          evaluator=evaluator,
          epochs=num_epochs,
          evaluation_steps=1000,
          warmup_steps=warmup_steps,
          output_path=output_path)

##############################################################################
#
# Load the stored model and evaluate its performance on STS benchmark dataset
#
##############################################################################

model = SentenceTransformer(output_path)
test_data = SentencesDataset(examples=triplet_reader.get_examples('test.csv'), model=model)
test_dataloader = DataLoader(test_data, shuffle=False, batch_size=train_batch_size)
evaluator = TripletEvaluator(test_dataloader)

model.evaluate(evaluator)
