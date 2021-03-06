import meta_ultra.config as config
from meta_ultra.utils import *
from meta_ultra.modules import *


class DiamondModule( Module):
	def __init__(self, **kwargs):
		super(DiamondModule, self).__init__(**kwargs)		
		

	def buildConf(self, confBuilder):
		diamond = confBuilder.addModule(self.moduleName().upper())
		if not diamond:
			return
		
		diamond.add_field('EXC',
				  UserChoice('Diamond',
					     self.tools,
					     new=lambda :self.askUserForTool('diamond')
				  ))

	@classmethod
	def worksForDataType(ctype, dataType):
		dataType = DataType.asDataType(dataType)
		allowed = [ DataType.WGS_DNA_SEQ_SINGLE_END, DataType.WGS_DNA_SEQ_PAIRED_END]
		return dataType in allowed
		
	@staticmethod
	def moduleName():
		return 'diamond'

		
modules.append(DiamondModule)
