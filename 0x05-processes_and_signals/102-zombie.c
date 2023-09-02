#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
 * infinite_while - creates infinite loop
 * Return: 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates zombie process
 * Return: 0
 */

int main(void)
{
	int idx;
	pid_t process_id;

	for (idx = 1; idx <= 5; idx++)
	{
		process_id = fork();
		if (!process_id)
		{
			return (0);
		}
		printf("Zombie process created, PID: %d\n", process_id);
	}

	infinite_while();
	return (0);
}
