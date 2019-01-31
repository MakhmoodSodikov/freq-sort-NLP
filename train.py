import argparse
import re
import sys
import glob
import pickle


def print_model(res_d, output_f):
    pickle.dump(res_d, output_f, 2)
    # Here we write our model to the output directive in .pkl(?) format


def set_relation(w1, w2, d):
    d.setdefault(w1, {})
    d[w1][w2] = d[w1].get(w2, 0) + 1
    # This function increments frequency value for current words pair


def split_words(result_line, args, res_d, last_word):
    for i in range(len(result_line) - 1):
        elem1 = result_line[i]
        elem2 = result_line[i + 1]
        if args.lc:
            elem1 = elem1.lower()
            elem2 = elem2.lower()
        if last_word != '' and i == 0:
            set_relation(last_word, elem1, res_d)
        set_relation(elem1, elem2, res_d)
    # This procedure splits current line in file and calls the set_relation function


def order_std_line(line, args, word_re, res_d, last_word):
    res = re.findall(word_re, line)
    split_words(res, args, res_d, last_word)
    return res[-1]
    # This function works with current line from std_in stream and returns the last word of this line


def order_text_from_std(args, res_d):
    last_word = ''
    word_re = r'\w+'
    for line in sys.stdin:
        if line == '0\n':
            break
        last_word = order_std_line(line, args, word_re, res_d, last_word)
    # This function parses text from std_in


def order_file(input_file, word_re, args, res_d):
    last_word = ''
    with input_file:
        for line in input_file:
            if line != '':
                res = re.findall(word_re, line)
                split_words(res, args, res_d, last_word)
                last_word = res[-1]
    # This function orders current file from directory


def parse_from_path(args, res_d):
    files = glob.glob(pathname=''.join([args.input_dir, '\*']))
    # For glob's 'glob'-method the directory is to be specified by the mask;
    # User enters the name of the folder-directory,
    # and at this step we just add to the name of the directory the mask "\*",
    # for the correct glob's work
    for name in files:
        input_file = open(name, mode='r', encoding='utf8')
        word_re = r'\w+'  # Here we specify a pattern for the regular expression of a word
        order_file(input_file, word_re, args, res_d)
    # We will store in the format <word1> | <word2> = <quantity>, each new bundle from a new line


def parse_args():
    inp_dir_help = 'Enter a directory, where We can find a source'
    model_help = 'Enter a directory, where We can save the Model'
    lc_help = 'All letters will become lowercase'
    parser = argparse.ArgumentParser(description='Enter "-h" for some help...')
    parser.add_argument('-input_dir', '--input_dir', help=inp_dir_help)
    parser.add_argument('-model', '--model', default=None, help=model_help, required=True)
    parser.add_argument('-lc', '--lc', action="store_true", help=lc_help)
    return parser.parse_args()
    # This procedure parses arguments from terminal


def main():
    res_dict = {}
    args_namespace = parse_args()
    if args_namespace.input_dir:
        parse_from_path(args_namespace, res_dict)
    else:
        print("Exit code = 0")
        # Write '0\n' to stop reading from std in
        order_text_from_std(args_namespace, res_dict)
    output_file = open(args_namespace.model, 'wb')
    print_model(res_dict, output_file)
    output_file.close()


if __name__ == "__main__":
    main()
# train_v2.0.py -model source\output\output -input_dir source\input
# ver. 2.0
