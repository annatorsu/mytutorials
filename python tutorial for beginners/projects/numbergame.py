{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-3-7acc5c0dfb90>, line 4)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-3-7acc5c0dfb90>\"\u001b[1;36m, line \u001b[1;32m4\u001b[0m\n\u001b[1;33m    for number in range guessnumber:\u001b[0m\n\u001b[1;37m                                  ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "number=\"\"\n",
    "total=0\n",
    "guessnumber=int(input(\"enter your number:  \"))\n",
    "for numbe in range guessnumber:\n",
    "    total+=\n",
    "print (total)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter an integer: 6\n",
      "The total numbers from 1 to 6 is 21\n"
     ]
    }
   ],
   "source": [
    "usersNumber = input('Please enter an integer: ') \n",
    "usersNumber = int(usersNumber)\n",
    "highEndOfRange = usersNumber + 1\n",
    "total = 0 \n",
    "for number in range(1, highEndOfRange):    \n",
    "    total = total + number\n",
    "print('The total numbers from 1 to', usersNumber, 'is', total)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter an integer: 6\n",
      "The total numbers from 1 to 6 is 21\n"
     ]
    }
   ],
   "source": [
    "usersNumber = input('Please enter an integer: ') \n",
    "usersNumber = int(usersNumber)     #program that asks user for a number and adds up from one to the users number \n",
    "\n",
    "total = 0 \n",
    "for number in range(1, (usersNumber+1)):    \n",
    "    total = total + number\n",
    "print('The total numbers from 1 to', usersNumber, 'is', total)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
