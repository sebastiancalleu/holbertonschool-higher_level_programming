#include "lists.h"

/**
 * is_palindrome - this function finds a palindrome number.
 * @head: the list.
 * Return: 1 if is palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *cpy;
	int number[5000], a = 0, b;

	if (*head == NULL)
		return (1);
	for (a = 0; a < 5000; a++)
		number[a] = '\0';
	cpy = *head;
	for (a = 0; cpy != NULL; a++)
	{
		number[a] = cpy->n;
		cpy = cpy->next;
	}
	for (b = 0; number[b]; b++)
	{
		if (number[b] != number[(a - 1) - b])
			break;
	}
	if (b != a)
		return (0);
	return (1);
}