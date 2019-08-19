#https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

#solution 1
def get_median(counter, d):
    count = 0
    for i, c in enumerate(counter):
        count += c
        if count > d // 2:
            break
    if d % 2 == 1:
        return i * 2
    else:
        for j in range(i, -1, -1):
            count -= counter[j]
            if count < d // 2:
                break
        return i + j

def activityNotifications(expenditure, d):
    count = 0
    counter = [0] * 201
    for exp in expenditure[:d]:
        counter[exp] += 1
    
    for i in range(d, len(expenditure)):
        tail = expenditure[i]
        head = expenditure[i-d]
        median = get_median(counter, d)
        if tail >= median:
            count += 1

        counter[tail] += 1
        counter[head] -= 1
    
    return count


#solution 2
def activityNotifications(expenditure, d):
    count = 0
    trailing = expenditure[0:d]
    trailing.sort()
    days = expenditure[d:]
    for i in range(len(days)):
        median = trailing[(d-1)//2] if d%2 == 1 \
        else ((trailing[d//2] + trailing[d//2-1])) /2
        if days[i] >= 2 * median:
            count += 1
        delIdx = bisect.bisect_left(trailing, expenditure[i])
        trailing.pop(delIdx)
        bisect.insort(trailing, days[i])

    return count