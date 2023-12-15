import torch

class MyNet(torch.nn.Module):
    def __init__(self):
        super(MyNet, self).__init__()
        self.fc = torch.nn.Linear(10, 1)  # 一个全连接层

    def forward(self, x):
        return self.fc(x)

def wow () : 
    mps_device = torch.device("mps")

    # Move your model to mps just like any other device
    model = MyNet()
    model.to(mps_device)

    # 创建一些示例输入数据
    x = torch.ones((1, 10)).to(mps_device)

    # Now every call runs on the GPU
    pred = model(x)
    # 打印预测值
    print(pred)

if not torch.backends.mps.is_available():
    if not torch.backends.mps.is_built():
        print("MPS not available because the current PyTorch install was not "
              "built with MPS enabled.")
    else:
        print("MPS not available because the current MacOS version is not 12.3+ "
              "and/or you do not have an MPS-enabled device on this machine.")

else:
    print("MPS is available!")
    wow()
