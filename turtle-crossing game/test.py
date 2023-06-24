n, k = input().split()
cost_list = list(map(float, input().split()))
amount_charged = float(input())
sum1 = 0
for item in range(0, len(cost_list)):
    sum1 = sum1 + cost_list[item]

charged_share = amount_charged
actual_sum = sum1 - cost_list[int(k)]
actual_share = actual_sum/2
print(actual_share, " ", charged_share)
if actual_share == charged_share:
    print("Bon Appetit")
else:
    print(charged_share - actual_share)