# CMScrape - no gui
A Cardmarket scraper as a command line tool.
This will work with a linux OS only, because it uses command line to launch and install docker.

## Setup
```
sudo apt-get install libxml2-dev libxslt-dev docker
python -m pip install -r requirements.txt
```

**Note : Docker is also necessary but will be automatically installed upon running if not installed**

## Usage
```console
usage: run.py [-h] -i INPUT -o OUTPUT

Cardmarket information scraper from a list of links

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input file or url of the input file
  -o OUTPUT, --output OUTPUT
                        Output file
```

## Example
```console
python run.py -i pokemon_list.txt -o pokemon_out.csv
```
### Input file 
```
https://www.cardmarket.com/fr/Pokemon/Products/Singles/10th-Movie-Commemoration-Set/Alto-Mares-Latios?language=7&minCondition=2
https://www.cardmarket.com/fr/Pokemon/Products/Singles/10th-Movie-Commemoration-Set/Alto-Mares-Latias?language=7&minCondition=2
https://www.cardmarket.com/fr/Pokemon/Products/Singles/10th-Movie-Commemoration-Set/Timeless-Celebi?language=7&minCondition=2
https://www.cardmarket.com/fr/Pokemon/Products/Singles/10th-Movie-Commemoration-Set/Tree-of-Beginnings-Mew?language=7&minCondition=2
https://www.cardmarket.com/fr/Pokemon/Products/Singles/11th-Movie-Commemoration-Set/Pikachu-Lv10?language=7&minCondition=2
```

### Output file
| title                         | expansion                    | rarity | real from | from  | trend | 30 days | 7 days | 1 day  | url                                                                                                                                  | image name                                                        | image id |
|-------------------------------|------------------------------|--------|-----------|-------|-------|---------|--------|--------|--------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|----------|
| Alto Mare's Latios (10M)      | 10th Movie Commemoration Set | Promo  | 14.99     | 14.99 | 61.43 | 28.90   | 48.25  | 160.00 | https://www.cardmarket.com/fr/Pokemon/Products/Singles/10th-Movie-Commemoration-Set/Alto-Mares-Latios?language=7&minCondition=2      | https://product-images.s3.cardmarket.com/51/10M/566546/566546.jpg | 566546   |
| Alto Mare's Latias (10M)      | 10th Movie Commemoration Set | Promo  | 23.00     | 23.00 | 32.03 | 21.94   | 32.56  | 12.49  | https://www.cardmarket.com/fr/Pokemon/Products/Singles/10th-Movie-Commemoration-Set/Alto-Mares-Latias?language=7&minCondition=2      | https://product-images.s3.cardmarket.com/51/10M/566545/566545.jpg | 566545   |
| Timeless Celebi (10M)         | 10th Movie Commemoration Set | Promo  | 19.99     | 19.99 | 20.45 | 16.81   | 12.98  | 4.99   | https://www.cardmarket.com/fr/Pokemon/Products/Singles/10th-Movie-Commemoration-Set/Timeless-Celebi?language=7&minCondition=2        | https://product-images.s3.cardmarket.com/51/10M/566544/566544.jpg | 566544   |
| Tree of Beginning's Mew (10M) | 10th Movie Commemoration Set | Promo  | 24.50     | 24.50 | 41.46 | 30.75   | 29.16  | 19.94  | https://www.cardmarket.com/fr/Pokemon/Products/Singles/10th-Movie-Commemoration-Set/Tree-of-Beginnings-Mew?language=7&minCondition=2 | https://product-images.s3.cardmarket.com/51/10M/566549/566549.jpg | 566549   |
| Pikachu Lv.10 (11M 003)       | 11th Movie Commemoration Set | Promo  | 20.90     | 20.90 | 30.61 | 27.84   | 20.75  | 14.75  | https://www.cardmarket.com/fr/Pokemon/Products/Singles/11th-Movie-Commemoration-Set/Pikachu-Lv10?language=7&minCondition=2           | https://product-images.s3.cardmarket.com/51/11M/566532/566532.jpg | 566532   |
