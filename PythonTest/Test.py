# Enter your code here. Read input from STDIN. Print output to STDOUT
import operator
n = int(raw_input())
line = raw_input()
words = line.split()
minimum_trade_size = int(words[0])
increament = int(words[1])
available_units = int(words[2])
total_order = 0
orders = {}
allocations = {}
for i in xrange(n):
    line = raw_input()
    words = line.split()
    portfolio_order = int(words[1])
    orders[words[0]] = portfolio_order
    allocations[words[0]] = 0
    total_order += portfolio_order
for k, v in sorted(orders.items(), key=operator.itemgetter(1)):
    proportion_allocation = int(float(orders[k]) / float(total_order) * float(available_units))
    if proportion_allocation < minimum_trade_size:
        if proportion_allocation > float(minimum_trade_size) / 2.0:
            if minimum_trade_size <= available_units:
                allocations[k] += minimum_trade_size
                available_units -= minimum_trade_size
                total_order -= minimum_trade_size
                orders[k] -= minimum_trade_size
            else:
                available_units -= orders[k]
                total_order -= orders[k]
    else:
        if proportion_allocation >= orders[k]:
            if orders[k] <= available_units:
                if total_order > available_units:
                    if available_units - orders[k] == ((available_units - orders[k] - minimum_trade_size) / increament) * increament + minimum_trade_size:
                        if orders[k] == ((orders[k] - minimum_trade_size) / increament) * increament + minimum_trade_size:
                            allocations[k] = orders[k]
                            total_order -= orders[k]
                            available_units -= orders[k]
                            orders[k] = 0
                        else:
                            total_order -= orders[k]
                    else:
                        total_order -= orders[k]
                else:
                    if orders[k] == ((orders[k] - minimum_trade_size) / increament) * increament + minimum_trade_size:
                        allocations[k] = orders[k]
                        total_order -= orders[k]
                        available_units -= orders[k]
                        orders[k] = 0
                    else:
                        total_order -= orders[k]
            else:
                if available_units == ((available_units - minimum_trade_size) / increament) * increament + minimum_trade_size:
                    allocations[k] = available_units
                    total_order -= available_units
                    available_units = 0
                    orders[k] -= available_units   
        else:
            if orders[k] <= available_units:
                if total_order > available_units:
                    if available_units - orders[k] == ((available_units - orders[k] - minimum_trade_size) / increament) * increament + minimum_trade_size:
                        if orders[k] == ((orders[k] - minimum_trade_size) / increament) * increament + minimum_trade_size:
                            allocations[k] += orders[k]
                            available_units -= orders[k]
                            total_order -= orders[k]
                            orders[k] = 0
                        else:
                            total_order -= orders[k]
                    else:
                        total_order -= orders[k]
                else:
                    if orders[k] == ((orders[k] - minimum_trade_size) / increament) * increament + minimum_trade_size:
                        allocations[k] += orders[k]
                        available_units -= orders[k]
                        total_order -= orders[k]
                        orders[k] = 0
                    else:
                        total_order -= orders[k]
            else:
                if available_units == ((available_units - minimum_trade_size) / increament) * increament + minimum_trade_size:
                    allocations[k] += available_units
                    available_units = 0
                    total_order -= available_units
                    orders[k] -= available_units

for k in sorted(allocations.keys()):
    print(k, allocations[k])
            
    