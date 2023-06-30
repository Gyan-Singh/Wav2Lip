def custom(path):
  """Loads the Wav2Lip model from the given path."""
  from wav2lip import Wav2Lip
  return Wav2Lip(path)