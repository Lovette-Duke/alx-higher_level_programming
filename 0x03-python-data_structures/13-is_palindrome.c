#include "lists.h"

/**
 * is_palindrome - check if a singly linked list is a palindrom
 * @head: the first node of the linked list
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *node = *head;
	unsigned int size, i;
	int data[10240];

	if (!head)
		return (0);
	if (!*head)
		return (1);
	size = len(node);

	if (size)
		return (1);

	node = *head;
	for (i = 0; node; i++, node = node->next)
		data[i] = node->n;

	for (i = 0; i <= size / 2; i++)
		if (data[i] != data[size - i - 1])
		return (0);

	return (1);
}
