class ConvNet(nn.Module):
    ## [[student]]
    def __init__(self,pooling = nn.MaxPool2d): # argument sur le pooling
        super().__init__()
        # Convolution 5*5, 16 filtres
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=16, kernel_size=5)
        # Max pooling 3x3
        self.pool1 = pooling(kernel_size=3, stride=1)
        # Convolution 5*5, 16 filtres
        self.conv2 = nn.Conv2d(in_channels=16, out_channels=16, kernel_size=5)
        # Max pooling 3x3
        self.pool2 = pooling(3, 1)
        #initialisation des poids pour éviter des problèmes de gradient
        torch.nn.init.xavier_uniform_(self.conv1.weight)
        torch.nn.init.xavier_uniform_(self.conv2.weight)

        self.lin1 = nn.Linear(16*16*16,120)
        self.lin2 = nn.Linear(120, 10)
        
        self.features   = nn.Sequential(self.conv1,nn.ReLU(),self.pool1,self.conv2,nn.ReLU(),self.pool2)
        self.classifier = nn.Sequential(self.lin1,nn.ReLU(),self.lin2)
        
    def forward(self, x):
        x = self.features(x)
        x = self.classifier(x.view(x.size(0), -1))
        return x
convnet=ConvNet().to(device)
convnet.name="1stConv-"+time.asctime()
convnet_avg = ConvNet(nn.AvgPool2d).to(device)
convnet_avg.name="1stConv-pool-"+time.asctime()