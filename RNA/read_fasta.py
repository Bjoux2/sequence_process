def standardize_seq(seq):  # standardize seq: upper, and replace T with U
    seq_s = seq.upper().replace('T', 'U')
    for base in seq_s:
        if base not in ['A', 'U', 'G', 'C']:
            print 'Unknown character(s) in sequence except AUGC'
            break
    return seq_s


def read_fasta_file(fasta_file):  # convert fasta file to dic
    f = open(fasta_file)
    data = f.readlines()
    f.close()
    data_dic = {}
    record = []
    for i in range(len(data)):
        if data[i].startswith('>'):
            record.append(i)
    for i in range(len(record))[0:-1]:
        loc = record[i]
        loc_next = record[i+1]
        key = data[loc].replace('>', '').strip()
        value = ''
        for line in data[loc+1: loc_next]:
            value += line.strip()
        data_dic[key] = standardize_seq(value)

    key = data[record[-1]].replace('>', '').strip()  # the last block
    value = ''
    for line in data[record[-1]+1:]:
        value += line.strip()
    data_dic[key] = standardize_seq(value)
    return data_dic


if __name__ == "__main__":
    miRNA_dic = read_fasta_file('/home/thl/my_task/test_DeepMirTar/miRNA.fa')
    print miRNA_dic
