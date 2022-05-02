#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

int recursion(listint_t **save, listint_t *node);
/**
 * is_palindrome - Checks is a linked list is palindrome
 * @head: address of linked list
 * Return: 1 if it is palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (!head || !(*head))
		return (1);
	if (!(*head)->next)
		return (1);
	return (recursion(head, *head));
}

/**
 * recursion -  Checks if a linekd list is palindrome
 * @head: address of linked list
 * @node: address of a node
 * Return: 1 if palindrome, 0 otherwise
 */
int recursion(listint_t **head, listint_t *node)
{
	if (node->next && recursion(head, node->next) && (*head)->n != node->n)
		return (0);
	(*head) = (*head)->next;
	return (1);
}
