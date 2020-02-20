from load_and_dump import read_in, data_exists, dump_data, get_data, write_submission

if __name__ == "__main__":
    filename = 'a_example'
    algorithm = 'hc'

    # data = read_in(filename)

    if not data_exists(filename, algorithm) or algorithm == 'init':
        # TODO DOE HIER INIT ALGORITME
        print('Running initialisation algorithm...')
        init_iets = [None]

        print('Dumping data and writing submission file...')
        dump_data(filename, init_iets, mod=algorithm)
        write_submission(filename, init_iets, mod=algorithm)
    else:
        print('Data loading!')
        init_iets = get_data(filename, mod=algorithm)

    # TODO DOE HIER HILLCLIMBER OFZO
    print('Running hillclimber...')
    outcome_hc = [None]

    print('Dumping data and writing submission file...')
    dump_data(filename, outcome_hc, mod='hc')
    write_submission(filename, outcome_hc, mod='hc')
