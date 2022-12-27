# Markdown to HTML

![meme](https://i.imgflip.com/3pw1vi.jpg)

# Description
Markdown is awesome! All your README.md are made in Markdown, but do you know how GitHub are rendering them?

It’s time to code a Markdown to HTML!

## Requirements
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7 or higher)
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `PEP 8` style (version 1.7.*)
- All your files must be executable
- All your modules should be documented: `python3 -c 'print(__import__("my_module").__doc__)'`
- Your code should not be executed when imported (by using `if __name__ == "__main__":`)

## Context

If we have this `README.md`:
```
# My title
- He**l**lo
- Bye

Hello

I'm **a** text
with __2 lines__

((I will live in Caracas))

But it's [[private]]

```

The content of our `README.html` should be:
```
<h1>My title</h1>
<ul>
<li>He<b>l</b>lo</li>
<li>Bye</li>
</ul>
<p>
Hello
</p>
<p>
I'm <b>a</b> text
<br/>
with <em>2 lines</em>
</p>
<p>
I will live in araas  ('c' and 'C' removed)
</p>
<p>
But it's 2c17c6393771ee3048ae34d6b380c5ec (converted in MD5(lowercase))
</p>
<p>
So cool!
</p>

```
