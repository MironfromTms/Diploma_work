def QHofstadter(start_point):
    if start_point != [1, 1]:
        return
    seq = start_point[:]
    while True:
        try:
            answer = seq[-seq[-1]] + seq[-seq[-2]]
            seq.append(answer)
            yield answer
        except IndexError:
            return


number = 1
for i in QHofstadter([1, 1]):
    if i > 30:
        break
    print(i, end=' ')
    number += 1
