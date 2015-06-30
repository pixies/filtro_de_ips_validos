#Ler o arquivo
def ler_arquivo(arquivo):
    arquivo = open(arquivo, 'r')
    return arquivo






def valida_ip(ip_testado):
	ip = ip_testado.split('.')
	k=0
	if int(ip[0])>0 and int(ip[0])<256:
		k+=1
	if int(ip[1])>=0 and int(ip[1])<256:
		k+=1
	if int(ip[2])>=0 and int(ip[2])<256:
		k+=1
	if int(ip[3])>0 and int(ip[3])<255:
		k+=1
	if k==4:
		return True
	else:
		return False

	
def criar_novo_arquivo():
	nova_lista = open('nova_lista.txt','a')
	arq = ler_arquivo('lista_ips.txt')
	#print 'imprimindo ',arq.read()
	for ip in arq.readlines():
		if valida_ip(str(ip)):
			nova_lista.write(str(ip))
	nova_lista.close()

print criar_novo_arquivo()
#ler_lisnhas_do_arquivo()

#print valida_ip('257.32.4.5')