import torch

tensor1 = torch.randn(3, 10)  # 假设已经有一个 [2825, 300] 的张量
tensor2 = torch.randn(3, 10)

print(tensor1)
print(tensor2)
print(tensor1+tensor2)
# print(tensor)
# bool_vector = torch.tensor([True, False, False])  # 假设已经有一个 [2825] 维度的布尔向量

# mask = bool_vector.view(-1, 1).expand_as(tensor)  # 将布尔向量扩展为和张量相同的形状
# filtered_tensor = tensor.clone()  # 克隆原始张量，以保持维度不变
# filtered_tensor[mask] = 0  # 将不符合条件的行设置为0 zjo

# print(filtered_tensor.shape)  # 输出过滤后的张量的形状
# print(filtered_tensor)