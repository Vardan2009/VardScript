# VardScript Programming Language
![Logo](/imgs/vardscript_text_new.png)
A simple, dynamically-typed, functional programming language.
![SampleScreenshot](/imgs/sample2.png)
## How to use
Create a .vard file and run it by running vard.py with an argument as the filepath (or just run shell.py for the shell)
```
py vard.py path/to.file.vard
```
## Comments
Comments are started with a colon ("`:`") and are ignored by the interpreter
```
:this is a comment
```
## Output
### `out()` function
```
out("Hello World!")
```
## Input
### `in()` function
```
out("You Wrote: "+in())
```
### `inint()` function
```
out("Your chosen number:"+inint()
```
## Variables
```
set e = 10
out(e)

set list = [1,2,3]
out(select(list,1)) :select selects the n-th value from the list

set isDone = true
out(isDone) :prints out `1` as in `true`

set name = in() :name == whatever in() returns
out("Hello, "+name+"!")
```
## Functions
### Built-in Functions
#### `isnum(arg)`,`isstr(arg)`,`isfunc(arg)`,`islist(arg)`
- Checks data type of whatever is given
#### `append(list,arg)`, `pop(list,index)`,`ext(list1,list2)`,`len(list)`
- List operations
#### `halt()`
- halts program
#### `include(libfilename)`
- includes a library from 'libraries' folder
```
:example with stdlib
include("std.vard")
```
#### `include(filepath)`
- runs other .vard code
### Custom functions
#### Definition
```
func funcname(arg1,arg2)
    :code
end
```
### Calling Functions
```
funcname(arg1,arg2)
```
## `if`,`elseif`,`else`
```
if statement then
    :code
elseif otherstatement then
    :othercode
else
    :othercode
end
```
## Loops
### `for` loops
```
set alphabet = ["a","b","c","d"]
for i=0 until len(alphabet) then
    out(select(alphabet,i))
end
```

Based on [davidcallanan's BASIC interpreter](https://github.com/davidcallanan/py-myopl-code/tree/master?tab=readme-ov-file)
