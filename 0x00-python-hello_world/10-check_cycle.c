#include "lists.h"

/**
 * check_cycle - check for loop in linked lists
 * @list: head of linked list
 * return: 1 if cycled, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *a, *b;

	if (!list)
	{
		return (0);
	}
	a = list;
	b = list->next;
	while (b && a && b->next)
	{
		if (a == b)
		{
			return (1);
		}
		a = a->next;
		b = b->next->next;
	}
	return (0);
}
