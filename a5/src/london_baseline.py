# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
from tqdm import tqdm
import utils
predictions = []
for line in tqdm(open('birth_dev.tsv')):
    pred = 'London'
    predictions.append(pred)
total, correct = utils.evaluate_places('birth_dev.tsv', predictions)
print('Correct: {} out of {}: {}%'.format(correct, total, correct / total * 100))