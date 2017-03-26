from operation import Operation


class Adjust(Operation):
    
    def __init__(self, observation):
        Operation.__init__(self)
        
        self.observation = observation
        pass
    
    @staticmethod
    def validate_parameter(param_dict=None):
        """
        this method will validate each input parameter. the validation includes type check and range check
        all appropriate errors shall be thrown within the implementation
        :return: boolean indicating success/failure
        """
        validated = True
        error = []
        if param_dict is None or not isinstance(param_dict, dict):
            error.append('No Valid Dictionary Provided')
            return ';'.join([str(x) for x in error])
        
        if "observation" not in param_dict:
            validated = False
            error.append('Missing Observation Value in Dictionary')
        
        if "height" in param_dict:
            height = param_dict['height']
            try:
                height = float(height)
            except ValueError:
                error.append("Height Value Must Be A Floating Number")
                validated = False
            if height < 0:
                error.append("Height Value Must Be A Positive Floating Number")
                validated = False
                
        if "pressure" in param_dict:
            pressure = param_dict['pressure']
            try:
                pressure = int(pressure)
            except ValueError:
                raise ValueError("Pressure Value Must Be A Integer")
            if pressure < 100:
                raise ValueError("Pressure Value Is Under Threshold of 100 mbar")
        
        if "temperature" not in param_dict:
            raise ValueError("Missing Temperature Value in Dictionary")
        
        if "horizon" not in param_dict:
            raise ValueError("Missing Horizon Value in Dictionary")
        
        #height = param_dict['height']
        #temperature = param_dict['temperature']
        #pressure = param_dict['pressure']
        #horizon = param_dict['horizon']
        if validated:
            return True
        else:
            return ';'.join([str(x) for x in error])
        
    
    def perform(self):
        """
        this method will perform the calculation for designated operation
        and attach the result as a key value pair to the original input dictionary
        :return: original dictionary + result key-value pair
        """
        return {}