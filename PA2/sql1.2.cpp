#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <sstream>
#include <iostream>
#include <openssl/md5.h>
#include <math.h>
using namespace std;
unsigned char result[MD5_DIGEST_LENGTH];

int main(int argc, char *argv[]) {
    	string tmp;
	char buffer[2];
	string longnum = "0";

    	for(long i = 0; i < 100; i++){
    		int start = ((int)longnum.size())-1;
		tmp = longnum[start];
		int digit = atoi(tmp.c_str());
		digit++;
		
		while(digit == 10){
			if(start == 0){
				longnum = "1" + longnum;
				longnum = longnum.size() -1;
			}
			digit = 0;
			sprintf(buffer,"%d", digit);
			longnum[start] = buffer[0];
			start--;
			tmp = longnum[start];
			digit = atoi(tmp.c_str());
			digit++;
		}
		
		sprintf(buffer,"%d",digit);
		//cout <<  buffer[0] << endl;
		longnum[start] = buffer[0];
		//printf(longnum.c_str());
		//char tmp [100];
		//sprintf(tmp,"%Lu",(unsigned long long)129581926211651571912466741651878684928);
		//cout << tmp << endl;
		//MD5((unsigned char*)longnum,1024, result);

		//cout << result << endl;
	}
	//char tmp[] = "";	
	//MD5((unsigned char*)tmp,strlen(tmp),result);
	//cout << result << endl;
    	return 0;
}
