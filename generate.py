import argparse
import random
import pickle
from itertools import accumulate


def write(path, res):
    f = open(path, 'w', encoding='utf8')
    f.write(res)
    f.close()
    # Writing answer in the specified location


def gen_word(m_dict, curr_seed):
    next_words_dict = m_dict[curr_seed]
    prob = list(next_words_dict.values())
    words = list(next_words_dict.keys())
    return str(random.choices(words, cum_weights=accumulate(prob), k=1)[0])
    # Generating new word by the specified seed


def find_rand_seed(m_dict):
    arr = list(m_dict.keys())
    return random.choice(arr)
    # Finding random seed through the list


def generate(args):
    random.seed()
    res = ''
    input_file = open(args.model, 'rb')
    main_dict = pickle.load(input_file)
    input_file.close()
    curr_seed = args.seed if args.seed else find_rand_seed(main_dict)
    for i in range(int(args.length)):
        res = res + ' ' + curr_seed
        new_seed = gen_word(main_dict, curr_seed)
        curr_seed = new_seed
    print(res) if not args.output else write(args.output, res)
    # Main function, which generates new sentences according to the dictionary of word pairs and frequencies


def parse_args():
    ln_help = 'Length of the generated sentence'
    mdl_help = 'Enter a directory, from where We can upload the Model'
    seed_help = 'This is a Word, from which We will start generating'
    out_help = 'This is a file, where We will save the result'
    parser = argparse.ArgumentParser(description='Enter "-h" for some help...')
    parser.add_argument('-length', '--length', default = None, help= ln_help, required=True)
    parser.add_argument('-model', '--model', default=None, help= mdl_help, required=True)
    parser.add_argument('-seed', '--seed', help=seed_help)
    parser.add_argument('-output', '--output', help=out_help)
    return parser.parse_args()
    # Parsing arguments from terminal


def main():
    args_namespace = parse_args()
    generate(args_namespace)


if __name__ == "__main__":
    main()
# generate_v2.0.py -model source/output/output -length 3
# ver. 2.0.5
