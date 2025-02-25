# Scream Cipher
Scream Cipher Encoder Decoder proposed by Randal Munroe https://xkcd.com/3054/

# Usage
python scream.py [encode|decode] text...

# Caveats
It doesn't work

# Testing
Here's a simple command line to see if it produces what one would expect:

    python scream.py decode `python scream.py encode ABCDEFGHIJKLMNOPQRSTUVWXYZ`

If it were to work correctly, it would output 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. Which it doesn't

# Look
I woke up at 6:30 am one tuesday monday, while on my winter holiday. 
I was browsing facebook on my phone in the bed. I saw this comic
and I was immediately nerd sniped. 

It's now 9:04 and I have learned more about diacritics 
than I ever needed or wanted to know. 

I'm just stopping here before I am accidentally learning about unicode too. Well, I already learned that it is way more complicated than I thought. And I have new appreciation to 
guys who write software that renders text.

Feel free to send PR's to improve on this! 
