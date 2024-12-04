#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef int bool;
bool true = 1;
bool false = 0;

bool is_num(char c) {
	if ((c < '0') | (c > '9')) {
		return 0;
	}
	return 1;
}

int char_to_int(char c) {
	return c - '0';
}

bool parse_num(char* buffer, int* total, int* index) {
	*total = 0;
	int original_index = *index;
	while (true) {
		if (is_num(buffer[*index])) {
			*total = *total * 10 + char_to_int(buffer[*index]);
			*index += 1;
		}
		else if (*index == original_index) {return 0;}
		else {return 1;}
	}
}

bool bufcmp(char* buf1, char* buf2) {
	int index = 0;
	while (true) {
		if ((buf1[index] == 0) | (buf2[index] == 0)) {return true;}
		if (buf1[index] != buf2[index]) {return false;}
		index++;
	}
}

int total_count = 0;

/// returns the index the buffer should advance
int check_buf(char* buf, bool* should_mul) {
	if (bufcmp("do()", buf)) {
		*should_mul = true;
		return 4;
	}
	if (bufcmp("don't()", buf)) {
		*should_mul = false;
		return 7;
	}
	if (!*should_mul) {return 1;}
	if (!bufcmp("mul(", buf)) {return 1;}
	int sum1, sum2;
	int index = 4;
	if (!parse_num(buf, &sum1, &index)) {return index;}
	if (buf[index] != ',') {return index;}
	index++;
	if (!parse_num(buf, &sum2, &index)) {return index;}
	if (buf[index] != ')') {return index;}
	total_count += sum1 * sum2;
	return index+1;
}

char* read_from_file() {
	FILE *file = fopen("3.txt", "r");

	fseek(file, 0L, SEEK_END);
	size_t size_of_file = ftell(file);
	fseek(file, 0L, SEEK_SET);
	
	char *content = malloc(size_of_file * sizeof(char));
	if (content == NULL) {printf("bad malloc");}

	fread(content, sizeof(char), size_of_file, file);

	return content;
}

int main() {
	char *buf = read_from_file();
	int buf_len = strlen(buf);
	int index = 0;
	bool should_mul = true;
	while (index < buf_len) {
		index += check_buf(buf+index, &should_mul );
	}
	printf("%d\n", total_count);
	return 0;
}
