from random import choice


def option():
	
	options = ["R", "P", "S"]
	player = input(
		f'Player pick one option beteween {options}\n')[0].upper()
	cpu = choice(options)
	
	while player not in options:
		print(f'CPU ({cpu}) : Player ({player})\n')
		print(f"Opps! Invalid choice, {player} not amongst our options (:")
		print("*" * 20)
		cpu = choice(options).upper()
		player = input(f'Player pick one option beteween {options}\n')[0].upper()
	return cpu, player



def game(cpu, player):
	while True:
		print(f'CPU ({cpu}) : Player ({player})')
		
		if cpu == player:
			print("Opps! It's a tie :)")
			cpu, player = option()
		elif cpu == 'R' and player == 'S':
			message = "Rock beats Scissors, CPU wins!"
			break
		elif cpu == 'P' and player == 'R':
			message = 'Paper beats Rock, CPU wins!'
			break
		elif cpu == 'S' and player == 'P':
			message= 'Scissors beats Paper, CPU wins!'
			break
		
		# for player
		elif player == 'R' and cpu == 'S':
			message = "Rock beats Scissors, Player wins!"
			break
		elif player == 'P' and cpu == 'R':
			message = 'Paper beats Rock, Player wins!'
			break
		elif player == 'S' and cpu == 'P':
			message = 'Scissors beats Paper, Player wins!'
			break
	return message


cpu, player = option()
print(game(cpu, player))
