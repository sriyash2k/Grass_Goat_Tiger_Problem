import threading

meml	 = ['man','tiger','grass','goat']
memr	 = []
memb	 = []
stop	 = 0
start1	 = 0
start2	 = 0
start3	 = 0
boatpos  = 'left'

def checkarea(a,place):
	global stop
	if stop == 1:
		return
	if( 'tiger' in a  and 'goat' in a and 'man' not in a):
		stop=1
		print('\n*****OOPS the Tiger ate the Goat on the',place,'*****')
	if( 'grass' in a  and 'goat' in a  and 'man' not in a):
		stop=1
		print('\n*****OOPS the Goat ate the Grass on the',place,'*****')
		
			
def sail():
	global boatpos
	if boatpos=='right':
	    print('\nBoat is Full and is sailing to the right beach ')
	else:
	    print('\nBoat is sailing to the left beach ')

def left():
	global memb
	global memr
	global meml
	global stop
	global boatpos
	if (len(memb) == 2):
		checkarea(meml,'left shore')
	else:
		return
	if stop==0:
		return;
	if (len(meml) == 0):
		print('Successfully completed the challenge')

		
def right():
	global memb
	global memr
	global meml
	global stop
	global boatpos
	checkarea(memr,'right shore')
	if (len(meml) == 0):
		print('Successfully completed the challenge')
		return;
	while ( boatpos=='right' and stop==0 ):
		sail()
		x=5
		while(x>4 or x<0):
			print('Right shore')
			x=int(input('Drop on right beach \n\t1.Man   2.Grass   3.Goat   4.Tiger\t'));
			if(x>4 or x<0):
				print('Invalid input. ');
			else:
				if (x==1):
					if('man' not in memb):
						print('Man is not on the boat')
						continue
					memb.remove('man');
					memr.append('man');
				elif (x==2):
					if('grass' not in memb):
						print('Grass is not on the boat')
						continue
					memb.remove('grass');
					memr.append('grass');
				elif (x==3):
					if('goat' not in memb):
						print('goat is not on the boat')
						continue
					memb.remove('goat');
					memr.append('goat');
				elif (x==4):
					if('tiger' not in memb):
						print('tiger is not on the boat')
						continue
					memb.remove('tiger');
					memr.append('tiger');
				boatpos='left'
				print('\nLeft ',meml)
				print('Boat ',memb)
				print('Right',memr,'\n')
				if (len(meml) == 0):
					print('Successfully completed the challenge')
					return;
		x=5
		while(x>4 or x<0):
			print('Right shore')
			x=int(input('Enter from right beach \n\t0.No One 1.Man   2.Grass   3.Goat   4.Tiger\t'));
			if(x>4 or x<0):
				print('Invalid input. ');
			else:
				if (x==1):
					if('man' not in memr):
						print('Man is not on the right shore')
						continue
					memr.remove('man');
					memb.append('man');
				elif (x==2):
					if('grass' not in memr):
						print('Grass is not on the right shore')
						continue
					memr.remove('grass');
					memb.append('grass');
				elif (x==3):
					if('goat' not in memr):
						print('goat is not on the right shore')
						continue
					memr.remove('goat');
					memb.append('goat');
				elif (x==4):
					if('tiger' not in memr):
						print('tiger is not on the right shore')
						continue
					memr.remove('tiger');
					memb.append('tiger');
				boatpos='left'
				print('\nLeft ',meml)
				print('Boat ',memb)
				print('Right',memr,'\n')
				sail()

	checkarea(memr,'right shore')
				

def boat():
	global memb
	global memr
	global meml
	global stop
	global boatpos
	
	checkarea(memb,'boat')
	if (stop == 1):
		return;

	if('man' not in memb):
		stop=1
		print('boatpos: ' + boatpos  )
		print('\nLeft ',meml)
		print('Boat ',memb)
		print('Right',memr,'\n')
		print('The boat must contain the man to sail through the sea.')
	
	else:
		print('man sails')
	if (len(meml) == 0):
		print('Successfully completed the challenge')
			
if __name__ == "__main__": 
	
	while (stop == 0):
		x=5
		boatpos='left'
			
		while(x>4 or x<0):
			t1 = threading.Thread(target=left,  args=())
			t2 = threading.Thread(target=right, args=())
			t3 = threading.Thread(target=boat,  args=())
			print('Left shore')
			x=int(input('Enter \n\t1.Man   2.Grass   3.Goat   4.Tiger\t'));
			if(x>4 or x<0):
				print('Invalid input. ');
			else:
				if (x==1):
					if('man' not in meml):
						print('Man is not on the left shore')
						continue;
					meml.remove('man')
					memb.append('man')
				elif (x==2):
					if('grass' not in meml):
						print('grass is not on the left shore')
						continue;
					meml.remove('grass')
					memb.append('grass')
				elif (x==3):
					if('goat' not in meml):
						print('goat is not on the left shore')
						continue;
					meml.remove('goat');
					memb.append('goat');
				elif (x==4):
					if('tiger' not in meml):
						print('tiger is not on the left shore')
						continue;
					meml.remove('tiger');
					memb.append('tiger');

				print('\nLeft ',meml)
				print('Boat ',memb)
				print('Right',memr,'\n')

				if (len(memb) == 2):	
					boatpos='right'
					t1.start()
					if stop==0:
						t2.start()
						start2 = 1
					if stop==0:
						t3.start()
						start3 = 1

					t1.join()
					if start2 == 1:
						t2.join()
					if start3 == 1:
						t3.join()
					if boatpos == 'left':
						t3 = threading.Thread(target=boat,  args=())
						t3.start()
					x=5;
					if (len(meml) == 0):
						print('Successfully completed the challenge')

					while((x>4 or x<0) and len(memb)==2):
						print('Left shore')
						x=int(input('Drop on left beach \n\t 1.Man   2.Grass   3.Goat   4.Tiger\t'));
						if(x>4 or x<0):
							print('Invalid input. ');
						else:
							if (x==1):
								if('man' not in memb):
									print('Man is not on the boat')
									continue
								memb.remove('man');
								meml.append('man');
							elif (x==2):
								if('grass' not in memb):
									print('Grass is not on the boat')
									continue
								memb.remove('grass');
								meml.append('grass');
							elif (x==3):
								if('goat' not in memb):
									print('goat is not on the boat')
									continue
								memb.remove('goat');
								meml.append('goat');
							elif (x==4):
								if('tiger' not in memb):
									print('tiger is not on the boat')
									continue
								memb.remove('tiger');
								meml.append('tiger');
							boatpos='left'
							print('\nLeft ',meml)
							print('Boat ',memb)
							print('Right',memr,'\n')
							if (len(meml) == 0):
								print('Successfully completed the challenge')
