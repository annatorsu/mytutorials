{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "what is your nameAn\n",
      "name must be at least 3 characters\n"
     ]
    }
   ],
   "source": [
    "name=input(\"what is your name\")\n",
    "if len(name)<3:\n",
    "    print(\"name must be at least 3 characters\")\n",
    "elif len(name)>50:\n",
    "    print(\"name must be less than 50 characters\")\n",
    "else:\n",
    "    print(\"name looks good\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "what is your nameaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaadjnfcvfhrjjffffffffffffffffffffffffffff\n",
      "name must be less than 50 characters\n"
     ]
    }
   ],
   "source": [
    "name=input(\"what is your name\")\n",
    "if len(name)<3:\n",
    "    print(\"name must be at least 3 characters\")\n",
    "elif len(name)>50:\n",
    "    print(\"name must be less than 50 characters\")\n",
    "else:\n",
    "    print(\"name looks good\")\n"
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
