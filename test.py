import torch
import torch.nn as nn
import torch.nn.functional as F

class LabelSmoothingLoss(nn.Module):
    def __init__(self, classes, smoothing=0.1, dim=-1):
        """
        初始化标签平滑损失函数。
        :param classes: 类别的总数。
        :param smoothing: 标签平滑的系数，默认为0.1。
        :param dim: 计算softmax的维度，默认为最后一个维度。
        """
        super(LabelSmoothingLoss, self).__init__()
        self.confidence = 1.0 - smoothing  # 置信度，即非平滑部分的权重
        self.smoothing = smoothing  # 平滑系数
        self.cls = classes  # 类别总数
        self.dim = dim  # softmax操作的维度

    def forward(self, pred, target):
        """
        计算标签平滑损失。
        :param pred: 模型的预测输出，未经softmax处理。
        :param target: 真实的标签。
        :return: 平滑损失的平均值。
        """
        # 对预测结果应用log softmax
        pred = pred.log_softmax(dim=self.dim)
        # 生成平滑的目标分布
        with torch.no_grad():
            true_dist = torch.zeros_like(pred)  # 创建与预测相同形状的张量
            # 对所有类别填充平滑值
            true_dist.fill_(self.smoothing / (self.cls - 1))
            # 在真实类别的位置上设置置信度
            true_dist.scatter_(1, target.data.unsqueeze(1), self.confidence)
        # 计算平滑损失
        return torch.mean(torch.sum(-true_dist * pred, dim=self.dim))

# 测试代码
def test_label_smoothing_loss():
    # 设置随机种子以获得可重复的结果
    torch.manual_seed(0)
    # 创建一个LabelSmoothingLoss实例
    label_smoothing_loss = LabelSmoothingLoss(classes=5, smoothing=0.1)
    # 随机生成一些模拟的预测值和真实标签
    preds = torch.randn(3, 5)  # 模拟的预测值（batch_size=3, num_classes=5）
    targets = torch.tensor([1, 0, 3])  # 真实标签
    # 计算标签平滑损失
    loss = label_smoothing_loss(preds, targets)
    print("Label Smoothing Loss:", loss.item())

# 运行测试
test_label_smoothing_loss()