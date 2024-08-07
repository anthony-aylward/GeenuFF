# GeenuFF
Schema and API for a relational db that encodes gene models in an explicit, structured, and robust fashion.

## Installation

```sh
conda env create -f rare-geenuff-conda-env.yml
conda activate rare-geenuff
pip install rare-geenuff
```

Contents of `rare-geenuff-conda-env.yml`:

```yaml
name: rare-geenuff
channels:
  - conda-forge
  - bioconda
dependencies:
  - intervaltree>=3.0.2
  - SQLAlchemy<2,>=1.3.12
  - numpy>=1.18.1
  - pandas
  - biopython
  - pyyaml
```

## beta disclaimer

GeenuFF is currently _extremely_ beta and very unstable. 
We're keen to get feed back or ideas from the community
(even if it's just whether you think this could be useful to you
if developed further), but if you build on GeenuFF as it is now, 
you're doing so at your own risk.

## Motivation
We developed this to provide a way of unambiguously encoding gene models, 
(the way the DNA sequence is interpreted to produce proteins) that is both
robust to partial information and biological complexity.

A more extensive description can be found [here](https://weberlab-hhu.github.io/GeenuFF/).

## Unit tests
```bash
conda install -c conda-forge pytest
git clone -b rare --single-branch https://github.com/anthony-aylward/GeenuFF.git
cd GeenuFF
pytest
```

## usage
You can run `bash example.sh` for a quick start with public data.
 This will setup the folder 'three_algae', download public data in
 the expected format, and import it into a geenuff spec db for each
species. For more information please see 
[the api docs](https://weberlab-hhu.github.io/GeenuFF/api.html).

## Major plans
* Add a validation module to check structure of gene models.
* Add extraction of raw & mature transcript, CDS, and protein sequence as a demo application.
* Visualization.

## Thanks

To @janinamass for discussion and advice.
