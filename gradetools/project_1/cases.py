from models.project_1 import PhoneManufacturingModel

INPUT_CASES = [
    dict(
        n_phones=100000,
        n_machines=5,
        n_life=10,
        price_phone=500,
        price_scrap=50000,
        d_0=100000,
        g_d=0.2,
        interest=0.05
    ),
    dict(
        n_phones=1000000,
        n_machines=3,
        n_life=5,
        price_phone=200,
        price_scrap=30000,
        d_0=1000000,
        g_d=0.25,
        interest=0.04
    ),
    dict(
        n_phones=10000,
        n_machines=1,
        n_life=18,
        price_phone=2000,
        price_scrap=300000,
        d_0=100000,
        g_d=0.15,
        interest=0.06
    ),
    dict(
        n_phones=1000,
        n_machines=1,
        n_life=2,
        price_phone=20,
        price_scrap=300000,
        d_0=100000,
        g_d=0.1,
        interest=0.1
    )
]

def output_dict_from_input_dict(input_dict):
    model = PhoneManufacturingModel(**input_dict)
    correct_values = dict(
        pv=model.pv,
        cash_flows=model.cash_flows
    )
    return correct_values

OUTPUT_CASES = [output_dict_from_input_dict(input_dict) for input_dict in INPUT_CASES]