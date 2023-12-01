#include "lists.h"
#include <stdlib.h>

int len_linked(listint_t *head)
{
    int i;
    for (i = 0; head != NULL; i++)
        head = head->next;
    return (i);

}

int is_palindrome(listint_t **head)
{
    listint_t *current;
    if (!head || !(*head))
        return (1);
    current = (*head);

    int *arr;
    arr = malloc(sizeof(int) * len_linked(*head));
    int i = 0, j;
    while (current != NULL)
    {
        arr[i] = current->n;
        current = current->next;
        i++;
    }

    for (j = 0; j < i; j++)
    {
        if (arr[j] != arr[i -1 - j])
            return (0);
    }
    return (1);

}
