from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]

    @classmethod
    def values(cls):
        return list(i.value for i in cls)

    @classmethod
    def mapping(cls):
        return dict((i.name, i.value) for i in cls)
    
class CurrencyEnum(BaseEnum):
    NGN = "NGN"
    EUR = "EUR"
    USD = "USD"
    GBP = "GBP"
    
class Settings(BaseEnum):
    COLOR = "theme"
    PARTNER = "partner"
    EMAIL = "email"
    TRADE_REF_PRICE = "trade_ref_price"
    PARTNER_REF_PRICE = "partner_ref_price"
    INVEST_REF_PRICE = "invest_ref_price"
    
class GlobalVariableType(BaseEnum):
    INT = "Int"
    STR = "Str"
    BOOL = "Bool"
    FLOAT = "Float"
    
class ProductType(BaseEnum):
    KGS = "Kgs"
    TRADE = "Trade"
    INVEST = "Invest"
    PARTNER = "Partner"
    