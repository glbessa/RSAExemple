import random
import base64

def primos(min, max):
	for i in range(min, max):
		if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
			pass
		else:
			yield i
			# print(i)

def mdc(n1, n2):
	while n2:
		n2, n1 = n1 % n2, n2
	return n1

def chaves_privadas(n, phi):
	for i in range(2, phi):
		if mdc(n, i) == 1 and mdc(phi, i) == 1:
			yield i

def chaves_publicas(phi, chave_privada, maximo):
	for i in range(phi + 1, phi + maximo):
		if i * chave_privada % phi == 1:
			yield i

def criptografar_frase(chave, n, frase):
	frase_criptografada = ''
	for letra in frase:
		letra_ascii = ord(letra)
		letra_criptografada_ascii = letra_ascii ** chave % n
		print(f'{letra_ascii} {letra_criptografada_ascii}')
		frase_criptografada += chr(letra_criptografada_ascii)
	return frase_criptografada

def descriptografar_frase(chave, n, frase_criptografada):
	frase_descriptografada = '' 
	for letra_criptografada in frase_criptografada:
		letra_criptografada_ascii = ord(letra_criptografada)
		letra_ascii = letra_criptografada_ascii ** chave % n
		print(f'{letra_criptografada_ascii} {letra_ascii}')
		frase_descriptografada += chr(letra_ascii)
	return frase_descriptografada

minimo = 10
maximo = 200

primos_gerados = [i for i in primos(minimo, maximo)]

primo1 = random.choice(primos_gerados)
primos_gerados.remove(primo1)
primo2 = random.choice(primos_gerados)

print(f'Primo 1 (p): {primo1}')
print(f'Primo 2 (q): {primo2}')

n = primo1 * primo2
print(f'n: {n}')

phi = (primo1 - 1) * (primo2 - 1)
print(f'phi: {phi}')

chaves_pri_geradas = [i for i in chaves_privadas(n, phi)]
# print(chaves_pri_geradas)
chave_privada = random.choice(chaves_pri_geradas)
print(f'Chave privada: {chave_privada}')

maximo_pub = 100000
chaves_pub_geradas = []
while chaves_pub_geradas == []:
	chaves_pub_geradas = [i for i in  chaves_publicas(phi, chave_privada, maximo_pub)]
	maximo_pub *= 10
#print(chaves_pub_geradas)
chave_publica = random.choice(chaves_pub_geradas)
print(f'Chave publica: {chave_publica}')

frase = 'Testando exemplo de criptografia RSA'
print(frase)

frase_criptografada = criptografar_frase(chave_publica, n, frase)
#print(frase_criptografada.encode('ascii'))
print(frase_criptografada.encode('utf-16', 'surrogatepass'))
#print(frase_criptografada.encode('utf-8').hex())

print()

frase_descriptografada = descriptografar_frase(chave_privada, n, frase_criptografada)
#print(frase_descriptografada.encode('utf-16', 'surrogatepass').decode('utf-16'))
print(frase_descriptografada)