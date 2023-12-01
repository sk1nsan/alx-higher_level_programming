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
	int *arr;
	int i, j;

	if (!head || !(*head))
		return (1);
	current = (*head);

	arr = malloc(sizeof(int) * len_linked(*head));
	i = 0;
	while (current != NULL)
	{
		arr[i] = current->n;
		current = current->next;
		i++;
	}

	for (j = 0; j < i; j++)
	{
		if (arr[j] != arr[i - 1 - j])
		{
			free(arr);
			return (0);
		}
	}
	free(arr);
	return (1);
}
