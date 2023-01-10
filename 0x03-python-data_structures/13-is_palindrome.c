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
	int length, i, palindrome, *nums;
	listint_t *current;

	i = length = 0;
	if (*head == NULL)
		return (1);
	current = *head;
	while (current != NULL)
	{
		current = current->next;
		length++;
	}
	if (length == 1)
		return (1);
	current = *head;
	nums = malloc(sizeof(int) * (length + 1));
	if (nums == NULL)
		exit(0);
	while (current != NULL)
	{
		nums[i] = current->n;
		current = current->next;
		i++;
	}
	nums[i] = '\0';
	i = 0;
	length--;
	while (i <= length)
	{
		if (nums[i] == nums[length])
			palindrome = 1;
		else
		{
			free(nums);
			return (0);
		}
		i++, length--;
	}
	free(nums);
	return (palindrome);
}
