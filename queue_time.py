def queue_time(customers, n):
    # TODO get customers count
    # TODO loop trough till/counter for each customer
    time_count = {}
    customer_count = len(customers)
    pelanggan = customers

    if customer_count < 1:
        return 0
    else:
        finish_count = False
        kaunter = {}
        for ix in range(n):
            kaunter[ix] = 0
            time_count[ix] = 0

        while finish_count == False:

            for ix in range(n):
                # check if kaunter is 0
                if kaunter[ix] == 0:
                    # get new customer if available
                    if len(pelanggan) > 0:
                        kaunter[ix] = pelanggan.pop(0)
                        # print(kaunter)
                else:
                    # reduce count

                    kaunter[ix] = kaunter[ix] - 1
                    time_count[ix] = time_count[ix] + 1
                    if kaunter[ix] == 0:
                        if len(pelanggan) > 0:
                            kaunter[ix] = pelanggan.pop(0)
                    # print(time_count)
            # print(kaunter)

            if sum(kaunter.values()) == 0 and len(pelanggan) == 0:
                # no more customer to count
                finish_count = True

    # return True
    return max(time_count.values())

    # return customers


def process_queue():

    return True


# print(queue_time([], 1))  # 0
# print(queue_time([5], 1))  # 5
# print(queue_time([2], 5))  # 2
# print(queue_time([1, 2, 3, 4, 5], 1))  # 15
# print(queue_time([1, 2, 3, 4, 5], 100))  # 5
# print(queue_time([2, 2, 3, 3, 4, 4], 2))  # 9

# Wrong answer for customers = [32, 50, 8, 45, 12, 2, 45, 31, 31, 30, 9, 11, 21, 25, 2, 36] and n = 6: 84 should equal 86
print(queue_time([32, 50, 8, 45, 12, 2, 45, 31,
      31, 30, 9, 11, 21, 25, 2, 36], 6))  # 86


def queue_time(customers, n):
    l = [0]*n
    for i in customers:
        l[l.index(min(l))] += i
    return max(l)
