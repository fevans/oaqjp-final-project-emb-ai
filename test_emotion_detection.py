import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        # test for joy
        expected_emotion='joy'
        joy = emotion_detector('I am glad this happened')
        self.assertEqual(expected_emotion, joy['dominant_emotion'].lower())

        # test for anger
        expected_emotion='anger'
        anger = emotion_detector('I am really mad about this')
        self.assertEqual(expected_emotion, anger['dominant_emotion'].lower())

        # test for disgust
        expected_emotion='disgust'
        anger = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(expected_emotion, anger['dominant_emotion'].lower())

        # test for sadness
        expected_emotion='sadness'
        anger = emotion_detector('I am so sad about this')
        self.assertEqual(expected_emotion, anger['dominant_emotion'].lower())

        # test for fear
        expected_emotion='fear'
        anger = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(expected_emotion, anger['dominant_emotion'].lower())

unittest.main()

