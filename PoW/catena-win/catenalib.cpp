#include <stdio.h>
#include "example_dll.h"
#include "catena.h"

__stdcall void hello(const char *s)
{
        printf("Hello %s\n", s);
}
