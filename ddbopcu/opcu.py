import boto3
import boto3.session
from datetime import datetime


class Opcu:
    def __init__(self, tables):
        self.tables = tables
        self.client = boto3.Session().client('dynamodb')
        self.tables_cu = {'common': {}, 'tables': []}

    def add_record_start_time(self):
        self.tables_cu['common']['record_start_time'] = datetime.now().strftime('%s')

    def add_record_end_time(self):
        self.tables_cu['common']['record_end_time'] = datetime.now().strftime('%s')

    def add_table_cu(self, table_val):
        return {'ProvisionedThroughput': {'ReadCapacityUnits': table_val['ProvisionedThroughput']['ReadCapacityUnits'], 'WriteCapacityUnits': table_val['ProvisionedThroughput']['WriteCapacityUnits']}}

    def get_gsi_cu(self, table_detail):
        table_name = table_detail['Table']['TableName']
        gsi_cus = {'GlobalSecondaryIndexes': []}
        for gsi_key, gsi_val in enumerate(table_detail['Table']['GlobalSecondaryIndexes']):
            gsi_cus['GlobalSecondaryIndexes'].append({
                'IndexName': gsi_val['IndexName'],
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': gsi_val['ProvisionedThroughput']['ReadCapacityUnits'],
                    'WriteCapacityUnits': gsi_val['ProvisionedThroughput']['WriteCapacityUnits']
                }
            })
        return gsi_cus

    def add_cu(self, table_name):
        table_detail = self.client.describe_table(TableName=table_name)
        want_data = {}
        want_data.update({'name': table_detail['Table']['TableName']})
        want_data.update(self.add_table_cu(table_detail['Table']))
        want_data.update(self.get_gsi_cu(table_detail))
        self.tables_cu['tables'].append(want_data)

    def get_cu(self):
        self.add_record_start_time()
        for table_key, table_name in enumerate(self.tables):
            self.add_cu(table_name)
        self.add_record_end_time()

        return self.tables_cu
