    
class UserModelUtils:
    """
    Class to hold methods to handle User Object details.
    """
    REGNAL_DICT = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI", 
        7: "VII",
        8: "VIII",
        9: "IX",
        10: "X",
        11: "XI",
        12: "XII",
        13: "XIII",
        14: "XIV",
        15: "XV",
        16: "XVI",
        17: "XVII",
        18: "XVIII",
        19: "XIX",
        20: "XX",
        21: "XXI"
    }

    @classmethod
    def translate_regnal_number(cls, regnal_number:int=None):
        if regnal_number in cls.REGNAL_DICT.keys():
            return cls.REGNAL_DICT[regnal_number]
        else:
            resp = {
                "error": "Regnal number not supported."
            }
            return resp