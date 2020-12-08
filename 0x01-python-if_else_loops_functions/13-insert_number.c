#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - this function adds a node at a sorted list.
 * @head: the list.
 * @number: the data to add.
 * Return: the new node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	int a;
	listint_t *tmp1, *tmp2;
	listint_t *new;

	tmp1 = *head;
	tmp2 = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if ((*head)->n >= number)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		tmp1 = tmp1->next;
		for (a = 0; tmp1 != NULL; a++)
		{
			if (tmp1->n >= number)
			{
				tmp2->next = new;
				new->next = tmp1;
				break;
			}
			else
				tmp1 = tmp1->next;
				tmp2 = tmp2->next;
		}
		if (tmp1 == NULL)
		{
			tmp2->next = new;
			new->next = tmp1;
		}
	}
	return (new);
}
