from load_and_dump import read_in, data_exists, dump_data, get_data, write_submission
from score import get_score

def sort_books(scores, book_ids):
    return sorted(book_ids, lambda book_id: scores[book_id])

def sort_libs(scores, libs):
    return sorted(libs, lambda lib: sum([scores[book] for book in lib['books']]))

def transform_format(data):
    output = []

    counter = 0
    for lib in data['libs']:
        output.append((counter, lib['books']))
        counter += 1

    return output

if __name__ == "__main__":
    filename = 'a_example'
    # filename = 'b_read_on'
    # filename = 'c_incunabula'
    # filename = 'd_tough_choices'
    # filename = 'e_so_many_books'
    # filename = 'f_libraries_of_the_world'
    algorithm = 'hc'

    data = read_in(filename)

    output = transform_format(data)
    score = get_score(output, data)
    print(score)

    # write_submission(filename, output, mod='random')

    # if not data_exists(filename, algorithm) or algorithm == 'init':
    #     # TODO DOE HIER INIT ALGORITME
    #     print('Running initialisation algorithm...')
    #     init_iets = [None]
    #
    #     print('Dumping data and writing submission file...')
    #     dump_data(filename, init_iets, mod=algorithm)
    #     write_submission(filename, init_iets, mod=algorithm)
    # else:
    #     print('Data loading!')
    #     init_iets = get_data(filename, mod=algorithm)
    #
    # # TODO DOE HIER HILLCLIMBER OFZO
    # print('Running hillclimber...')
    # outcome_hc = [None]
    #
    # print('Dumping data and writing submission file...')
    # dump_data(filename, outcome_hc, mod='hc')
    # write_submission(filename, outcome_hc, mod='hc')
