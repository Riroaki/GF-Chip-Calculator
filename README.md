# GF Chip Calculator
> A simple tool that reads chip storing code of the game Girls' Frontline
> and calculates best combinations that reaches the theoretical limits.
> 
> For study purposes mainly.

## Requirements
- numpy==1.16.2
- tqdm==4.38.0

## Usage
```shell script
python main.py --help
usage: Simple chip calculator, able to parse store code and calculate optimal combinations.
       [-h] [--limit LIMIT] [--input INPUT] [--output OUTPUT] [--type TYPE]

optional arguments:
  -h, --help            show this help message and exit
  --limit LIMIT, -l LIMIT
                        limit of solutions.
  --input INPUT, -i INPUT
                        name of input file containing store codes.
  --output OUTPUT, -o OUTPUT
                        name of output file containing results.
  --type TYPE, -t TYPE  name of hyper fire troop, e.g.: bgm-14.
```

The program calculates solutions for exact covering 
for all the hyper fire troops' cells first using
 Donald Knuth's [Algorithm X with Dancing Links](https://zh.wikipedia.org/wiki/%E8%88%9E%E8%B9%88%E9%93%BE).

Not all the solutions are captured, for the sake of efficiency.

The calculation still needs improvement `_(:_」∠)_`(quite slow), and maybe even bugly...

So welcome to report an issue if you have some new ideas to share!

For format of storing codes, see `sample.txt`.
You can get the storing codes using [rsyars](https://github.com/xxzl0130/rsyars).

## Speed
Processes about 20,000 solutions / sec.

However, each combinination set may have over 100,000 solutions...
so you may have a long time waiting for the result.

## Output format
```json5
[
  // List of solutions
  // Solution 1.
  [
    -36.0,  // Negative value of absolute difference
    -188785,  // Index of solution
    [
      // List of chips...
      {
        "color":"1",  // 1 means blue, while 2 means red
        "name":"551-11",  // Refer to data.py for its shape
        "enhance":0,  // Enhancement value
        "attrs":[
          1,  // Accuracy cell count
          3,  // Filling cell count
          1,  // Damage cell count
          0   // Destruction cell count
        ]
      },
      // ...more chips
    ]
  ],
  // ...more solutions
]
```

## TODO
- multiprocessing to fasten the processing