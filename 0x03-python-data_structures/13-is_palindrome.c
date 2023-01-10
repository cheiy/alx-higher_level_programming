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
	int length, i, palindrome;
	int *nums;
	listint_t *current;

	i = 0;
	length = 0;
	if (*head == NULL)
		return (0);
	current = *head;
	while (current != NULL)
	{
		current = current->next;
		length++;
	}
	current = *head;
	nums = malloc(sizeof(int) * (length + 1));
	if (nums == NULL)
		exit(1);
	while (current != NULL)
	{
		nums[i] = current->n;
		current = current->next;
		i++;
	}
	nums[i] = '\0';
	if (nums != NULL)
	{
		i = 0;
		while (i <= length)
		{
			if (nums[i] == nums[length])
				palindrome = 1;
			else
				palindrome = 0;
			i++, length--;
		}
		free(nums);
	}
	return (palindrome);
}
