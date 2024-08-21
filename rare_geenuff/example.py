from argparse import ArgumentParser
import os
import os.path
import ftplib
import shutil
import gzip
from subprocess import run

SPECIES=('Chlamydomonas_reinhardtii', 'Ostreococcus_lucimarinus', 'Cyanidioschyzon_merolae')
DATA_FTP = 'ftp.ensemblgenomes.org'
DATA_PATHS = (
    ('Chlamydomonas_reinhardtii', 'pub/plants/release-47/fasta/chlamydomonas_reinhardtii/dna/Chlamydomonas_reinhardtii.Chlamydomonas_reinhardtii_v5.5.dna_sm.toplevel.fa.gz'),
    ('Chlamydomonas_reinhardtii', 'pub/plants/release-47/gff3/chlamydomonas_reinhardtii/Chlamydomonas_reinhardtii.Chlamydomonas_reinhardtii_v5.5.47.gff3.gz'),
    ('Ostreococcus_lucimarinus', 'pub/plants/release-47/fasta/ostreococcus_lucimarinus/dna/Ostreococcus_lucimarinus.ASM9206v1.dna.toplevel.fa.gz'),
    ('Ostreococcus_lucimarinus', 'pub/plants/release-47/gff3/ostreococcus_lucimarinus/Ostreococcus_lucimarinus.ASM9206v1.47.gff3.gz'),
    ('Cyanidioschyzon_merolae', 'pub/plants/release-47/fasta/cyanidioschyzon_merolae/dna/Cyanidioschyzon_merolae.ASM9120v1.dna.toplevel.fa.gz'),
    ('Cyanidioschyzon_merolae', 'pub/plants/release-47/gff3/cyanidioschyzon_merolae/Cyanidioschyzon_merolae.ASM9120v1.47.gff3.gz')
)

def parse_arguments():
    parser = ArgumentParser('GeenuFF example')
    parser.add_argument('--working-dir', default=os.path.join(os.getcwd(), 'three_algae'))
    parser.add_argument('--download-example-data', action='store_true')
    return parser.parse_args()


def main():
    args = parse_arguments()
    # put the data in the format compatible with the --basedir parameter
    # basically --basedir needs a folder <your_species>
    # with a subfolder <your_species>/input containing a (compressed) gff3 annotation and fasta genome file.
    # The results will then be located in <your_species>/output
    # If desired, you can alternatively specify all file parameters individually
    # --gff3 <your.gff3> --fasta <your.fa> --db-path <your_output_genuff.sqlite3> --log-file <your_output.log>
    if args.download_example_data:
        if not os.path.isdir(args.working_dir):
            os.mkdir(args.working_dir)
        for sp in SPECIES:
            if not os.path.isdir(os.path.join(args.working_dir, sp)):
                os.mkdir(os.path.join(args.working_dir, sp))
            if not os.path.isdir(os.path.join(args.working_dir, sp, 'input')):
                os.mkdir(os.path.join(args.working_dir, sp, 'input'))
        ftp = ftplib.FTP(DATA_FTP)
        ftp.login()
        for species, ftp_path in DATA_PATHS:
            basename = os.path.basename(ftp_path)
            with open(os.path.join(args.working_dir, species, 'input', basename), "wb") as f:
                ftp.retrbinary(f"RETR {ftp_path}", f.write)
            with gzip.open(os.path.join(args.working_dir, species, 'input', basename), 'rb') as f_in, \
                open(os.path.join(args.working_dir, species, 'input', basename[:-3]), 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
            os.remove(os.path.join(args.working_dir, species, 'input', basename))
    for sp in SPECIES:
        run(('rare-geenuff-import', '--basedir', os.path.join(args.working_dir, sp),
             '--species', sp))


if __name__ == '__main__':
    main()
