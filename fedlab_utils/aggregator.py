# unfinished

import torch

class Aggregators(object):
    # 合并模型
    @staticmethod
    def fedavg_aggregate(serialized_params_list):
        serialized_parameters = torch.mean(
            torch.stack(serialized_params_list), dim=0)
        print("Aggregators.fedavg_aggregate:  merged shape ",serialized_parameters.shape)
        return serialized_parameters