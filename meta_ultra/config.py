import os.path
import os
from tinydb import TinyDB


lib_root = os.path.dirname(__file__)

ref_file = os.path.join( lib_root, 'references')
pipeline_dir = os.path.join( lib_root, 'pipelines/')
snake_file = os.path.join( pipeline_dir, 'all.snkmk')
cluster_wrapper = os.path.join( lib_root, 'cluster_wrapper_script.py')

mu_dir = '.mu'
mu_db = os.path.join(mu_dir,'mudb')

def get_db(dir='.'):
    dir = os.path.abspath(dir)
    if mu_dir in os.listdir(dir):
        return TinyDB( os.path.join(dir,mu_db))
    else:
        # recurse up
        up = dirname(dir)
        if up == dir:
            # top, fail
            sys.stderr.write('No MetaUltra database found. Exiting.\n')
            sys.exit(1)
        else:
            return get_db(up)

db_module_table = get_db().table('module_table')
db_sample_table = get_db().table('sample_table')
db_data_table = get_db().table('data_table')
db_experiment_table = get_db().table('experiment_table')
db_conf_table = get_db().table('conf_table')
db_result_table = get_db().table('result_table')


def canon_tool(toolName):
    return toolName.lower()


class DataType(Enum):
    DNA_SEQ_SINGLE_END='DNA_SEQ_SINGLE_END'
    DNA_SEQ_PAIRED_END='DNA_SEQ_PAIRED_END'
