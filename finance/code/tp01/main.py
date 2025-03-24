import math


def exercise1():
    print("\nExercise 1\n")
    p = [100 + i for i in range(13)]
    
    print("\nQuestion 1\n")
    monthly_returns = [(p[i] - p[i - 1]) / p[i - 1] for i in range(1, 13)]
    print(f"Monthly returns:")
    for r in monthly_returns:
        print(f"{100 * r:.2f}%")
    
    print("\nQuestion 2\n")
    ra = 1
    for r in monthly_returns: 
        ra *= 1 + r
    ra = ra - 1
    print(f"Annual return: {ra  * 100: .2f}%") 
    print(f"Sum of the monthly returns: {sum(monthly_returns) * 100: .2f}%") 
    
    print("\nQuestion 3\n")
    rm = (1 + ra) ** (1 / 12) - 1
    avg_m_returns = sum(monthly_returns) / 12
    print(f"Average monthly return: {rm * 100: .2f}%")
    print(f"Average of the monthly return: {avg_m_returns * 100: .2f}%")
    print(rm == avg_m_returns)
    if rm > avg_m_returns:
        print("Avg monthly return is bigger than the avg of THE monthly returns.")
    else:
        print("Avg of THE monthly returns is bigger than avg monthly return.")

def exercise2():
    print("\nExercise 2\n")
    pm0 = 85
    ps0 = 30
    pm1 = 90
    ps1 = 28

    print("\nQuestion 1\n")
    v0 = 10 * pm0 + 10 * ps0
    print(f"Initial value: {v0}")

    print("\nQuestion 2\n")
    alpham = 10 * pm0 / v0
    alphas = 10 * ps0 / v0
    print(f"alpha_msft = {alpham} and alpha_sbux = {alphas}")

    print("\nQuestion 3\n")
    rm = pm1 / pm0 - 1
    rs = ps1 / ps0 - 1
    print(f"One_period return of Microsoft: {rm * 100: .2f}%")
    print(f"One_period return of Starbucks: {rs * 100: .2f}%")
       
    print("\nQuestion 4\n")
    r = alpham * rm + alphas * rs
    print(f"One-period return of portfolio: {r * 100: .2f}%")
    v1 = v0 * (1 + r)
    print(f"New value: {v1}")

        
def exercise3():
    print("\nExercise 3\n")
    R = 4.5 / 100
    m = 2
    v0 = 10 ** 4
    fv = lambda n: v0 * (1 + R / m) ** (n * m) 

    print("\nQuestion 1")
    print(f"FV(1) = {fv(1)}")
    print(f"FV(5) = {fv(5)}")
    print(f"FV(10) = {fv(10)}")

    print("\nQuestion 2")
    init = lambda n: 10000 / ((1 + R / m) ** (n * m))
    print(f"Initial value to have 10000 in 1 year: {init(1)}")
    print(f"Initial value to have 10000 in 3 years: {init(3)}")
    print(f"Initial value to have 10000 in 10 years: {init(10)}")

    print("\nQuestion 3")
    fvinf = lambda n: v0 * math.exp(R * n)
    print(f"FV_inf(1) = {fvinf(1)}")

def main():
    exercise1()
    exercise2()
    exercise3()

if __name__ == "__main__":
    main()

