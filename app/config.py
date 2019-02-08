class BaseConfig(object):
	SECRET_KEY = 'test123'

class Development(BaseConfig):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SQLALCHEMY_DATABASE_URI = 'postgres://ramrios_candidate:ramrios_candidate@localhost/ramrios_candidate'

config_map = {
	'development': Development,
}
