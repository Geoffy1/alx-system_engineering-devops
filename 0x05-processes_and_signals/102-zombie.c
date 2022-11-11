#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - creates an infinite loop
 * Return: always 0 on Success,
 * and 1 if Failure
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
 * main - creates 5 zombie jobs
 * Return: always 0 on Success
 * and 1 if Failure
 */
int main(void)
{
	int n;
	pid_t zombie;

	for (n = 0; n < 5; n++)
	{
		zombie = fork();
		if (!zombie)
			return (0);
		printf("Zombie process created, PID: %d\n", zombie);
	}

	infinite_while();
	return (0);
}