 def on_click3(self):
        if ter[0]<2:
            QMessageBox.about(self, "Error", "Missing Image")
            return
             
        pro = np.zeros([256,1],dtype=np.float16)
        pro2 = np.zeros([256,1],dtype=np.float16)
        pro3 = np.zeros([256,1],dtype=np.float16)
        b=0
        v=0
        s=0
        for a in range(256):
            b=b+hist[a,0,0]
            
        for u in range(256):
            v=v+hist[u,0,1]
            
        for o in range(256):
            s=s+hist[o,0,2]
            
        for y in range(256):
            e=y
            while e>-1:
                pro[y]=pro[y]+float(hist[e,0,0]/b)
                e=e-1
        for h in range(256):
            e=h
            while e>-1:
                pro2[h]=pro2[h]+float(hist[e,0,1]/v)
                e=e-1
        for n in range(256):
            e=n
            while e>-1:
                pro3[n]=pro3[n]+float(hist[e,0,2]/s)
                e=e-1
        
        pro1 = np.zeros([256,1],dtype=np.float16)
        pro21 = np.zeros([256,1],dtype=np.float16)
        pro31 = np.zeros([256,1],dtype=np.float16)
        b1=0
        v1=0
        s1=0
        for a1 in range(256):
            b1=b1+hist2[a1,0,0]
            
        for u1 in range(256):
            v1=v1+hist2[u1,0,1]
            
        for o1 in range(256):
            s1=s1+hist2[o1,0,2]
            
        for y1 in range(256):
            e=y1
            while e>-1:
                pro1[y1]=pro1[y1]+float(hist2[e,0,0]/b1)
                e=e-1
        for h1 in range(256):
            e=h1
            while e>-1:
                pro21[h1]=pro21[h1]+float(hist2[e,0,1]/v1)
                e=e-1
        for n1 in range(256):
            e=n1
            while e>-1:
                pro31[n1]=pro31[n1]+float(hist2[e,0,2]/s1)
                e=e-1
                
        LUT = np.zeros([256,1],dtype=np.uint8)
        z=0
        for r in range(256):
            while((pro1[z] < pro[r]) and (z<255)):
                z+=1
            LUT[r]=z
            
        LUT1 = np.zeros([256,1],dtype=np.uint8)
        z=0
        for c in range(256):
            while((pro21[z] < pro2[c]) and (z<255)):
                z+=1
            LUT1[c]=z
            
        LUT2 = np.zeros([256,1],dtype=np.uint8)
        z=0
        for l in range(256):
            while((pro31[z] < pro3[l]) and (z<255)):
                z+=1
            LUT2[l]=z

        tar=np.zeros([256,1,3],dtype=np.uint8)
        for x in range(256):
            tar[x,0,0]=LUT[x]
            
        for x1 in range(256):
            tar[x1,0,1]=LUT1[x1]
            
        for x2 in range(256):
            tar[x2,0,2]=LUT2[x2]
    
        for p9 in range(427):
            for p3 in range(277):
                for p7 in range(3):
                    imga[p9,p3,p7]=tar[imga[p9,p3,p7],0,p7]
       
        cv2.imwrite('color3.png', imga)
        pixmap3 = QPixmap('color3.png')
        self.label9.setPixmap(pixmap3)
        self.label9.setGeometry(1300, 100, pixmap3.width(), pixmap3.height())
        Ak=256
        Bk=1
        Ck=3
        tar1=np.zeros([Ak,Bk,Ck],dtype=np.uint32)
        for kt in range(256):
            tar1[kt,0,...]=np.sum(np.sum(imga==kt,0),0)
        plt.clf()
        plt.figure(3)
        plt.subplot(3,1,1)
        N0 = len(tar1)
        x0 = range(N0)
        width = 1/1.5
        plt.bar(x0,tar1[:,0,2],width,color='red')
        plt.subplot(3,1,2)
        plt.bar(x0,tar1[:,0,1],width,color='green')
        plt.subplot(3,1,3)
        plt.bar(x0,tar1[:,0,0],width,color='blue')
        plt.savefig('3.png')
        img5 = cv2.imread('3.png', flags=cv2.IMREAD_COLOR)
        scale_percent = 70
        width = int(img5.shape[1] * scale_percent / 100)
        height = int(img5.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(img5, dim, interpolation = cv2.INTER_AREA)
        cv2.imwrite('3.png', resized)
        pixmap = QPixmap('3.png')
        self.label8.setPixmap(pixmap)
        self.label8.setGeometry(1300, 600, pixmap.width(), pixmap.height())
