#include "lists.h"
/**
 * check_cycle - checks if there is a cycle in the linked list
 *
 * @list: list to be checked
 *
 * Return: 1 if there is no cycle
 * 0 otherwise
*/
int check_cycle(listint_t *list)
{
	listint_t *buffer[1024];
	int i = 0, j;

	if (list == NULL)
		return (0);
	while (list->next != NULL)
	{
		for (j = 0; j <= i; j++)
		{
			if (list->next == buffer[j])
				return (0);
		}
		buffer[i] = list->next;
	}
	return (1);
}
