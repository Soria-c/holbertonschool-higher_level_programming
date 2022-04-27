#include "lists.h"
/**
 * insert_node - inserts a node in a sorted linked list.
 * @head: address of linked list.
 * @number: number to be inserted.
 * Return: address of linked list.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *tmp = *head;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (!(*head) || number <= tmp->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	for (; tmp->next; tmp = tmp->next)
	{
		if (number >= tmp->n && number <= tmp->next->n)
		{
			new->next = tmp->next;
			tmp->next = new;
			return (new);
		}
	}
	tmp->next = new;
	return (new);
}

