from numpy import true_divide


class game:
    def isWin(ste):
        if int(ste[1]) == 0 and int(ste[2]) == 0:
            return True
        elif int(ste[3]) == 0 and int(ste[4]) == 0:
            return False
        else:
            raise Exception('Not a terminated state!')
            
    def isTwZo(ste):
        steAry = [int(ste[1]), int(ste[2]), int(ste[3]), int(ste[4])]
        if steAry[0] == 0 and steAry[1] != 0:
            if steAry[2] == 0 and steAry[3] != 0:
                return True
            elif steAry[3] == 0 and steAry[2] != 0:
                return True
        elif steAry[0] != 0 and steAry[1] == 0:
            if steAry[2] == 0 and steAry[3] != 0:
                return True
            elif steAry[3] == 0 and steAry[2] != 0:
                return True
        return False

    def stateAction(ste : str) -> list:
            steAry = [int(ste[1]), int(ste[2]), int(ste[3]), int(ste[4])]
            toRet = []
            if int(ste[0]) == 0:
                if steAry[0] != 0 and steAry[2] != 0:
                    toRet.append(0)
                if steAry[0] != 0 and steAry[3] != 0:
                    toRet.append(1)
                if steAry[1] != 0 and steAry[2] != 0:
                    toRet.append(2)
                if steAry[1] != 0 and steAry[3] != 0:
                    toRet.append(3)
            else:
                if steAry[2] != 0 and steAry[0] != 0:
                    toRet.append(0)
                if steAry[2] != 0 and steAry[1] != 0:
                    toRet.append(1)
                if steAry[3] != 0 and steAry[0] != 0:
                    toRet.append(2)
                if steAry[3] != 0 and steAry[1] != 0:
                    toRet.append(3)
            return toRet

    def actionToState(ste, act):
            steAry = [int(ste[1]), int(ste[2]), int(ste[3]), int(ste[4])]
            if int(ste[0]) == 0:
                if int(act) == 0:
                    if steAry[0] != 0 and steAry[2] != 0:
                        return str((int(ste[0]) + 1) % 2) + str((steAry[0] + steAry[2]) % 10) + str(steAry[1]) + str(steAry[2]) + str(steAry[3])
                elif int(act) == 1:
                    if steAry[0] != 0 and steAry[3] != 0:
                        return str((int(ste[0]) + 1) % 2) + str((steAry[0] + steAry[3]) % 10) + str(steAry[1]) + str(steAry[2]) + str(steAry[3])
                elif int(act) == 2:
                    if steAry[1] != 0 and steAry[2] != 0:
                        return str((int(ste[0]) + 1) % 2) + str(steAry[0]) + str((steAry[1] + steAry[2]) % 10) + str(steAry[2]) + str(steAry[3])
                elif int(act) == 3:
                    if steAry[1] != 0 and steAry[3] != 0:
                        return str((int(ste[0]) + 1) % 2) + str(steAry[0]) + str((steAry[1] + steAry[3]) % 10) + str(steAry[2]) + str(steAry[3])
            else:
                if int(act) == 0:
                    if steAry[2] != 0 and steAry[0] != 0:
                        return str((int(ste[0]) + 1) % 2) + str(steAry[0]) + str(steAry[1]) + str((steAry[2] + steAry[0]) % 10) + str(steAry[3])
                elif int(act) == 1:
                    if steAry[2] != 0 and steAry[1] != 0:
                        return str((int(ste[0]) + 1) % 2) + str(steAry[0]) + str(steAry[1]) + str((steAry[2] + steAry[1]) % 10) + str(steAry[3])
                elif int(act) == 2:
                    if steAry[3] != 0 and steAry[0] != 0:
                        return str((int(ste[0]) + 1) % 2) + str(steAry[0]) + str(steAry[1]) + str(steAry[2]) + str((steAry[3] + steAry[0]) % 10)
                elif int(act) == 3:
                    if steAry[3] != 0 and steAry[1] != 0:
                        return str((int(ste[0]) + 1) % 2) + str(steAry[0]) + str(steAry[1]) + str(steAry[2]) + str((steAry[3] + steAry[1]) % 10)
            print(ste, act)
            raise "!"

    class state:
        def __init__(self, ste : str):
            self.__state = ste
            self.__actions = game.stateAction(ste)
            self.nextIdx = []
            self.prevIdx = []
            self.ai = []
            self.dtmd = False
            self.winrDtmd = False
            self.winr = False
            self.ulesDtmd = False
            self.ules = False
        def getSte(self) -> str:
            return self.__state

        def getActs(self) -> str:
            return self.__actions

        def toJSON(self):
            import json
            return {"ste" : self.__state, 
                "acts": self.__actions,
                "nxts" : self.nextIdx,
                "ai": self.ai,
                "dtmd": self.dtmd,
                "winr": self.winr}

        def toList(self):
            return [self.__state, self.__actions, self.prevIdx, self.nextIdx, self.dtmd, self.winr]
        
    def __init__(self):
        self.__states = [game.state("01111")]
        self.__map = { "01111" : 0 }
        states = self.__states
        length = len(states)
        ucount0 = 0
        tpFlg = 0
        flag1 = 0
        flag2 = 1
        while flag1 < flag2:#(flag1 != flag2):
            for i in range(flag1, flag2):
                cuSteObj = states[i]
                legAct = cuSteObj.getActs()
                for act in legAct:
                    nSte = game.actionToState(cuSteObj.getSte(), act)
                    if not self.__map.__contains__(nSte):
                        self.__map[nSte] = length
                        nLegAct = game.stateAction(nSte)
                        self.__states.append(game.state(nSte))
                        nSteObj = states[length]
                        if len(nLegAct) == 0:
                            if game.isWin(nSte):
                                nSteObj.dtmd = True
                                nSteObj.winrDtmd = True
                                nSteObj.winr = True
                            else:
                                nSteObj.dtmd = True
                                nSteObj.winrDtmd = True
                                nSteObj.winr = False
                        else:
                            nSteObj.dtmd = False
                            ucount0 += 1
                        length += 1
                    else:
                        continue
            flag1 = flag2
            flag2 = length - 1
            tpFlg += 1
            print(flag1, length)
        
        for i in range(length):
            ste = self.__states[i].getSte()
            for act in self.__states[i].getActs():
                nextId = self.__map[game.actionToState(ste, act)]
                self.__states[i].nextIdx.append(nextId)
                self.__states[nextId].prevIdx.append(i)
        '''
        for i in range(length):
            ste = self.__states0[i].getSte()
            if game.isTwZo(ste):
                temp = [i]
                
                idx = self.__nexts[i][0]
                
                while self.__dtmd[idx] != True and idx != i:
                    temp.append(idx)
                    idx = self.__nexts[idx][0]
                if self.__dtmd[idx] == True:
                    for i in temp:
                        self.__dtmd[i] = True
                        self.__chce[i] = self.__chce[idx]
                elif idx == i:
                    for i in temp:
                        self.__dtmd[i] = True
                        self.__chce[i] = False
                else:
                    raise Exception('Unexpected!')
        '''       
        ucount1 = 0
        count = 0
        while(ucount0 != ucount1):
            ucount1 = ucount0
            ucount0 = 0
            
            count += 1
            for i in range(length):
                if self.__states[i].dtmd == False:
                    isPReady = False
                    isFReady = True
                    ste = self.__states[i].getSte()
                    for next in self.__states[i].nextIdx:
                        isPReady = isPReady or self.__states[next].dtmd
                        isFReady = isFReady and self.__states[next].dtmd
                    if isFReady:
                        self.__states[i].dtmd = True
                        self.__states[i].winrDtmd = True
                        win0 = False
                        win1 = False
                        for next in self.__states[i].nextIdx:
                            if self.__states[next].dtmd:
                                if self.__states[next].winr:
                                    win0 = True
                                else:
                                    win1 = True
                        if int(ste[0]) == 0:
                            if win0:
                                self.__states[i].winr = True
                            else:
                                self.__states[i].winr = False
                        else:
                            if win1:
                                self.__states[i].winr = False
                            else:
                                self.__states[i].winr = True
                    elif isPReady:
                        win0 = False
                        win1 = False
                        for next in self.__states[i].nextIdx:
                            if self.__states[next].dtmd:
                                if self.__states[next].winr:
                                    win0 = True
                                else:
                                    win1 = True
                        if int(ste[0]) == 0:
                            if win0:
                                self.__states[i].dtmd = True
                                self.__states[i].winrDtmd = True
                                self.__states[i].winr = True
                            else:
                                ucount0 += 1
                        else:
                            if win1:
                                self.__states[i].dtmd = True
                                self.__states[i].winrDtmd = True
                                self.__states[i].winr = False
                            else:
                                ucount0 += 1
                    else:
                        ucount0 += 1
        print(ucount0)
        ucount0 = ucount1 + 1
        
        for i in states:
            p = True
            if i.getSte()[0] == '0':
                p = True
            else:
                p = False
            if i.dtmd:
                for j in i.nextIdx:
                    if states[j].dtmd and states[j].winrDtmd and states[j].winr == p:
                        i.ai.append(j)
            else:
                for j in i.nextIdx:
                    if states[j].dtmd == False:
                        i.ai.append(j)
        
        '''
        while (ucount1 < ucount0):
            ucount0 = ucount1
            ucount1 = 0
            count = 0
            for i in states:
                if i.dtmd == False:
                    flag = len(i.prevIdx) > 0
                    for j in i.prevIdx:
                        flag = flag and states[j].dtmd
                    if flag:
                        count += 1
                        i.dtmd = True
                        i.ulesDtmd = True
                        i.ules = True
                    else:
                        ucount1 += 1
            print(count)
          
        print(ucount0, ucount1)
        '''

    def __getitem__(self, idx):
        return self.__states[idx].toList()
    def getItemJSONById(self, id):
        return self.__states[id].toJSON()
    def getItemByIdx(self, ste):
        if (self.__map.__contains__(ste)):
            idx = self.__map[ste]
            return self.__states[idx].toList()
        else:
            raise Exception('Not a valid state string')
    def getLen(self):
        return len(self.__states)
import random as r
a = game()
strt = '01111'#"00562""04705"
#"03701"
#"13771"
# #"02017"
class myStk:
    def __init__(self):
        self.__nde = []
        self.__nxt = []

    def append(self, nde:int, nxt:list):
        self.__nde.append(nde)
        self.__nxt.append(nxt)
    def pop(self):
        toRet = self.__nxt[-1].pop()
        if (len(self.__nxt[-1]) == 0):
            self.__nde.pop(-1)
        return toRet
    def get(self, nde):
        return self.__nde[self.__nde.index(nde):len(self.__nde)]

    def getLen(self):
        return len(self.__nde)
met = set()
trace = []
stack = myStk()
stack.append(0, list(a[0][3]))
met.add(0)
count = 0
rings = []
'''
while(stack.getLen() > 0):
    cuIdx = stack.pop()

    if cuIdx in met:
        rings.append(stack.get(cuIdx))
        break
    else:
        met.add(cuIdx)
    stack.append(cuIdx, list(a[cuIdx][3]))
    count += 1
for i in rings[0]:
    print(a[i])
'''
'''
strt='01111'
legAct = game.stateAction(strt)
for i in a.getItemByIdx(strt)[2]:
    print(a[i])
print('----')
print(a.getItemByIdx(strt))
print('----')
for act in legAct:
    print(a.getItemByIdx(game.actionToState(strt, act)))
print('----')
count = 0
while len(game.stateAction(strt)) > 0 and count < 100:
    legAct = game.stateAction(strt)
    act = legAct[r.randint(0, len(legAct) - 1)]
    count += 1
    print(a.getItemByIdx(strt), act)
    strt = game.actionToState(strt, act)
print(a.getItemJSONById(0))
'''
import json
temp = []
for i in range(a.getLen()):
    temp.append(a.getItemJSONById(i))
file = open('test.json', 'w')
file.write(json.dumps(temp))
file.close()
