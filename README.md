# Snapp CLI

[![asciicast](https://asciinema.org/a/4LMxOtcPPQDZQI8xpXdck1059.png)](https://asciinema.org/a/4LMxOtcPPQDZQI8xpXdck1059)

`snapp-cli` is a command-line interface for [Snapp](https://en.wikipedia.org/wiki/Snapp_(company)) APIs that emphasizes your **PRIVACY**:). request a ride with Snapp like a boss!

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

for example to caclulate price of with geo points using this:

```
$ python ride.py ride --source 35.70071439856985 51.39509439468384 --destination 35.70364178950393 51.39932155609131
```
and for try it using command-line map type:
```
$ python ride.py ride --map
```
