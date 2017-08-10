import tensorflow as tf
import opennmt as onmt

def model():
  return onmt.models.SequenceToSequence(
    source_embedder=onmt.embedders.WordEmbedder(
      vocabulary_file="data/en-dict.txt",
      embedding_size=512),
    target_embedder=onmt.embedders.WordEmbedder(
      vocabulary_file="data/fr-dict.txt",
      embedding_size=512),
    encoder=onmt.encoders.BidirectionalRNNEncoder(
      num_layers=2,
      num_units=512,
      cell_class=tf.contrib.rnn.LSTMCell,
      dropout=0.3,
      residual_connections=False),
    decoder=onmt.decoders.AttentionalRNNDecoder(
      num_layers=4,
      num_units=512,
      bridge=onmt.utils.DenseBridge(),
      attention_mechanism_class=tf.contrib.seq2seq.LuongAttention,
      cell_class=tf.contrib.rnn.LSTMCell,
      dropout=0.3,
      residual_connections=False))

def train(model):
  model.set_filters(
    maximum_source_length=70,
    maximum_target_length=70)

def infer(model):
  pass