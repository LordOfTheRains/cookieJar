from __future__ import absolute_import

import unittest
from softwareprocess.operations.correct import Correct


class CorrectTest(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_validate_parameter_mandatory_information(self):
        # tests following mandatory parameter presence
        # lat xdyy.y
        # long xdyy.y
        # altitude xdyy.y
        # assumedLat xdyy.y
        # assumedLong xdyy.y
        expected = "mandatory information is missing"
        
        # happy path
        # all parameter present
        input_dict = {'op': 'correct', 'lat': "asdsad", 'long': "adsa",
                      'assumedLat': 'unknown', 'assumedLong': '2016-01-17',
                      'altitude': '03:15:99'}
        result = Correct.validate_parameter(input_dict)
        self.assertTrue(result)
        
        # sad path
        # missing lat
        
        input_dict = {'op': 'correct', 'lat1': "asdsad", 'long': "adsa",
                      'assumedLat': 'unknown', 'assumedLong': '2016-01-17',
                      'altitude': '03:15:99'}
        result = Correct.validate_parameter(input_dict)
        self.assertTrue(expected in result)

        # missing long
        input_dict = {'op': 'correct', 'lat': "asdsad", 'long1': "adsa",
                      'assumedLat': 'unknown', 'assumedLong': '2016-01-17',
                      'altitude': '03:15:99'}
        result = Correct.validate_parameter(input_dict)
        self.assertTrue(expected in result)
        
        # missing altitude
        input_dict = {'op': 'correct', 'lat': "asdsad", 'long': "adsa",
                      'assumedLat': 'unknown', 'assumedLong': '2016-01-17',
                      'altitude1': '03:15:99'}
        result = Correct.validate_parameter(input_dict)
        self.assertTrue(expected in result)
        
        # missing assumedLat
        input_dict = {'op': 'correct', 'lat': "asdsad", 'long': "adsa",
                      'assumed1Lat': 'unknown', 'assumedLong': '2016-01-17',
                      'altitude': '03:15:99'}
        result = Correct.validate_parameter(input_dict)
        self.assertTrue(expected in result)
        
        # missing assumedLong
        input_dict = {'op': 'correct', 'lat': "asdsad", 'long': "adsa",
                      'assumedLat': 'unknown', 'assumed1Long': '2016-01-17',
                      'altitude': '03:15:99'}
        result = Correct.validate_parameter(input_dict)
        self.assertTrue(expected in result)
    
    def test_validate_parameter_long(self):
        # long: mandatory, unvalidated,
        # xdyy.y
        # x GT -90 and LT 90
        # yy.y GT 0 and LT 60.0
        
        # happy path
        # high bound long
        input_dict = {'op': 'correct', 'long': "89d59.9", 'lat': "89d59.9",
                      'assumedLat': '89d59.9', 'assumedLong': '89d59.9',
                      'altitude': '89d59.9'}
        result = Correct.validate_parameter(input_dict)
        self.assertTrue(result)
        
        # low bound long
        input_dict = {'op': 'correct', 'long': "-89d59.9", 'lat': "-89d59.9",
                      'assumedLat': '-89d59.9', 'assumedLong': '-89d59.9',
                      'altitude': '-89d59.9'}
        result = Correct.validate_parameter(input_dict)
        self.assertTrue(result)
        
        # normal long
        input_dict = {'op': 'correct', 'long': "0d0.0", 'lat': "-89d59.9",
                      'assumedLat': '-89d59.9', 'assumedLong': '-89d59.9',
                      'altitude': '-89d59.9'}
        result = Correct.validate_parameter(input_dict)
        self.assertTrue(result)
        
        # sad path
        # not string
        
        input_dict = {'op': 'correct', 'long': 123, 'lat': "-89d59.9",
                      'assumedLat': '-89d59.9', 'assumedLong': '-89d59.9',
                      'altitude': '-89d59.9'}
        result = Correct.validate_parameter(input_dict)
        self.assertTrue("Longitude Must be A String Value" in result, result)
        
        # bad format
        input_dict = {'op': 'correct', 'long': "-89d001.9", 'lat': "-89d59.9",
                      'assumedLat': '-89d59.9', 'assumedLong': '-89d59.9',
                      'altitude': '-89d59.9'}
        result = Correct.validate_parameter(input_dict)
        self.assertTrue("Incorrect Longitude Format: xdyy.y" in result, result)
        
        # bad format
        input_dict = {'op': 'correct', 'long': "12ddd12.3", 'lat': "-89d59.9",
                      'assumedLat': '-89d59.9', 'assumedLong': '-89d59.9',
                      'altitude': '-89d59.9'}
        result = Correct.validate_parameter(input_dict)
        self.assertTrue("Incorrect Longitude Format: xdyy.y" in result, result)
        
        # bad format
        input_dict = {'op': 'correct', 'long': "12d12..3", 'lat': "-89d59.9",
                      'assumedLat': '-89d59.9', 'assumedLong': '-89d59.9',
                      'altitude': '-89d59.9'}
        result = Correct.validate_parameter(input_dict)
        self.assertTrue("Incorrect Longitude Format: xdyy.y" in result, result)
        
        # out of high range
        input_dict = {'op': 'correct', 'long': "90d00.0", 'lat': "-89d59.9",
                      'assumedLat': '-89d59.9', 'assumedLong': '-89d59.9',
                      'altitude': '-89d59.9'}
        result = Correct.validate_parameter(input_dict)
        self.assertTrue("Longitude Out of Range: -90.0 < long < 90.0" in result, result)
        
        # out of low range
        input_dict = {'op': 'correct', 'long': "-90d00.0", 'lat': "-89d59.9",
                      'assumedLat': '-89d59.9', 'assumedLong': '-89d59.9',
                      'altitude': '-89d59.9'}
        result = Correct.validate_parameter(input_dict)
        self.assertTrue("Longitude Out of Range: -90.0 < long < 90.0" in result, result)
        
        # out of arc minute range
        input_dict = {'op': 'correct', 'long': "30d70.0", 'lat': "-89d59.9",
                      'assumedLat': '-89d59.9', 'assumedLong': '-89d59.9',
                      'altitude': '-89d59.9'}
        result = Correct.validate_parameter(input_dict)
        self.assertTrue("Longitude Minute Out of Range: 0 <= long < 60.0" in result, result)
        
    def test_validate_parameter_lat(self):
        # lat: mandatory, unvalidated,
        # xdyy.y
        # x GT -90 and LT 90
        # yy.y GT 0 and LT 60.0
        
        # happy path
        # high boiund lat
        input_dict = {'op': 'correct', 'lat': "89d59.9", 'long': "89d59.9",
                      'assumedLat': '89d59.9', 'assumedLong': '89d59.9',
                      'altitude': '89d59.9'}
        result = Correct.validate_parameter(input_dict)
        self.assertTrue(result)
        
        # low bound lat
        input_dict = {'op': 'correct', 'lat': "-89d59.9", 'long': "-89d59.9",
                      'assumedLat': '-89d59.9', 'assumedLong': '-89d59.9',
                      'altitude': '-89d59.9'}
        result = Correct.validate_parameter(input_dict)
        self.assertTrue(result)
        
        # normal lat
        input_dict = {'op': 'correct', 'lat': "0d0.0", 'long': "-89d59.9",
                      'assumedLat': '-89d59.9', 'assumedLong': '-89d59.9',
                      'altitude': '-89d59.9'}
        result = Correct.validate_parameter(input_dict)
        self.assertTrue(result)
        
        # sad path
        # not string
        
        input_dict = {'op': 'correct', 'lat': 123, 'long': "-89d59.9",
                      'assumedLat': '-89d59.9', 'assumedLong': '-89d59.9',
                      'altitude': '-89d59.9'}
        result = Correct.validate_parameter(input_dict)
        self.assertTrue("Latitude Must be A String Value" in result, result)
        
        # bad format
        input_dict = {'op': 'correct', 'lat': "-89d001.9", 'long': "-89d59.9",
                      'assumedLat': '-89d59.9', 'assumedLong': '-89d59.9',
                      'altitude': '-89d59.9'}
        result = Correct.validate_parameter(input_dict)
        self.assertTrue("Incorrect Latitude Format: xdyy.y" in result, result)
        
        # bad format
        input_dict = {'op': 'correct', 'lat': "12ddd12.3", 'long': "-89d59.9",
                      'assumedLat': '-89d59.9', 'assumedLong': '-89d59.9',
                      'altitude': '-89d59.9'}
        result = Correct.validate_parameter(input_dict)
        self.assertTrue("Incorrect Latitude Format: xdyy.y" in result, result)
        
        # bad format
        input_dict = {'op': 'correct', 'lat': "12d12..3", 'long': "-89d59.9",
                      'assumedLat': '-89d59.9', 'assumedLong': '-89d59.9',
                      'altitude': '-89d59.9'}
        result = Correct.validate_parameter(input_dict)
        self.assertTrue("Incorrect Latitude Format: xdyy.y" in result, result)
        
        # out of high range
        input_dict = {'op': 'correct', 'lat': "90d00.0", 'long': "-89d59.9",
                      'assumedLat': '-89d59.9', 'assumedLong': '-89d59.9',
                      'altitude': '-89d59.9'}
        result = Correct.validate_parameter(input_dict)
        self.assertTrue("Latitude Out of Range: -90.0 < lat < 90.0" in result, result)
        
        # out of low range
        input_dict = {'op': 'correct', 'lat': "-90d00.0", 'long': "-89d59.9",
                      'assumedLat': '-89d59.9', 'assumedLong': '-89d59.9',
                      'altitude': '-89d59.9'}
        result = Correct.validate_parameter(input_dict)
        self.assertTrue("Latitude Out of Range: -90.0 < lat < 90.0" in result, result)
        
        # out of arc minute range
        input_dict = {'op': 'correct', 'lat': "30d70.0", 'long': "-89d59.9",
                      'assumedLat': '-89d59.9', 'assumedLong': '-89d59.9',
                      'altitude': '-89d59.9'}
        result = Correct.validate_parameter(input_dict)
        self.assertTrue("Latitude Minute Out of Range: 0 <= lat < 60.0" in result, result)
