
import math
import time

def find_name():
	find_na = "123"
	name_list = [{"name": "12", "tel": "12"}, {"name": "123", "tel": "123"}, {"name": "1234", "tel": "1234"}]
	for ss in name_list:
		if ss["name"] == find_na:
			print("%s \t %s \t" %(ss["name"], 
									ss["tel"]))
			break
	else:
		print("...")


def cal():
	a = -9.92*pow(10, -8)
	b = 0.1005
	c = -12717
	# a=-3.467*pow(10, -5)
	# b=0.5423
	# c=-848.23
	# 1762.798408191077; 13878.966806692106
	mid = pow(b, 2)-4*a*c
	if mid >=0:
		x1 = (-b+pow(mid, 0.5))/(2*a)
		x2 = (-b-pow(mid, 0.5))/(2*a)
		print(x1,"\n", x2)


def cal_smoke():
	value = []
	for x in range(1, 1000):
		for y in range(1, 20):
			c_x = 0.04 * pow((1 + 0.0001 * x), -0.5) # 扩散系数，x
			c_y = c_x  # 扩散系数，y
			c_z = 0.016 * pow((1 + 0.0001 * x), -1) # 扩散系数，z
			Qm = 5000 # 泄漏源速度；
			pi = math.pi
			u = 2 # wind speed;
			Hr = 2 # height
			con = Qm/(pi * c_y * c_z * u)
			exp = -0.5 * pow(y/c_y, 2) - 0.5 * pow(Hr/c_z, 2)
			time.sleep(1)
			print(con, exp)
			C = con * pow(math.e, exp)
			print(C)
			if C in range(6500, 6700):
				value.append([x, y, C])
	print(value)




cal_smoke()
