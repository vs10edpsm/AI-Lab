from itertools import permutations

def solve_cryptarithm(words,result):
    letters = set(''.join(words) + result)
    letters = list(letters)

    if len(letters) > 10:
        print('Too many letters')
        return

    first_letters = set(word[0] for word in words + [result])

    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))

        if any(mapping[ch] == 0 for ch in first_letters):
            continue

        nums = [int("".join(str(mapping[c]) for c in word)) for word in words]
        res = int("".join(str(mapping[c]) for c in result))

        if sum(nums) == res:
            print('Solution:', mapping)
            print('Equation:', ' + '.join(map(str, nums)), '=', res)
            return 

    print('No Solution Found.')


solve_cryptarithm(["SEND","MORE"], "MONEY")
solve_cryptarithm(["CROSS","ROADS"], "DANGER")