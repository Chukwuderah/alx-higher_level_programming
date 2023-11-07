#include <stdlib.h>
#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info -  function that prints some of the basic
 * infos about Python lists
 * @p: python list
 */

void print_python_list_info(PyObject *p)
{
	int elm;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (elm = 0; elm < Py_SIZE(p); elm++)
		printf("Element %d: %s\n", elm, Py_TYPE(PyList_GetItem(p, elm))->tp_name);
}

