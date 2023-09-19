def calculate_present_value(t_values, c_values, i):
    n = len(t_values)
    pv = 0
    for t, c in zip(t_values, c_values):
        pv += c / (1 + i) ** t
    return pv

# 情况1: 计算 t_k = k, C_{t_k} = 1
t_values_1 = [k for k in range(1, 101)]
c_values_1 = [1] * 100
i_1 = 0.05
pv_1 = calculate_present_value(t_values_1, c_values_1, i_1)
print(f"情况1: PV = {pv_1}")

# 情况2: 计算 t_k = C_{t_k} = k-1
t_values_2 = [k - 1 for k in range(1, 101)]
c_values_2 = [k - 1 for k in range(1, 101)]
i_2 = 0.05
pv_2 = calculate_present_value(t_values_2, c_values_2, i_2)
print(f"情况2: PV = {pv_2}")

# 情况3: 计算 t_k = k-1, C_{t_k} = k * (1.05^k)
t_values_3 = [k - 1 for k in range(1, 101)]
c_values_3 = [k * (1.05 ** k) for k in range(1, 101)]
i_3 = 0.05
pv_3 = calculate_present_value(t_values_3, c_values_3, i_3)
print(f"情况3: PV = {pv_3}")

# 情况4: 计算 t_k = k, C_{t_k} = k * (1.06^k)
t_values_4 = [k for k in range(1, 101)]
c_values_4 = [k * (1.06 ** k) for k in range(1, 101)]
i_4 = 0.05
pv_4 = calculate_present_value(t_values_4, c_values_4, i_4)
print(f"情况4: PV = {pv_4}")
