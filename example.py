from argparse import ArgumentParser
import os
import ftplib

DATA_FTP = 'ftp.ensemblgenomes.org'
DATA_PATHS = (
    'pub/plants/release-47/fasta/chlamydomonas_reinhardtii/dna/Chlamydomonas_reinhardtii.Chlamydomonas_reinhardtii_v5.5.dna_sm.toplevel.fa.gz',
    'pub/plants/release-47/gff3/chlamydomonas_reinhardtii/Chlamydomonas_reinhardtii.Chlamydomonas_reinhardtii_v5.5.47.gff3.gz',
    'pub/plants/release-47/fasta/ostreococcus_lucimarinus/dna/Ostreococcus_lucimarinus.ASM9206v1.dna.toplevel.fa.gz',
    'pub/plants/release-47/gff3/ostreococcus_lucimarinus/Ostreococcus_lucimarinus.ASM9206v1.47.gff3.gz',
    'pub/plants/release-47/fasta/cyanidioschyzon_merolae/dna/Cyanidioschyzon_merolae.ASM9120v1.dna.toplevel.fa.gz',
    'pub/plants/release-47/gff3/cyanidioschyzon_merolae/Cyanidioschyzon_merolae.ASM9120v1.47.gff3.gz'
)

def parse_arguments():
    parser = ArgumentParser('GeenuFF example')
    parser.add_argument('-d', '--working-dir', default=os.getcwd())
    return parser.parse_args()


def main():
    args = parse_arguments()
    ftp = ftplib.FTP(DATA_FTP)
    ftp.login()
    for ftp_path in DATA_PATHS:
            with open(os.path.join(args.working_dir, os.path.basename(ftp_path)), "wb") as f:
                ftp.retrbinary(f"RETR {ftp_path}", f.write)




if __name__ == '__main__':
    main()
