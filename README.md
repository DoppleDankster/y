# Dota Tutorial Celebrity Randomizer


## Description

Takes a csv file as input with the name of each 'celebrity' and a list of title for each of them.
Randomly picks a name from the list for each celebrity and outputs the result to stdout in json format.


## Dependencies

you'll need pandas : `pip install pandas`

## How to run

``` sh
python3 ./randomize.py ./path/to/csv/file.csv
```


## Format of the CSV

An example is provided as a seperate file : example.csv

:warning: assuming that a user deliberatly chooses not to name some celebrities, leave the fields empty or set them to 'n/a'

example:

the 2nd line is missing an entry for sunsfan

```
# In csv format
SirActionSlacks,Purge,Sunsfan, Valkyrja
Windranger s turbo simp,TIL,The last Artifact player,The Slack Nullifier
YOU VE ALWAYS WANTED SOMETHING MORE,For those who don t know how it works,,P5 Slacks until the 25th of march
```

which is equivalent to : 

| SirActionSlacks | Purge | Sunsfan | Valkyrja
| -- | -- | -- | -- |
| Windranger's turbo simp | TIL | The last Artifact player | The Slack Nullifier
|YOU'VE ALWAYS WANTED SOMETHING MORE | For those who don't know how it works || P5's Slacks until the 25th of march

## Output

The output is passed to stdout if the script is called directly.
If you want to manipulate it from another python script call the method `run()`

Missing values are exposed as `n/a`

The output looks as follow: 

``` json
{
    "SirActionSlacks":"Windranger's turbo simp",
    "Purge": "TIL", 
    "Sunsfan": "n/a",
    "Valkyrja": "The Slack Nullifier"
}
```

