from clone_tinyphysics import run
from sko.PSO import PSO
import json

def main():
    print("Hello from controls-challenge!")
    tmp = run()
    print(tmp["total_cost"])

    def demo_func(x):
        x1,x2,x3 = x
        param_dict = {
            "p":x1,
            "i":x2,
            "d":x3
        }
        with open('config.json', 'w') as jsonfile:
            print(param_dict)
            json.dump(param_dict, jsonfile)
        print(x1,x2,x3)
        return run()["total_cost"]

    pso = PSO(func=demo_func, n_dim=3, pop=10, max_iter=5, lb=[0.25, 0, -0.15], ub=[0.35, 0.1, 0], w=0.8, c1=0.5, c2=0.5)
    pso.run()
    print('best_x is ', pso.gbest_x, 'best_y is', pso.gbest_y)


    
if __name__ == "__main__":
    main()
