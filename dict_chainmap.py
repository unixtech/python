import os, argparse
from collections import ChainMap


def chainmap_example():
    defaults = {'user': 'guest', 'status': 'visitor'}
    env = os.environ
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user')
    parser.add_argument('-s', '--status')
    args_namespace = parser.parse_args()

    args_dict = {k: v for k, v in vars(args_namespace).items() if v is not None}
    # args_chain = ChainMap(args_dict, env, defaults)
    # args_dict = vars(args_namespace)
    print(args_dict)
    args_chain = ChainMap(args_dict, env, defaults)
    print(args_chain)
    print("User: ", args_chain['user'])
    print("Status: ", args_chain['status'])


if __name__ == '__main__':
    os.environ['user'] = 'Admin'
    os.environ['status'] = 'Owner'
    chainmap_example()
