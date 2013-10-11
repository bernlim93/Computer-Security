#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sstream>
#include <iostream>
#include <openssl/md5.h>
using namespace std;
unsigned char result[MD5_DIGEST_LENGTH];

int main(int argc, char *argv[]) {
    
    for(long i = 3000000000000000; i <3000000000000010; i++){
    		char tmp [100];
		sprintf(tmp,"%Lu",(unsigned long long)129581926211651571912466741651878684928);
		cout << tmp << endl;
		MD5((unsigned char*)tmp,strlen(tmp), result);
		cout << result << endl;
	}
	char tmp[] = "";	
	MD5((unsigned char*)tmp,strlen(tmp),result);
	cout << result << endl;
    return 0;
}
