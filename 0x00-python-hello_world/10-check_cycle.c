#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - this function checks if a listed link has a loop.
 * @list: the list.
 * Return: 1 if there is a loop, 0 if not.
 */
int check_cycle(listint_t *list)
{
listint_t *listft, *listsl;

listft = list;
listsl = list;
while (listft != NULL && listsl != NULL && listft->next != NULL)
{
	listsl = listsl->next;
	listft = listft->next->next;
	if (listft == listsl)
		return (1);
}
return (0);
}
