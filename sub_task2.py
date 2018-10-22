# import time

#Utilities start

class Container :

    def __init__(self, state, answer) :
        self.state = state
        self.answer = answer

def deep_copy(selected_index, pr) :
    return [pr[i] for i in range(len(pr)) if i != selected_index]

def hasher(arr) :
    return "".join(map(str, arr))

def is_present(cache, ar_a) :
    hashed_val = hasher(ar_a)

    if hashed_val not in cache:
        return False
    
    return True


def dp(cache, pr) :
    hashed_val = hasher(pr)

    if is_present(cache, pr) :
        return cache[hashed_val].answer

    if len(pr) == 1 :
        return  pr[0]
    
    answers = [-1]*len(pr)

    for i in range(len(pr)) :
        if i == 0 :
            answers[i] =  dp(cache, deep_copy(i, pr)) + (pr[i] * pr[i + 1])
        elif i == (len(pr) - 1) :
            answers[i] = dp(cache, deep_copy(i, pr)) + (pr[i] * pr[i - 1])
        else :
            answers[i] = dp(cache, deep_copy(i, pr)) + (pr[i] * pr[i + 1] * pr[i - 1])

    ans = max(answers)
    cache[hashed_val] = Container(pr, ans)

    return ans

#Utilities end

#code starts executing
_tc = int(input())


for cs in range(_tc) :
    n = int(input())
    prices = list(map(int, input().split()))
    cache = dict()
    # start_time = time.time()
    ans = dp(cache, prices)
    print("Case " + str(cs + 1) + ": " + str(ans))
    # print("--- %s seconds ---" % (time.time() - start_time))
