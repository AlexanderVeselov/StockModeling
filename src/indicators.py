def lerp(a, b, t):
	return a * (1 - t) + b * t

def SMA(price_data, window_size):
	result = []
	inv_window_size = 1.0 / window_size
	for i in range(len(price_data)):
		sum = 0.0
		total_weight = 0.0
		for j in range(max(i - window_size + 1, 0), i + 1):
			sum += price_data[j]
			total_weight += 1.0
		result.append(sum / total_weight)

	return result

def EMA(price_data, hysteresis):
	result = [price_data[0]]
	for i in range(1, len(price_data)):
		ema = lerp(price_data[i], result[i - 1], hysteresis)
		result.append(ema)
	return result

def StochasticOscillator(price_data, window_size):
	result = []
	for i in range(len(price_data)):
		current_price = price_data[i]
		min_price = current_price
		max_price = current_price
		for j in range(max(i - window_size, 0), i):
			min_price = min(min_price, price_data[j])
			max_price = max(max_price, price_data[j])
		denom = max_price - min_price
		stochastic_osc_value = (current_price - min_price) / denom if denom > 0 else 0
		result.append(stochastic_osc_value)

	return result
