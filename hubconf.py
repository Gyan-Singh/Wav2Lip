def custom(path):
  """Loads the Wav2Lip model from the given path."""
  from Wav2Lip.models import Wav2Lip
  return Wav2Lip(path)
