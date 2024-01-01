#include <stdlib.h>

int main(int argc, char** argv) {
	system("python -m http.server | start http://127.0.0.1:8000/data/setup.html");
	system("pause");
	return 0;
}
