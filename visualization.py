import sys;
sys.path.append("/home/yunshanl/test_1/user") 
import my_problem

import os
import tensorflow as tf
from tensor2tensor import problems
from tensor2tensor.bin import t2t_decoder  # To register the hparams set
from tensor2tensor.utils import registry
from tensor2tensor.utils import trainer_lib
from tensor2tensor.visualization import attention
from tensor2tensor.visualization import visualization

# Load the model
CHECKPOINT = os.path.expanduser("/home/yunshanl/test_1/train/")
# HParams
problem_name = 'my_problem'
data_dir = os.path.expanduser('/home/yunshanl/test_1/data')
model_name = "transformer"
hparams_set = "transformer_small"

visualizer = visualization.AttentionVisualizer(hparams_set, model_name, data_dir, problem_name, beam_size=1)

tf.Variable(0, dtype=tf.int64, trainable=False, name='global_step')
sess = tf.train.MonitoredTrainingSession(
    checkpoint_dir=CHECKPOINT,
    save_summaries_secs=0,
)

print("done")
input_sentence = "0:35:000000000:Huntley:F:Zahrayh::PO Box 3642::Cleveland:OH:44100"
output_string, inp_text, out_text, att_mats = visualizer.get_vis_data_from_string(sess, input_sentence)
print("start to print")
print(output_string)

attention.show(inp_text, out_text, *att_mats)
