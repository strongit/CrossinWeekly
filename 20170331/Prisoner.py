# Crossin 2017/03/31


def start_behavior(strategy):  # 根据不同策略确定第一轮的行为，0代表否认，1代表揭发
    if strategy == 'nice':
        return 0
    elif strategy == 'rat':
        return 1
    elif strategy == 'tit_for_tat':
        return 0
    elif strategy == 'my_strategy':
        return 1  # 这里自定义自己的策略


def update_behavior(strategy, behavior1, behavior2):  # 根据自己的策略、双方历史行为，确定下一轮的行为
    if strategy == 'nice':
        return 0
    elif strategy == 'rat':
        return 1
    elif strategy == 'tit_for_tat':
        return behavior2[-1]  # 以牙还牙，选择对方上一轮的行为
    elif strategy == 'my_strategy':
        return round(sum(behavior2)/len(behavior2))  # 这里自定义自己的策略
    
    
def step_result(behavior1, behavior2):  # 对于双方行为的四种组合，用一个式子算出双方要关几年
    return [-1*behavior1+4*behavior2-2*behavior1*behavior2+1, 4*behavior1-1*behavior2-2*behavior1*behavior2+1]


def prisoner_dilemma(N, strategy1, strategy2):  # N：轮数； Strategy1：主角策略； Strategy2：另一个人的策略
    result = [0, 0]  # 两个人判几年
    behavior = [[start_behavior(strategy1)], [start_behavior(strategy2)]]  # 第一轮选择
    for step in range(N):
        tmp_result = step_result(behavior[0][-1], behavior[1][-1])
        result[0] += tmp_result[0]  # 每一轮选择会导致主角判几年
        result[1] += tmp_result[1]  # 每一轮选择会导致另一个人判几年
        behavior[0].append(update_behavior(strategy1, behavior[0], behavior[1]))
        behavior[1].append(update_behavior(strategy2, behavior[1], behavior[0]))  # 每一轮行为会导致双方下一轮做出什么选择
    return (result[0], result[1])


if __name__ == '__main__':
    print(prisoner_dilemma(4, 'nice', 'nice'))
    print(prisoner_dilemma(5, 'rat', 'rat'))
    print(prisoner_dilemma(6, 'nice', 'rat'))
    print(prisoner_dilemma(4, 'rat', 'tit_for_tat'))
    print(prisoner_dilemma(7, 'tit_for_tat', 'tit_for_tat'))
    print('----------------')
    print(prisoner_dilemma(4, 'my_strategy', 'nice'))
    print(prisoner_dilemma(5, 'my_strategy', 'rat'))
    print(prisoner_dilemma(6, 'my_strategy', 'rat'))
    print(prisoner_dilemma(4, 'my_strategy', 'tit_for_tat'))
    print(prisoner_dilemma(7, 'my_strategy', 'tit_for_tat'))
