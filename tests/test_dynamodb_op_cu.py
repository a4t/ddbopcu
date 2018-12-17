import unittest
import opcu
from datetime import datetime
import copy


class TestCore(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        tables = ["hoge", "fuga"]
        cls.opcu = opcu.Opcu(tables)
        cls.response = cls.__sample_response()

    def __sample_response():
        return {
            'Table': {
                'AttributeDefinitions': [{
                    'AttributeName': 'created',
                    'AttributeType': 'S'
                }, {
                    'AttributeName': 'id',
                    'AttributeType': 'S'
                }],
                'TableName':
                'prescription-dev',
                'KeySchema': [{
                    'AttributeName': 'id',
                    'KeyType': 'HASH'
                }],
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 20,
                    'WriteCapacityUnits': 30
                },
                'GlobalSecondaryIndexes': [{
                    'IndexName': 'hoge',
                    'ProvisionedThroughput': {
                        'ReadCapacityUnits': 50,
                        'WriteCapacityUnits': 60
                    },
                }, {
                    'IndexName': 'fuga',
                    'ProvisionedThroughput': {
                        'ReadCapacityUnits': 70,
                        'WriteCapacityUnits': 100
                    },
                }]
            }
        }

    def test_add_record_start_time(self):
        self.opcu.add_record_start_time()
        start_time = datetime.now().strftime('%s')
        end_time = datetime.now().strftime('%s')
        self.assertTrue(start_time <= self.opcu.tables_cu['common']['record_start_time'] <= end_time)

    def test_add_record_end_time(self):
        self.opcu.add_record_end_time()
        start_time = datetime.now().strftime('%s')
        end_time = datetime.now().strftime('%s')
        self.assertTrue(start_time <= self.opcu.tables_cu['common']['record_end_time'] <= end_time)

    def test_add_table_cu(self):
        result = self.opcu.add_table_cu(self.response['Table'])
        self.assertEquals(result['ProvisionedThroughput']['ReadCapacityUnits'], self.response['Table']['ProvisionedThroughput']['ReadCapacityUnits'])
        self.assertEquals(result['ProvisionedThroughput']['WriteCapacityUnits'], self.response['Table']['ProvisionedThroughput']['WriteCapacityUnits'])

    def test_get_gsi_cu(self):
        result = self.opcu.get_gsi_cu(self.response)
        self.assertEquals(result['GlobalSecondaryIndexes'][0]['IndexName'], self.response['Table']['GlobalSecondaryIndexes'][0]['IndexName'])
        self.assertEquals(result['GlobalSecondaryIndexes'][0]['ProvisionedThroughput'], self.response['Table']['GlobalSecondaryIndexes'][0]['ProvisionedThroughput'])
        self.assertEquals(result['GlobalSecondaryIndexes'][1]['ProvisionedThroughput'], self.response['Table']['GlobalSecondaryIndexes'][1]['ProvisionedThroughput'])

    def test_get_gsi_cu_with_empty(self):
        empty_response = copy.deepcopy(self.response)
        empty_response['Table']['GlobalSecondaryIndexes'] = []
        result = self.opcu.get_gsi_cu(empty_response)
        print(result)
        self.assertEquals(result['GlobalSecondaryIndexes'], [])


if __name__ == '__main__':
    unittest.main()
