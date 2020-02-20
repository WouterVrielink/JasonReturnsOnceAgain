
def get_score(submission, data):
    score = 0
    signup = 0
    for lib, books in submission:
        T = data['libs'][lib]['T']
        B = data['B']
        M = data['libs'][lib]['M']

        no_books = (B - T) * M  - signup - 1
        for i in range(min(no_books, len(books))):
            score += data['points'][books[i]]

        signup += T
    return score
