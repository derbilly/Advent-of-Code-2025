#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
	char lines[9][256]; // Buffer to store each line
	// Read until EOF (End of File)
	int num_lines = 0;
	while (fgets(lines[num_lines], sizeof(lines[num_lines]), stdin)) {
		lines[num_lines][strcspn(lines[num_lines], "\n")] = '\0';
		num_lines++;
	}
	for (int n=0; n<num_lines; n++) {
		printf("%s\n", lines[n]);
	}
	char operations[256];
	strcpy(operations, lines[num_lines-1]);
	printf("operations = <%s>\n", operations);

	int length = strlen(operations);
	printf("length is %i\n", length);

	

	return 0;
}

