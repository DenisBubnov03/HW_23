import functions

CMD_TO_FUNCTIONS = {
    'filter': functions.filter_query,
    'map': functions.map_query,
    'unique': functions.unique_query,
    'sort': functions.sort_query,
    'limit': functions.limit_query,
}

FILEE_NAME = 'data/apache_logs.txt'


def builder_query(cmd, param, data):
    if data is None:
        with open(FILEE_NAME) as file:
            prepared_data = list(map(lambda x: x.strip(), file))

    else:
        prepared_data = data

    return CMD_TO_FUNCTIONS[cmd](param=param, data=prepared_data)
