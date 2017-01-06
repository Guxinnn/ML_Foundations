import numpy as np def read_file(file):	x_d = []	y_d = []	f = open(file)	for line in f:		l = line.split()		x = [1.0] + [float(v) for v in l[:-1]]		x_d.append(x)		y_d.append(int(l[-1]))	f.close()	return np.array(x_d), np.array(y_d)def ridge_reg(x, y, lamda):	z = np.linalg.inv(np.dot(x.transpose(), x) + lamda * np.eye(x.shape[1]))	return np.dot(np.dot(z, x.transpose()), y)def err_func(x, y, w, n):	e = 0	for i in range(n):		if np.sign(np.dot(x[i], w)) != y[i]:			e += 1	return e / ndef quiz13(lmd = 10):	x_in, y_in = read_file("hw4_train.dat")	x_out, y_out = read_file("hw4_test.dat")	w_reg = ridge_reg(x_in, y_in, lmd)	e_in = err_func(x_in, y_in, w_reg, len(y_in))	e_out = err_func(x_out, y_out, w_reg, len(y_out))	print(e_in, e_out)def quiz14():	x_in, y_in = read_file("hw4_train.dat")	x_out, y_out = read_file("hw4_test.dat")		best_e_in = float("inf")	best_lmd = 0	w = 0	for lmd in range(2, -11, -1):		w_reg = ridge_reg(x_in, y_in, pow(10, lmd))		e_in = err_func(x_in, y_in, w_reg, len(y_in))		if e_in < best_e_in:			best_e_in = e_in			w = w_reg			best_lmd = lmd	e_out = err_func(x_out, y_out, w, len(y_out))	print(best_lmd, best_e_in, e_out)def quiz15():	x_in, y_in = read_file("hw4_train.dat")	x_out, y_out = read_file("hw4_test.dat")		best_e_out = float("inf")	best_lmd = 0	w = 0	for lmd in range(2, -11, -1):		w_reg = ridge_reg(x_in, y_in, pow(10, lmd))		e_out = err_func(x_out, y_out, w_reg, len(y_out))		if e_out < best_e_out:			best_e_out = e_out			w = w_reg			best_lmd = lmd	e_in = err_func(x_in, y_in, w, len(y_in))	print(best_lmd, best_e_out, e_in)def quiz16():	x_in, y_in = read_file("hw4_train.dat")	x_out, y_out = read_file("hw4_test.dat")	x_train = x_in[:120]	y_train = y_in[:120]	x_val = x_in[120:]	y_val = y_in[120:]	best_e_train = float("inf")	best_lmd = 0	w = 0	for lmd in range(2, -11, -1):		w_reg = ridge_reg(x_train, y_train, pow(10, lmd))		e_train = err_func(x_train, y_train, w_reg, len(y_train))		if e_train < best_e_train:			best_e_train = e_train			w = w_reg			best_lmd = lmd	e_out = err_func(x_out, y_out, w, len(y_out))	e_val = err_func(x_val, y_val, w, len(y_val))	print(best_lmd, best_e_train, e_val, e_out)def quiz17():	x_in, y_in = read_file("hw4_train.dat")	x_out, y_out = read_file("hw4_test.dat")	x_train = x_in[:120]	y_train = y_in[:120]	x_val = x_in[120:]	y_val = y_in[120:]	best_e_val = float("inf")	best_lmd = 0	w = 0	for lmd in range(2, -11, -1):		w_reg = ridge_reg(x_train, y_train, pow(10, lmd))		e_val = err_func(x_val, y_val, w_reg, len(y_val))		if e_val < best_e_val:			best_e_val = e_val			w = w_reg			best_lmd = lmd	e_train = err_func(x_train, y_train, w, len(y_train))	e_out = err_func(x_out, y_out, w, len(y_out))	print(best_lmd, e_train, best_e_val, e_out)def quiz18():	x_in, y_in = read_file("hw4_train.dat")	x_out, y_out = read_file("hw4_test.dat")	x_train = x_in[:120]	y_train = y_in[:120]	x_val = x_in[120:]	y_val = y_in[120:]	best_e_val = float("inf")	best_lmd = 0	for lmd in range(2, -11, -1):		w_reg = ridge_reg(x_train, y_train, pow(10, lmd))		e_val = err_func(x_val, y_val, w_reg, len(y_val))		if e_val < best_e_val:			best_e_val = e_val			best_lmd = lmd	quiz13(pow(10, best_lmd))def quiz1920(split = 40):	x_in, y_in = read_file("hw4_train.dat")	x_out, y_out = read_file("hw4_test.dat")	n_cv = split	best_e_cv = float("inf")	best_lmd = 0	for lmd in range(2, -11, -1):         e_cv = 0         for i in range(int(len(y_in) / n_cv)):             x_cv = x_in[n_cv * i: n_cv * (i + 1)]             y_cv = y_in[n_cv * i: n_cv * (i + 1)]             w_reg = ridge_reg(x_cv, y_cv, pow(10, lmd))             e_cv += err_func(x_cv, y_cv, w_reg, n_cv)         if e_cv < best_e_cv:             best_e_cv = e_cv             best_lmd = lmd                	w = ridge_reg(x_in, y_in, pow(10, best_lmd))	e_in = err_func(x_in, y_in, w, len(y_in))	e_out = err_func(x_out, y_out, w, len(y_out))	print(best_lmd, best_e_cv, e_in, e_out)def main():	# quiz13()	# quiz14()	# quiz15()	# quiz16()	# quiz17()	# quiz18()	quiz1920()if __name__ == '__main__':	main()