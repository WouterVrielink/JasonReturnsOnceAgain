from load_and_dump import read_in, data_exists, dump_data, get_data, write_submission

if __name__ == "__main__":
    filename = 'a_example.txt'

    data = read_in(filename)

    if not data_exists(filename):
        # TODO DOE HIER INIT ALGORITME
        init_iets = None

        dump_data(init_iets, filename)
    else:
        init_iets = get_data(filename)
        print('Data loaded!')

    # TODO DOE HIER HILLCLIMBER OFZO
    outcome_hc = None

    dump_data(outcome_hc, mod='hc')
    write_submission(filename, outcome_hc)
