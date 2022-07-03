from uuid import uuid4
from ruamel.yaml import YAML

class AgentConfig:

    source_name = None
    interval = None
    cpu = False
    memory = False
    host_identificator = 0
    agent_yaml = YAML()
    config = {}

    def __init__(self, configuration_file):
        self.__config_file = configuration_file
        self.parse_config()

    def load_config_from_yaml(self) ->dict:
        with open(self.__config_file, "r") as f:
            return self.agent_yaml.load(f)

    def parse_config(self):
        class_variables = AgentConfig.__dict__.keys()
        self.config = self.load_config_from_yaml()
        for key, value in self.config.items():
            if key in class_variables:
                value = self.transform_values(key, value)
                setattr(AgentConfig, key, value)

    def transform_values(self, key, value):
        transformation_mapper = {
            "interval": self.transform_interval,
            "host_identificator": self.transform_identificator
        }

        transformator = transformation_mapper.get(key, None)
        if transformator:
            return transformator(value)
        else:
            return value

    def transform_interval(self, interval: str) -> int:
        interval_mapper = {
            "s": 1,
            "m": 60,
            "h": 3600
        }
        interval = int(interval[:-1]) * interval_mapper[interval[-1]]
        return interval

        '''
        seconds_in_minute = 60
        seconds_in_hour = 3600
        time_ind = interval[-1]

        if time_ind == "s":
            return int(interval[:-1])
        else:
            return int(interval[:-1]) * seconds_in_minute if time_ind == "m" else int(interval[:-1]) * seconds_in_hour
        '''

    def transform_identificator(self, host_identificator):
        if host_identificator == 0:
            host_identificator = str(uuid4())
            self.load_config_to_yaml("host_identificator", host_identificator)
            return host_identificator

    def load_config_to_yaml(self, key, value):
        self.config[key] = value
        with open(self.__config_file, "w") as f:
            self.agent_yaml.dump(self.config, f)



        # TODO write transform_interval (suffix <s>, suffix <m>, suffix <h>)
        # TODO write transform_identificator (if value: 0 -> uuid.uuid4)
        # TODO write load_config_to_yaml to save config with <host_identificator>

ag = AgentConfig("./config/agent.yaml")
