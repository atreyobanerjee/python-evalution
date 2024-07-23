# python-evalution

The script justify.py takes two command-line arguments: a paragraph string and a paragraph width. It then outputs the justified text as an array of strings.

```
python justify.py --paragraph-string "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works." --paragraph-width 20
```

Output for this code will be:

```
Array [1] = "This  is  a  sample"
Array [2] = "text   but   a"
Array [3] = "complicated problem"
Array [4] = "to  be  solved, so we"
Array [5] = "are adding more text"
Array [6] = "to   see   that  it"
Array [7] = "actually     works."
```

Some more test cases:

```
python3 justify.py --paragraph-string "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam." 
--paragraph-width 20
```

output for this code:

```
Array [1] = "Lorem   ipsum  dolor"
Array [2] = "sit            amet,"
Array [3] = "consectetur         "
Array [4] = "adipiscing     elit."
Array [5] = "Integer   nec  odio."
Array [6] = "Praesent libero. Sed"
Array [7] = "cursus  ante dapibus"
Array [8] = "diam.               "
```

some more with width as 15:

```
python3 justify.py --paragraph-string "The quick brown fox jumps over the lazy dog." --paragraph-width 15
```

```
Array [1] = "The quick brown"
Array [2] = "fox  jumps over"
Array [3] = "the  lazy  dog."
```
