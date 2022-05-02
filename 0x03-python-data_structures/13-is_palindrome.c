#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - Checkes is a linked list is palindrome
 * @head: address of linked list
 * Return: 1 if it is palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp1, *tmp2;

	tmp1 = *head;
	for (; tmp1; tmp1 = tmp1->next)
	{
		tmp2 = tmp1;
		for (; tmp2->next->next; tmp2 = tmp2->next)
			continue;
		if (tmp1->n != tmp2->next->n)
			return (0);
		free(tmp2->next);
		tmp2->next = NULL;
	}
	return (1);
}
