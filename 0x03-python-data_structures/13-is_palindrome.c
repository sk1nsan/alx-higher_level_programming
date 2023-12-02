#include "lists.h"
#include <stdlib.h>
/**
 * len_linked - returns length of linked list
 *
 * @head: linked list
 *
 * Return: length
 */
int len_linked(listint_t *head)
{
	int i;

	for (i = 0; head != NULL; i++)
		head = head->next;
	return (i);
}

/**
 * is_palindrome - checks if linkedlist is palindrome
 *
 * @head: linked list
 *
 * Return: 1 if it is
 * 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *current;
	int arr[10000];
	int i = 0, j = 0, n = 0;

	if (!head || !(*head))
		return (1);
	current = (*head);

	n = len_linked(*head);
	if (n == 1)
		return (1);
	while (current != NULL)
	{
		arr[i] = current->n;
		current = current->next;
		i++;
	}

	for (; j < (i / 2); j++)
	{
		if (arr[j] != arr[i - 1 - j])
			return (0);

	}
	return (1);
}
