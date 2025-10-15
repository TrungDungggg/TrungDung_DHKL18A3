{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f1948db3",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "invalid literal for int() with base 10: ''",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mValueError\u001b[39m                                Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[1]\u001b[39m\u001b[32m, line 17\u001b[39m\n\u001b[32m     15\u001b[39m         \u001b[38;5;28mprint\u001b[39m(\u001b[33m\"\u001b[39m\u001b[33mDiện tích HCN: \u001b[39m\u001b[33m\"\u001b[39m,\u001b[38;5;28mself\u001b[39m.dien_tich())\n\u001b[32m     16\u001b[39m hcn = HCN()\n\u001b[32m---> \u001b[39m\u001b[32m17\u001b[39m \u001b[43mhcn\u001b[49m\u001b[43m.\u001b[49m\u001b[43mnhap\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m     18\u001b[39m hcn.display()\n",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[1]\u001b[39m\u001b[32m, line 6\u001b[39m, in \u001b[36mHCN.nhap\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m      5\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34mnhap\u001b[39m(\u001b[38;5;28mself\u001b[39m):\n\u001b[32m----> \u001b[39m\u001b[32m6\u001b[39m     \u001b[38;5;28mself\u001b[39m.canhA = \u001b[38;5;28;43mint\u001b[39;49m\u001b[43m(\u001b[49m\u001b[38;5;28;43minput\u001b[39;49m\u001b[43m(\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mNhập cạnh A: \u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m      7\u001b[39m     \u001b[38;5;28mself\u001b[39m.canhB = \u001b[38;5;28mint\u001b[39m(\u001b[38;5;28minput\u001b[39m(\u001b[33m\"\u001b[39m\u001b[33mNhập cạnh B: \u001b[39m\u001b[33m\"\u001b[39m))\n",
      "\u001b[31mValueError\u001b[39m: invalid literal for int() with base 10: ''"
     ]
    }
   ],
   "source": [
    "class HCN:\n",
    "    def __init__(self, canhA:int=0, canhB:int=0):\n",
    "        self.canhA = canhA\n",
    "        self.canhB = canhB\n",
    "    def nhap(self):\n",
    "        self.canhA = int(input(\"Nhập cạnh A: \"))\n",
    "        self.canhB = int(input(\"Nhập cạnh B: \"))\n",
    "    def chu_vi(self):\n",
    "        return 2*(self.canhA+self.canhB)\n",
    "    def dien_tich(self):\n",
    "        return self.canhA*self.canhB\n",
    "    def display(self):\n",
    "        print(f\"Độ dài cạnh A={self.canhA} Độ dài cạnh B={self.canhB}\")\n",
    "        print(\"Chu vi HCN: \",self.chu_vi())\n",
    "        print(\"Diện tích HCN: \",self.dien_tich())\n",
    "hcn = HCN()\n",
    "hcn.nhap()\n",
    "hcn.display()\n"
   ]
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
   "version": "3.13.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
