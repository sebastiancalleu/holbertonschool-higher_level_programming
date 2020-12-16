#include "Python.h"

/**
 * print_python_list_info - print some python info.
 * @p: pointer to Pyobject.
 */

void print_python_list_info(PyObject *p)
{
	int a, b;
	PyObject *element;

	b = PyList_Size(p);

	PyListObject *tmp = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", b);
	printf("[*] Allocated = %li\n", tmp->allocated);
	for (a = 0; a < b; a++)
	{
		element = PyList_GetItem(p, a);
		if (PyFloat_Check(element))
			printf("Element %d: float\n", a);
		if (PyTuple_Check(element))
			printf("Element %d: tuple\n", a);
		if (PyList_Check(element))
			printf("Element %d: list\n", a);
		if (PyLong_Check(element))
			printf("Element %d: int\n", a);
		if (PyUnicode_Check(element))
			printf("Element %d: str\n", a);
	}
}