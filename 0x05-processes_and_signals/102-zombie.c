#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - This function creates an infinite loop, kinda making the
 * code hang.
 * Return: 0
*/
int infinite_while(void)
{
while (1)
sleep(1);
return (0);
}
/**
 * main - The main finction. It creates 5 zombie processes.
 * Return: 0
 */
int main(void)
{
int x;
pid_t zombie;

for (x = 0; x < 5; x++)
{
zombie = fork();
if (!zombie)
return (0);
printf("Zombie process created, PID: %d\n", zombie);
}
infinite_while();
return (0);
}
