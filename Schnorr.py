#!/usr/bin/python
# -*- coding: utf-8 -*-

import bint
import sys
import random




def xgcd(a, b):
	
	if a == bint.bint(0):
		return 0, 1, b

	if b == bint.bint(0):
		return 1, 0, a

	px = bint.bint(0)
	ppx = bint.bint(1)
	py = bint.bint(1)
	ppy = bint.bint(0)

	while b > bint.bint(0):
		q = a / b
		a, b = b, a % b
		x = ppx - q * px
		y = ppy - q * py
		ppx, px = px, x
		ppy, py = py, y

	return ppx, ppy, a


def inverse(a, p):
	x, y, g = xgcd(a, p)

	return (x % p + p) % p


def gen_keys():
	# generiruem p q and g
	f = open("p.txt")

	p = int(f.read())

	f.close()

	f = open("q.txt")

	q = int(f.read())

	f.close()

	f = open("g.txt")

	g = int(f.read())

	f.close()



	w = random.randint(2, q - 1) # w -sluchainoe chislo 1 < w < q-1

	r = random.randint(2, q - 1) # r - sluchainoe chislo 1 < r < q-1

	p = bint.bint(str(p))
	q = bint.bint(str(q))
	g = bint.bint(str(g))
	w = bint.bint(str(w))
	r = bint.bint(str(r))

	inv_g = inverse(g, p) # nahodim g^-1

	y = p.powmod(inv_g, w, p) # y = (g^-1)^w mod p

	x = p.powmod(g, r, p) # x = g^r mod p

	print "\nКлючи сгенерированы:\n"

	print "x = ", x, "отсылается Виктору\n"

	return p, q, g, w, r, y, x

# algoritm proverki podlinnosti
def schnorr(p, q, g, w, r, y, x):
	e = random.randint(0, pow(2, 20) - 1)   #vibiraetsya chslo e takoe chto 0< e < 2^20 -1 

	e = bint.bint(str(e))

	print "e = ", e, "отсылается Пегги\n"

	s = (r + w * e) % q # s = (r+ w*e) mod q

	print "s = ", s, "отсылается Виктору\n"

	m1 = p.powmod(g, s, p) # m1=g^s mod p
	m2 = p.powmod(y, e, p) # m2=y^e mod p

	m = (m1 * m2) % p # m = m1*m2 mod p

	if m == x: 
		print "Виктор удостоверился в подлинности x = ", m, "\n"
	else:
		print "Подлинность не установлена\n"


def main():
	p, q, g, w, r, y, x = gen_keys()

	schnorr(p, q, g, w, r, y, x)

main()