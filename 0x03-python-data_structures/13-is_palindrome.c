#include "lists.h"
#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>
/**
 * is_palindrome - Function checks if a singly linked list is a palindrome
 * @head: A pointer to the address of the head node.
 *
 * Description: Function checks if a singly linked list is a palindrome
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int length, vals, i, palindrome;
	int *nums = NULL;
	listint_t *current;

	i = 0;
	vals = 0;
	length = 0;
	if (*head == NULL)
		return (0);
	current = *head;
	while (current != NULL)
	{
		nums = realloc(nums, (vals + 1) * sizeof(int));
		nums[vals] = current->n;
		current = current->next;
		length++;
		vals++;
	}
	while (i <= length)
	{
		if (nums[i] == nums[length])
			palindrome = 1;
		else
			palindrome = 0;
		i++, length--;
	}
	return (palindrome);
}
