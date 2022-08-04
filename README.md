# Morse Code Converter

## Task

A text-based Python program to convert Strings into Morse Code.  

## Assignment

You will use what you've learnt to create a text-based (command line) program that takes any String input and converts it into Morse Code.  

You've created plenty of text-based programs in Days 1 -10, so look back at some of those projects if you don't remember what a text-base program looks like.  

[Wikipedia Entry for Morse Code](https://en.wikipedia.org/wiki/Morse_code)  

The design, functionality, code style is all up to you. You're wearing the big-girl/big-boy pants now. So you get to decide.  

## Summary

As I didn't want to create a morse code table myself, I touched web scraping as a first step. I decided to scrape an HTML page and saved the morse data as a JSON because of the dictionary format. This scraping will happen only if the JSON does not exist. I think key / value pairs are a great solution here because those can give you the convenience to search by key (letter) or loop through them and find keys based on values (code). I tried to tackle the project with OOP, however I'm not really sure if it does makes sense or not. The code won't be re-usable elsewhere as the project is too special in itself, but it is much more readable with OOP anyways.  

I tried to make the code foul-proof by handling possible errors and incorporate a handy menu where the user can choose between encode / decode / help or stop.  

My only concerns in my code are the for loops in the web scraping section: I think there should be a better way to solve that part, but I decided to do this way because the web scraping was just an extra step, didn't want to spend too much time on it.  

The hardest part was the web scraping for me, because a lot of pages are using JS for rendering. I had to find a site what I can use as a target and I had to target only specific pieces from it to not to mess up my JSON.  

I believe the morse encode / decode was pretty straightforward. The hardest was to find out and implement the convention for the letter spaces, etc.  

I believe I should use external libraries / more advanced Python functions more courageously in the future to expand my skills in that area.  

My biggest learning was to find out how the regex and exists module works.  

If I were to tackle this project again, I wouldn't spend too much time on web scraping as it is a task what has to be done only once in the first place. Maybe I would use more fancy Python functions, such as join, etc.  