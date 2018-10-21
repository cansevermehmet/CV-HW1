def on_click(self):
        imagePath, _ = QFileDialog.getOpenFileName()
        pixmap2 = QPixmap(imagePath)
        self.label2.setPixmap(pixmap2)
        self.label2.setGeometry(100, 100, pixmap2.width(), pixmap2.height())
        img = cv2.imread(imagePath, flags=cv2.IMREAD_COLOR)
        R,G,B=img.shape
        for pi in range(427):
            for pi2 in range(277):
                for pi3 in range(3):
                    imga[pi,pi2,pi3]=img[pi,pi2,pi3]

        for g in range(256):
            hist[g,0,...]=np.sum(np.sum(img==g,0),0)
        plt.clf()
        plt.figure(1)
        plt.subplot(3,1,1)
        N = len(hist)
        x = range(N)
        width = 1/1.5
        plt.bar(x,hist[:,0,2],width,color='red')
        plt.subplot(3,1,2)
        plt.bar(x,hist[:,0,1],width,color='green')
        plt.subplot(3,1,3)
        plt.bar(x,hist[:,0,0],width,color='blue')
        plt.savefig('1.png')
        img2 = cv2.imread('1.png', flags=cv2.IMREAD_COLOR)
        scale_percent = 70
        width = int(img2.shape[1] * scale_percent / 100)
        height = int(img2.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(img2, dim, interpolation = cv2.INTER_AREA)
        cv2.imwrite('1.png', resized)
        pixmap = QPixmap('1.png')
        self.label.setPixmap(pixmap)
        self.label.setGeometry(100, 600, pixmap.width(), pixmap.height())
        ter[0]+=1
