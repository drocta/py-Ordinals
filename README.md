# py-Ordinals
Handles Hessenberg natural addition, multiplication, and compairison of ordinal numbers. Uses Cantor Normal Form.

The base file, ordinals.py, supports ordinals less than Epsilon(0).
Using epsilon.py instead also supports ordinals less than phi(2,0).
Using veblen.py instead allows for representing any ordinal number less than the small veblen ordinal, barring limitations on memory.
However, there are probably bugs in veblen.py. Using only the two parametr veblen function is more likely to not have bugs, and this allows representing ordinals less than the Feferman–Schütte ordinal , Γ_0 .

If you are using only the base ordinals.py:

To use, just import ordinals, and use w from it.
If you grab w from the ordinals file, whatever arithmetic you want to do based on that should work.

from ordinals import Ordinal, w
should do the trick. Then you can do whatever you want with w (which stands for omega) , whether it be adding, multiplying, raising to powers, comparing, casting to string, or what have you.

This is an early version, so it may have bugs.
I don't know of any bugs in it yet though, and it seems to work pretty well.

If you need larger ordinals of size at least epsilon_0 , instead of importing ordinals.py, instead use veblen.py

To use veblen.py, import whatever things you need from veblen.py.

"from veblen import *"

should work fine.

This lets you use Epsilon(whatever ordinal you want) , as well as w , and also lets you use the extended veblen function, phi.
the Veblen function phi takes any number of arguments, wbich should all be either ordinals, or non-negative int s or long s.
For how the extended veblen function works, see the wikipedia article on the same, as that is what this is based on.

I hope this can be of use to someone.

If the license is a problem for you, please ask, and I'll try to see if we can work something out. However, I don't anticipate it being a problem, if I understand the license correctly.

Issues, pull requests, etc. are welcome.
