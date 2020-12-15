#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * resersed - reverse a number.
 * @number: the number.
 * Return: the reversed number.
int reversed(int number)
{
	int revnum = 0;

	while (number > 0)
	{
		revnum = revnum * 10 + (number % 10);
		number = number / 10;
	}
	return (revnum);
}
*/

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