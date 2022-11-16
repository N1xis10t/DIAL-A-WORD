

<span style="text-align:center">* DIAL-A-WORD *</span>
<span style="text-align:center">Copyright (c) 2022 N1xis10t</span> 


ABSTRACT

This software is for finding words in phone numbers (like 888-EYES) that
you see government agencies and others using. Now, I'm pretty sure that they
just pay the telephone companies extra so that they get special phone numbers.
The idea behind this software is to provide the user with the ability to
aquire numbers like that without paying extra.


FUNCTIONALITY

When you are setting up a phone line with the telephone company, what
they typically do is give you an option to choose a randomly selected phone
number, or have them randomly select another one. When they present you with
a number, feed it into this program with no dashes or special characters
(like xxx5243373 where "xxx" is an area code) and it will search the number to
see if it has any words in it. If it does, it will show you what the number
is in the format "xxx5-CHEESE". If it doesn't find anything, or if you don't
like what it did find, have them show you another number and then check it.
Repeat this until you find one that you like, or until the technician gets
fed up with you.


DEPENDENCIES

This software requires that the file "google-10000-english.txt" be in the same
folder. This is a file that has the 10000 most common english words in it,
and can easily be found on the Internet. I have limited this program to such
a small dictionary because the running time is simply too long to be practical
when you try to use an exhaustive list of English words. Feel free to try to
use a better dictionary.


NOTES

This software cannot find words that are less than three characters long, as a
side effect of having to filter out garbage words from the dictionary. This
could be fixed by removing the filter and using a better dictionary.

This software is only 7 Kilobytes in size (not including the dictionary),
and would easily fit on a 5.25 inch floppy disk.


COPYRIGHT NOTICE

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

