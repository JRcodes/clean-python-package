from {{cookiecutter.project_name.lower().replace('-', '_')}} import common
from logzero import logger


@common.newrelic_wrapper
def lambda_handler(event, context = None):


	raise NotImplementedError