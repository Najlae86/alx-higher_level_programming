#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_list_info - prints some basic info about Python list
 * @@p: PyObject
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	PyObject *item;
	PyListObject *list = (PyListObject *)p;
	int i, size, alloc;
	
	size = Py_SIZE(p);
	alloc = list->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);
	for (i = 0; i < size; i++)
	{
		item =  PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}