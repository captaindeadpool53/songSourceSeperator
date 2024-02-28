class ConfigurationHandler :
	def __init__(self, TRAINING_DATA_ROOT, SAMPLE_RATE, SEGMENT_LENGTH_IN_SECONDS, FRAME_SIZE, HOP_LENGTH,NUMBER_OF_OUTPUT_CHANNELS, SONG_TO_PREDICT_PATH ) -> None:
		self.TRAINING_DATA_ROOT: str = TRAINING_DATA_ROOT
		self.SAMPLE_RATE: int = SAMPLE_RATE
		self.SEGMENT_LENGTH: float = SEGMENT_LENGTH_IN_SECONDS
		self.FRAME_SIZE: int = FRAME_SIZE
		self.HOP_LENGTH: int = HOP_LENGTH
		self.SONG_TO_PREDICT_PATH: str = SONG_TO_PREDICT_PATH
  
		self.SAMPLES_PER_SEGMENT = self.SEGMENT_LENGTH * self.SAMPLE_RATE
		self.FRAMES_IN_SEGMENT = 1 + (self.SAMPLES_PER_SEGMENT - self.FRAME_SIZE)//self.HOP_LENGTH
		self.FREQUENCY_BINS = 1 + self.FRAME_SIZE//2
		self.SPECTROGTRAM_SHAPE = [self.FREQUENCY_BINS, self.FRAMES_IN_SEGMENT]
		self.INPUT_SHAPE = self.SPECTROGTRAM_SHAPE + [1]
		self.NUMBER_OF_OUTPUT_CHANNELS = NUMBER_OF_OUTPUT_CHANNELS
		self.OUTPUT_SHAPE = self.INPUT_SHAPE[:-1]+[self.NUMBER_OF_OUTPUT_CHANNELS]