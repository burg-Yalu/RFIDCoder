class Hamming():
    def __init__(self,data):
        self.data = data
    def hammingEncode(self):
        self.dataLen = len(self.data)
        self.r = 0
        while pow(2,self.r) - self.r < self.dataLen + 1:
            self.r += 1
        self.HammingLen = self.r + self.dataLen #求出插入校验码后的总长
        self.HammingData = [0] * self.HammingLen
        for i in range(self.r):
            self.HammingData[pow(2,i)-1] = 1#先默认校验位都设置为1
        dataIndex = 0
        for i in range(self.HammingLen):#插入数据
            if self.HammingData[i] == 0:
                self.HammingData[i] = self.data[dataIndex]
                dataIndex += 1
        print(self.HammingData)
        for pn in range(1,self.r+1):#逐个计算校验位
            #pn所在位置
            pos = pow(2,(pn-1)) - 1
            temp = 0
            for pr in range(pos,self.HammingLen+1,pow(2,pn)):
                for i in range(pr,min(pr+pow(2,(pn-1)),self.HammingLen)):#疯狂异或
                    temp ^= self.HammingData[i]
            if temp == 1:
                self.HammingData[pos] = 0
        print(self.HammingData)

    def makeMistake(self,k):
        if self.HammingData[k] == 0:
            self.HammingData[k] = 1
        else:
            self.HammingData[k] = 0
        print(self.HammingData)

    def hammingDecode(self):
        wrongList = []
        for pn in range(1,self.r+1):#逐个计算校验组
            #pn所在位置
            pos = pow(2,(pn-1)) - 1
            temp = 0
            for pr in range(pos,self.HammingLen+1,pow(2,pn)):
                for i in range(pr,min(pr+pow(2,(pn-1)),self.HammingLen)):#疯狂异或
                    temp ^= self.HammingData[i]
            print(temp)
            if temp == 1:
                wrongList.append(pn)#记下哪个校验组错了
        if wrongList:
            print("原数据",self.HammingData)
            if len(wrongList) == 1:
                self.HammingData[pow(2,wrongList[0]-1)-1] ^= 1
            elif len(wrongList) == 2:
                if 1 in wrongList and 2 in wrongList:
                    self.HammingData[2] ^= 1
                elif 1 in wrongList and 3 in wrongList:
                    self.HammingData[4] ^= 1
                elif 1 in wrongList and 4 in wrongList:
                    self.HammingData[8] ^= 1
                elif 2 in wrongList and 3 in wrongList:
                    self.HammingData[5] ^= 1
                elif 2 in wrongList and 4 in wrongList:
                    self.HammingData[9] ^= 1
                elif 4 in wrongList and 3 in wrongList:
                    self.HammingData[11] ^= 1
            elif len(wrongList) == 3:
                if 1 in wrongList and 2 in wrongList and 3 in wrongList:
                    self.HammingData[6] ^= 1
                elif 1 in wrongList and 2 in wrongList and 4 in wrongList:
                    self.HammingData[10] ^= 1
            print("现数据",self.HammingData)
            return False
        else:
            return True


a = Hamming([1,0,1,1,1,0,1,1])
a.hammingEncode()
a.hammingDecode()
a.makeMistake(4)
a.hammingDecode()
