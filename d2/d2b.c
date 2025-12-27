#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#define MAX_LINE_LENGTH 1024
#define MAX_RANGE_LENGTH 32

bool is_code_invalid(long code) {
	char codestr[15];
	char target[15];
	char chunk[15];
	sprintf(codestr, "%li", code);

	int code_len = strlen(codestr);
	
	for (int num_chars=1; num_chars<=code_len/2; num_chars++) {
		if ((code_len % num_chars) == 0) {
			// generate target code
			target[0]='\0';
			// get substring chunk to repeat
			strcpy(chunk, codestr);
			chunk[num_chars]='\0';
			// create target from repeated chunk
			for (int n=0; n<code_len/num_chars; n++) {
				strcat(target, chunk); 
			}
			// test if invalid
			if (strcmp(codestr, target) == 0) {
				return true;
			}
		}
	}
	return false;
}

int main(void) {
	char buffer[MAX_LINE_LENGTH];
	
	int invalid_count = 0;
	long invalid_sum = 0;

	long start, stop;
	
	scanf("%s", buffer);
	// char range[MAX_RANGE_LENGTH];
	char *range = strtok(buffer, ",");
	// loop over input
	while (range != NULL) {
		sscanf(range, "%li-%li", &start, &stop);
		// printf("%li-%li ", start, stop);
		for (long code = start; code <= stop; code++) {
			if (is_code_invalid(code)) {
				// printf("%li ", code);
				invalid_count++;
				invalid_sum = invalid_sum + code;
			}
		}
		// printf("\n");
		range = strtok(NULL, ",");
	}
	printf("%i invalid codes summing to %li.\n", invalid_count, invalid_sum);
}

