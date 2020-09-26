#Name: Esther Tan
#Crytography Project- RSA Cracker
#Date: 9/13/2019


#isPrime function
#pre:  an integer num is assigned to the function
#post: if num is prime then the function will return true
#usage: isNumberPrime = isPrime(2);
def isPrime(num):

	i = 2;
	while i < 10:
		if((num % i == 0) and (num != i)):
			return 0;
		i = i + 1;
	
	return 1;

	
#getPrivateKey function
#pre:  two integers e and phiN are assigned 
#post: returns the value of d such that e*d % phiN is 1
#usage: d = getPrivateKey(7, 20);
def getPrivateKey(e, phiN):
	d = 1
	while d <= phiN:
		if((e*d) % phiN == 1):
			return d;
		d = d + 1;

		
#rsaEncrypt function
#pre:  three integers plaintext, e and n are assigned 
#post: returns the value of C (ciphertext) 
#usage: C = rsaEncrypt(5, 7, 33);
def rsaEncrypt(plaintext, e, n):
	return ((plaintext**e) % n);

	
	
#rsaDecrypt function
#pre:  three integers ciphertext, d and n are assigned 
#post: returns the value of P (plaintext) 
#usage: C = rsaEncrypt(5, 7, 33);
def rsaDecrypt(ciphertext, d, n):
	return ((ciphertext**d) % n);

	
	
#crackRsa function
#pre:  two integers e and n
#post: factors n into p and q,
#      finds the value of phiN
#      uses phiN and e to get the value of d
#      returns d 
#usage: d = crackRsa(7,33);
def crackRsa(e,n):
	divisor = 2;
	p = q = 0;
	while n > 1:
		if( (isPrime(divisor)) and (n % divisor == 0) ):
			n = n / divisor;
			if(not p):
				p = divisor;
			else:
				q = divisor;
		else:
			divisor = divisor + 1;
	
	phiN = (p - 1)*(q -1);
	return (getPrivateKey(e, phiN));
	
	
			
#main function
def main():
	#Test Case 1
	
	d_Expected = 3;
	plaintext_Expected = 5;
	ciphertext_Expected = 14;
	e = 7;
	n = 33;
	d_Actual = crackRsa(e,n);
	print ""
	print "*********************** Test Case 1***********************"
	print "d (expected - actual):         " ,d_Expected, " " ,d_Actual;
	

	ciphertext_Actual = rsaEncrypt(plaintext_Expected, e , n);
	print "ciphertext (expected - actual):" ,ciphertext_Expected, " " ,ciphertext_Actual;
	
	plaintext_Actual = rsaDecrypt(ciphertext_Actual, d_Actual , n);
	print "plaintext (expected - actual): " ,plaintext_Expected, " " ,plaintext_Actual;
	
	#end of Test 1 
	
	#Test 2 
	
	d_Expected = 27;
	plaintext_Expected = 9;
	ciphertext_Expected = 14;
	e = 3;
	n = 55;
	d_Actual = crackRsa(e,n);
	print ""
	print "*********************** Test Case 2***********************"
	print "d (expected - actual):         " ,d_Expected, " " ,d_Actual;
	

	ciphertext_Actual = rsaEncrypt(plaintext_Expected, e , n);
	print "ciphertext (expected - actual):" ,ciphertext_Expected, " " ,ciphertext_Actual;
	
	plaintext_Actual = rsaDecrypt(ciphertext_Actual, d_Actual , n);
	print "plaintext (expected - actual): " ,plaintext_Expected, " " ,plaintext_Actual;
	
	#end of Test 2 
	
	#Test 3 
	
	d_Expected = 53;
	plaintext_Expected = 8;
	ciphertext_Expected = 57;
	e = 17;
	n = 77;
	d_Actual = crackRsa(e,n);
	print ""
	print "*********************** Test Case 3***********************"
	print "d (expected - actual):         " ,d_Expected, " " ,d_Actual;
	

	ciphertext_Actual = rsaEncrypt(plaintext_Expected, e , n);
	print "ciphertext (expected - actual):" ,ciphertext_Expected, " " ,ciphertext_Actual;
	
	plaintext_Actual = rsaDecrypt(ciphertext_Actual, d_Actual , n);
	print "plaintext (expected - actual): " ,plaintext_Expected, " " ,plaintext_Actual;
	
	#end of Test 3 
	
	#Test 4 
	
	d_Expected = 11;
	plaintext_Expected = 7;
	ciphertext_Expected = 106;
	e = 11;
	n = 143;
	d_Actual = crackRsa(e,n);
	print ""
	print "*********************** Test Case 4***********************"
	print "d (expected - actual):         " ,d_Expected, " " ,d_Actual;
	

	ciphertext_Actual = rsaEncrypt(plaintext_Expected, e , n);
	print "ciphertext (expected - actual):" ,ciphertext_Expected, " " ,ciphertext_Actual;
	
	plaintext_Actual = rsaDecrypt(ciphertext_Actual, d_Actual , n);
	print "plaintext (expected - actual): " ,plaintext_Expected, " " ,plaintext_Actual;
	
	#end of Test 4
	
	#Test 3 
	
	d_Expected = 343;
	plaintext_Expected = 2;
	ciphertext_Expected = 128;
	e = 7;
	n = 527;
	d_Actual = crackRsa(e,n);
	print ""
	print "*********************** Test Case 5***********************"
	print "d (expected - actual):         " ,d_Expected, " " ,d_Actual;
	

	ciphertext_Actual = rsaEncrypt(plaintext_Expected, e , n);
	print "ciphertext (expected - actual):" ,ciphertext_Expected, " " ,ciphertext_Actual;
	
	plaintext_Actual = rsaDecrypt(ciphertext_Actual, d_Actual , n);
	print "plaintext (expected - actual): " ,plaintext_Expected, " " ,plaintext_Actual;
	print "";
	
	#end of Test 3 
	
	

if __name__ == "__main__":
    main()