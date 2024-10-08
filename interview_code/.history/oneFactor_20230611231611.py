#%%
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
# %%
close = pd.read_csv("close.csv", index_col=0)
print(close.shape)
print(close.index)
print(close.columns)
# %% Problem 1
r = close.shift(-5) / close - 1
r0 = close / close.shift(1) - 1

# %%
factor1 = r0.rolling(window=10,min_periods=1).mean() 
# %%
factor2 = r0.apply(lambda x: x.rank(ascending=False,na_option='keep') / x.count(), axis=1)
# %%
factor3 = r0.rolling(10, min_periods=1).apply(lambda x: pd.Series(x).rank(ascending=False,na_option='keep').iloc[-1] / x.count())
# %%
weights = np.arange(0.1, 1.1, 0.1)  # 权重数组 [1, 0.9, ..., 0.1]
factor4 = r0.rolling(10, min_periods=1).apply(lambda x: np.sum(x.fillna(0) * weights[:x.shape[0]]))
# %%
factors = { "factor1": factor1, "factor2": factor2, "factor3": factor3, "factor4": factor4,}
for name, factor in factors.items():
    factor.to_csv(f"{name}.csv")
    print(f"{name}: coverage={factor.count().mean() / factor.shape[0]}")  
# %% Problem2
# 计算每个因子相对于r的IC
ic_factor1 = factor1.corrwith(r)
ic_factor2 = factor2.corrwith(r)
ic_factor3 = factor3.corrwith(r)
ic_factor4 = factor4.corrwith(r)

# 计算IC时间序列的均值和方差
ic_mean = pd.DataFrame([ic_factor1.mean(), ic_factor2.mean(), ic_factor3.mean(), ic_factor4.mean()], columns=['Mean'], index=['factor1', 'factor2', 'factor3', 'factor4'])
ic_std = pd.DataFrame([ic_factor1.std(), ic_factor2.std(), ic_factor3.std(), ic_factor4.std()], columns=['Std'], index=['factor1', 'factor2', 'factor3', 'factor4'])

# 打印结果
print("factor1: mean={} std={}".format(ic_mean.loc['factor1']['Mean'], ic_std.loc['factor1']['Std']))
print("factor2: mean={} std={}".format(ic_mean.loc['factor2']['Mean'], ic_std.loc['factor2']['Std']))
print("factor3: mean={} std={}".format(ic_mean.loc['factor3']['Mean'], ic_std.loc['factor3']['Std']))
print("factor4: mean={} std={}".format(ic_mean.loc['factor4']['Mean'], ic_std.loc['factor4']['Std']))

# %% Problem3
#factor1
# 去极值
lower_bound = factor1.quantile(0.02, axis=1)  # 每个横截面的下界，2%分位数
upper_bound = factor1.quantile(0.98, axis=1)  # 每个横截面的上界，98%分位数
factor1 = np.where(factor1 > upper_bound.to_numpy()[:, np.newaxis], upper_bound.to_numpy()[:, np.newaxis], factor1)  # 超过上界的赋值为上界
factor1 = np.where(factor1 < lower_bound.to_numpy()[:, np.newaxis], lower_bound.to_numpy()[:, np.newaxis], factor1)  # 低于下界的赋值为下界

# 标准化
factor1_mean = np.nanmean(factor1,axis=1)  # 每个横截面的均值
factor1_std = np.nanstd(factor1,axis=1)  # 每个横截面的标准差
factor1 = (factor1 - factor1_mean[:, np.newaxis]) / factor1_std[:, np.newaxis]  # 标准化

# 创建处理后的因子矩阵
factor = pd.DataFrame(factor1, index=close.index, columns=close.columns)

# 打印结果
print(factor)
factor.to_csv("processed_factor.csv")

# %%
close = close.iloc[10:, :]
factor = factor.iloc[10:, :]
print(close.shape)
# %% Problem4
# 选出所有 factor > 0 且 close 有值的股票
selected_stocks = (factor > 0) & close.notna()
print(selected_stocks)
# 初始化持股数矩阵
holding = pd.DataFrame(0, index=close.index, columns=close.columns)

for date in holding.index:
    if date == holding.index[0]:
        # 第一天，将每股分配金额除以股价得到持股数
        cash_per_stock = 1 / selected_stocks.loc[date].sum()  # 初始每股分配金额
        holding.loc[date] = selected_stocks.loc[date] * ((cash_per_stock / close.loc[date]).fillna(0))
    else:
        # 之后的每一天
        sell_mask = (close.loc[date].notna()) & (prev_holding > 0)
        holding.loc[date] += (1- sell_mask) * prev_holding # 没卖的不动
        cash = (sell_mask * prev_holding * close.loc[date]).sum()  # 计算卖出后的现金
        num_selected_stocks = selected_stocks.loc[date].sum()
        if num_selected_stocks > 0:
            cash_per_stock = cash / num_selected_stocks  # 计算每股分配金额
            holding.loc[date] += selected_stocks.loc[date] * ((cash_per_stock / close.loc[date]).fillna(0))
        
        # print(date,"@@@",num_selected_stocks,"cash",cash)
      
    prev_holding = holding.loc[date]
   
# 打印结果
# print(holding)
# holding.to_csv("holding.csv")
equity = (holding * close.ffill()).sum(axis=1)
plt.plot(equity.values)

# %% Problem5
# 计算每日收益率
daily_return = equity / equity.shift(1) - 1

# 计算年化收益率
annual_return = daily_return.mean() * 250

# 计算最大回撤率
cumulative_return = equity / equity.iloc[0]
max_drawdown = np.max(np.maximum.accumulate(cumulative_return) - cumulative_return)

# 计算日化收益率的夏普比率
daily_std = daily_return.std()
sharpe_ratio_daily = annual_return / daily_std

# 计算年化收益率的夏普比率
sharpe_ratio_annual = np.sqrt(250) * sharpe_ratio_daily

# 打印结果
print(f"年化收益率={annual_return}")
print(f"最大回撤率={max_drawdown}")
print(f"日化收益率的夏普比率={sharpe_ratio_daily}")
print(f"年化收益率的夏普比率={sharpe_ratio_annual}")


# %% Problem7
from scipy.optimize import minimize ,differential_evolution,NonlinearConstraint
import time
t0= time.time()

# 定义目标函数
def objective(weights):
    def strategy(factor):
        factor = factor.iloc[10:, :]
        selected_stocks = (factor > 0) & close.notna()
        # print(selected_stocks)
        # 初始化持股数矩阵
        holding = pd.DataFrame(0, index=close.index, columns=close.columns)

        for date in holding.index:
            if date == holding.index[0]:
                # 第一天，将每股分配金额除以股价得到持股数
                cash_per_stock = 1 / selected_stocks.loc[date].sum()  # 初始每股分配金额
                holding.loc[date] = selected_stocks.loc[date] * ((cash_per_stock / close.loc[date]).fillna(0))
            else:
                # 之后的每一天
                sell_mask = (close.loc[date].notna()) & (prev_holding > 0)
                holding.loc[date] += (1- sell_mask) * prev_holding # 没卖的不动
                cash = (sell_mask * prev_holding * close.loc[date]).sum()  # 计算卖出后的现金
                num_selected_stocks = selected_stocks.loc[date].sum()
                if num_selected_stocks > 0:
                    cash_per_stock = cash / num_selected_stocks  # 计算每股分配金额
                    holding.loc[date] += selected_stocks.loc[date] * ((cash_per_stock / close.loc[date]).fillna(0))

                # print(date,"@@@",num_selected_stocks,"cash",cash)

            prev_holding = holding.loc[date]

        # 打印结果
        # print(holding)
        # holding.to_csv("holding.csv")
        equity = (holding * close.ffill()).sum(axis=1)
        return equity
    
    factor = sum([
        weights[0] * r0.rolling(2, min_periods=1).mean(),
        weights[1] * r0.rolling(4, min_periods=1).mean(),
        weights[2] * r0.rolling(8, min_periods=1).mean(),
        weights[3] * r0.rolling(16, min_periods=1).mean(),
        weights[4] * r0.rolling(32, min_periods=1).mean()
    ])
    equity = strategy(factor)
    daily_return = equity / equity.shift(1) - 1
    annual_return = daily_return.mean() * 250
    daily_volatility = daily_return.std()
    annual_volatility = daily_volatility * np.sqrt(250)
    sharpe_ratio = annual_return / annual_volatility
    print(sharpe_ratio)
    print("time",time.time()-t0)
    print(weights)
    return -sharpe_ratio  # 目标是最大化夏普比率

def equality_constraint(x):
    # 这里假设有两个参数 x1 和 x2，满足等式约束 x1 + x2 = 1
    return np.sum(np.abs(x)) - 1
equality = NonlinearConstraint(equality_constraint, 0, 0)
bounds = [(-1, 1)] * 5
result = differential_evolution(objective, bounds,constraints=(equality))
print(result.x), print(result.fun)
print(result)
'''
# 初始化权重
initial_weights = np.array([0.1, 0.2, 0.3, 0.3, 0.1])

# 定义约束条件：权重的绝对值之和为1
constraint = {'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1}#np.sum(np.abs(weights)) - 1

# 定义边界条件：每个权重的取值范围为[-1, 1]
bounds = [(-1, 1)] * len(initial_weights)

# 使用梯度下降法寻找最优解
result = minimize(objective, initial_weights, method='SLSQP',bounds=bounds, constraints=constraint,tol=1e-8)

# 提取最优权重
optimal_weights = result.x

print("最优权重:", optimal_weights)
'''
#%%
#导入sympy包，用于求导，方程组求解等等
from sympy import * 
 
#设置变量

x1,x2,x3,x4,x5 = symbols("x1"),symbols("x2"),symbols("x3"),symbols("x4"),symbols("x5")
alpha = symbols("alpha")
weights = (x1,x2,x3,x4,x5)
 
#构造拉格朗日等式
L = objective(weights) + alpha * np.sum(np.abs(weights))
 
#求导，构造KKT条件
difyL_x1 = diff(L, x1) #对变量x1求导
difyL_x2 = diff(L, x2) #对变量x2求导
difyL_x3 = diff(L, x3)
difyL_x4 = diff(L, x4)
difyL_x5 = diff(L, x5)
difyL_beta = diff(L, beta) #对乘子beta求导
dualCpt = alpha * np.sum(np.abs(weights)) #对偶互补条件
 
#求解KKT等式
aa = solve([difyL_x1, difyL_x2, difyL_beta, dualCpt], [x1, x2, alpha, beta])
 
#打印结果，还需验证alpha>=0和不等式约束<=0
for i in aa:
 if i[2] >= 0:
    if (i[0]**2 - i[1]) <= 0:
        print(i)



# %%
