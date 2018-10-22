# import time

# Utilities start
def deep_copy(selected_index, pr) :
    return [pr[i] for i in range(len(pr)) if i != selected_index]

def brute_force(pr) :
    if len(pr) == 1 :
        return pr[0]
    
    answers = [-1]*len(pr)

    for i in range(len(pr)) :
        if i == 0 :
            answers[i] =  brute_force(deep_copy(i, pr)) + (pr[i] * pr[i + 1])
        elif i == (len(pr) - 1) :
            answers[i] = brute_force(deep_copy(i, pr)) + (pr[i] * pr[i - 1])
        else :
            answers[i] = brute_force(deep_copy(i, pr)) + (pr[i] * pr[i + 1] * pr[i - 1])

    return max(answers)

# Utilities end

#Code execution starts
_tc = int(input())

for cs in range(_tc) :
    n = int(input())
    prices = list(map(int, input().split()))
    # start_time = time.time()
    ans = (brute_force(prices))
    print("Case " + str(cs + 1) + ": " + str(ans))
    # print("--- %s seconds ---" % (time.time() - start_time))
