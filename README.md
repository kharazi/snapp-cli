# Snapp Cli 


[![asciicast](https://asciinema.org/a/4LMxOtcPPQDZQI8xpXdck1059.png)](https://asciinema.org/a/4LMxOtcPPQDZQI8xpXdck1059)

`snapp-cli` is a command-line interface for [Snapp](https://en.wikipedia.org/wiki/Snapp_(company)) that emphasizes your **PRIVACY**:). request a ride with Snapp like a boss!

## Installation

```
$ cd mapscii
$ npm install -g
$ cd ..
$ pip install -r requirements.pip
```

## Usage 

```
Usage: ride.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  login  Login to your Snapp account
  price  Calculate price of a trip
  ride   Compelete this function to take a ride with...
```

an example:

```
$ python ride.py price --source 35.70071439856985 51.39509439468384 --destination 35.70364178950393 51.39932155609131

+-----------+-------+----------+
| Service   | Price | Distance |
+-----------+-------+----------+
| اسنپ اکو  | 40000 | 731      |
| اسنپ رُز  | 40000 | 731      |
| اسنپ باکس | 30000 | 731      |
| اسنپ بایک | 45000 | 731      |
+-----------+-------+----------+
```
