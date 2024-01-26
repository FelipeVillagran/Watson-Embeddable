from emotion_detection import analyze_emotions
import unittest


class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        joy = 'joy'
        anger = 'anger'
        disgust = 'disgust'
        sadness = 'sadness'
        fear = 'fear'
        
        # Testing positive emotion detection
        result_1 = analyze_emotions('I am glad this happend')
        self.assertEqual(result_1['dominant_emotion'], joy)
        
        result_2 = analyze_emotions('I am really mad about this')
        self.assertEqual(result_2['dominant_emotion'], anger)
        
        result_3 = analyze_emotions('I feel disgusted just hearing about this')
        self.assertEqual(result_3['dominant_emotion'], disgust)
        
        result_4 = analyze_emotions('I am so sad about this')
        self.assertEqual(result_4['dominant_emotion'], sadness)
        
        result_5 = analyze_emotions('I am really afraid that this will happen')
        self.assertEqual(result_5['dominant_emotion'], fear)
        
if __name__ == '__main__':
    unittest.main()