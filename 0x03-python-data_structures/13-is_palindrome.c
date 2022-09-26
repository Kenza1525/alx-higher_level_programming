#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome - check if a list is palindrome
 * @head: head of the list
 * Return: 0 if is not palindrome or 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	int size = 0, idx = 0;
	int buffer[2043];

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (*head != NULL)
	{
		buffer[size] = (*head)->n;
		size++;
		(*head) = (*head)->next;
	}

	while (size >= idx)
	{
		if (buffer[idx] != buffer[size - 1])
			return (0);
		size--;
		idx++;
	}
	return (1);


}
