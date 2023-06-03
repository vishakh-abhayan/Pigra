import pynecone as pc

class PyconeConfig(pc.Config):
    pass

config = PyconeConfig(
    app_name="pycone",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)