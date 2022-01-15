import pandas as pd
from datetime import date, datetime

class finder:
    def find_element_dframe(dframe:pd.DataFrame,divisoes:dict):
        elements_key = len(divisoes)
        result_find:pd.DataFrame
        result_find = dframe

        for key, value in divisoes.items():
            mask = ((result_find[key] == value))
            result_find = result_find[mask]

        print(result_find[['location','dt_mr']].to_markdown())

        now = datetime.now()
        datetime_formated = now.strftime("%d%m%Y_%I%M%S_%p")

        result_find.to_csv(f"./out/output_search_{datetime_formated}.csv", sep=';', decimal=",", index=False, encoding="utf-8-sig")


dframe = pd.read_csv("./data/base.csv", low_memory=False, sep=";", decimal=".")

busca = {
    'no_div_3':'1435'
}
finder.find_element_dframe(dframe=dframe, divisoes=busca)