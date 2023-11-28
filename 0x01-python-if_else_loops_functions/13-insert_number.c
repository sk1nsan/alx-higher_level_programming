#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * add_nodeint - adds an element to the linked list
 *
 * @head: first node
 * @n: int to be copied
 *
 * Return: linked list
 */

listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->next = *head;
	new->n = n;
	*head = new;
	return (new);
}
/**
 * insert_node - insets node in sorted linked list
 *
 * @head:linkedlist
 * @number: number of the new node
 *
 * Return: new node if it exists
 * Null otherwise
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *currentnode = *head;

	if (!head)
		return (NULL);
	if (!(*head))
	{
		*head =  malloc(sizeof(listint_t));
		if (*head == NULL)
			return (NULL);
		(*head)->next = NULL;
		(*head)->n = number;
		return (*head);


	}
	if ((*head)->n >= number)
	{
		return (add_nodeint(head, number));
	}
	else
	{
		while (currentnode->next != NULL)
		{
			newnode = malloc(sizeof(listint_t));
				if (newnode == NULL)
					return (NULL);
			if ((currentnode->next)->n >= number)
			{
				newnode->next = currentnode->next;
				newnode->n = number;
				currentnode->next = newnode;
				return (newnode);
			}
			free(newnode);
			currentnode = currentnode->next;
		}
	}
	return (add_nodeint_end(head, number));
}
