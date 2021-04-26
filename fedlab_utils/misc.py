import torch


def evaluate(model, criterion, test_loader, cuda):
    """
    Evaluate local model based on given test :class:`torch.DataLoader`

    Args:
        test_loader (torch.DataLoader): :class:`DataLoader` for evaluation
        cuda (bool): Use GPUs or not
    """
    model.eval()
    loss_sum = 0.0
    correct = 0.0
    total = 0.0
    with torch.no_grad():
        for inputs, labels in test_loader:
            if cuda:
                inputs = inputs.cuda()
                labels = labels.cuda()

            outputs = model(inputs)
            loss = criterion(outputs, labels)

            _, predicted = torch.max(outputs, 1)
            correct += torch.sum(predicted.eq(labels)).item()
            total += len(labels)
            loss_sum += loss.item()

    accuracy = correct / total
    # TODO: is it proper to use loss_sum here?? CrossEntropyLoss is averaged over each sample
    log_str = "Evaluate, Loss {}, accuracy: {}".format(loss_sum,
                                                       accuracy)
    print(log_str)


class Aggregators(object):

    @staticmethod
    def fedavg_aggregate(serialized_params_list):
        serialized_parameters = torch.mean(
            torch.stack(serialized_params_list), dim=0)
        return serialized_parameters
