#include "lists.h"
/**
 * insert_node - inserts a node in a sorted linked list.
 * @head: address of linked list.
 * @number: number to be inserted.
 * Return: address of linked list.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL;
	listint_t *tmp = *head;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	for (; tmp->next; tmp = tmp->next)
	{
		if (number >= tmp->n && number <= tmp->next->n)
		{
			new->next = tmp->next;
			tmp->next = new;
			break;
		}
		else if (number <= tmp->n)
		{
			new->next = tmp;
			*head = new;
			break;
		}
	}
	if (!(tmp->next))
	{
		new->next = NULL;
		tmp->next = new;
	}
	return (*head);
}

