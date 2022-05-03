import joblib
import numpy as np
import json

scaler = joblib.load('model/scaler.sav')

model = joblib.load('model/finalized_model.sav')

miles = json.load(open('assets/miles.json'))


def get_predefined_record(record):
    record_keys = ["MktCoupons", "Quarter", "Miles", "ContiguousUSA", "NumTicketsOrdered",
                   "AA", "AS", "B6", "DL", "F9", "G4", "HA", "NK", "SY", "UA", "VX", "WN"]

    predefined_record = dict.fromkeys(record_keys, 0)

    loop_features = record_keys[:5]
    loop_features.remove("Miles")

    for key in loop_features:
        predefined_record[key] = record[key]

    predefined_record['Miles'] = miles[f"{record['Origin']}>{record['Dest']}"]
    predefined_record[record['AirlineCompany']] = 1

    return np.array(list(predefined_record.values())).reshape(1, -1)


def standarized(record):
    return scaler.transform(record)


def predict(record):
    return model.predict(record)


def pipe(record):
    result = record
    func_list = [get_predefined_record, standarized, predict]

    for fnc in func_list: result = fnc(result)

    return np.exp(result)
