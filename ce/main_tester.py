import os
import unittest
from ce.utils import __, log, local
from ce import data_view as dv
from ce.config_util import Config


class MainUnittest(unittest.TestCase):
    def setUp(self):
        with local.cwd('../test_env'):
            Config.Global('../default.conf')
            dv.init_shared_db(True)

    def test_add_record(self):
        config_path = os.path.join(os.getcwd(), '../ce/default.conf')
        logs = __(
            'python main.py --config %s --is_test 1 --workspace ../test_env' %
            config_path)
        log.info('logs', logs)
        kpi = dv.shared_db.get({}, table='kpi')
        task = dv.shared_db.get({}, table='task')
        commit = dv.shared_db.get({}, table='commit')
        self.assertTrue(kpi)
        self.assertTrue(task)
        self.assertTrue(commit)
        log.info('kpi', kpi)
        log.info('task', task)
        log.info('commit', commit)

    def tearDown(self):
        log.warn('delete test db')

        dv.shared_db.client.drop_database('test')


if __name__ == '__main__':
    unittest.main()
