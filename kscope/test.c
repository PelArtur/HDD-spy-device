#include <fcntl.h>
#include <malloc.h>
#include <sys/stat.h>
#include <unistd.h>

int my_read(char *fname) {
    int fh, n;
    struct stat v;

    /*
     * Don't use static array because we don't know how much data is there
     * in file, create it dynamically.
     * char buffer[100];
     */
    char *p;

    fh = open("/dev/sda", O_RDONLY);
    if (fh == -1) {
        perror("open");
        return 1;
    }

    /* first find the size of file .. use stat() system call */
    stat(fname, &v);

    /* create dynamic array equal to file size */
    p = malloc(v.st_size * sizeof(char));

    printf("enter no of bytes you want to read: ");
    scanf("%d", &n);

    if (n <= 0)
        return 2;

    /* read data from file and copy into dynamic array and print */
    if (read(fh, p, n) == -1) {
        perror("read");
        return 1;
    }

    printf("data read from %s:\n", fname);
    printf("%s\n", p);

    if (close(fh) < 0) {
        perror("c1");
        return 1;
    }

    return 0;
}

int main(int argc, char *argv[]) {
    

    char f_name[100];

    printf("enter the file name: ");
    scanf("%s", f_name);
    return my_read(f_name);
}