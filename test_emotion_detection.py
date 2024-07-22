import unittest
import json
import EmotionDetection

class TestEmotionDetection(unittest.TestCase):
    def testJoy(self):
        result = EmotionDetection.emotion_detection.emotion_detector("I am glad this happened")
        self.assertEqual(json.loads(result)["dominant_emotion"], "joy")
    def testAnger(self):
        result = EmotionDetection.emotion_detection.emotion_detector("I am really mad about this")
        self.assertEqual(json.loads(result)["dominant_emotion"], "anger")
    def testDisgust(self):
        result = EmotionDetection.emotion_detection.emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(json.loads(result)["dominant_emotion"], "disgust")
    def testSadness(self):
        result = EmotionDetection.emotion_detection.emotion_detector("I am so sad about this")
        self.assertEqual(json.loads(result)["dominant_emotion"], "sadness")
    def testFear(self):
        result = EmotionDetection.emotion_detection.emotion_detector("I am really afraid that this will happen")
        self.assertEqual(json.loads(result)["dominant_emotion"], "fear")

if __name__ == "__main__":
    unittest.main()
