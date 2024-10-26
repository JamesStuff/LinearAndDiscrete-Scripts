# Linear and Discrete Scripts
These python scripts are intended to be used for making your life easier with LPSolve IDE.

## `lcm.py`
This was used for the ration constraints in `Cargo` and gets arround LPSolve not hainvg division.
This can also be achived using extra variables in LPSolve...

### Usage

```lp
❯ python lcm.py 12 18 10
Using:	Front = 12, Center = 18, Back = 10
	lcm=180

=== COPY AND PASTE BELOW ===
15f1 + 15f2 + 15f3 + 15f4  -  10c1 - 10c2 - 10c3 - 10c4 = 0;  /* F vs C */
15f1 + 15f2 + 15f3 + 15f4  -  18b1 - 18b2 - 18b3 - 18b4 = 0;  /* F vs B */
18b1 + 18b2 + 18b3 + 18b4  -  10c1 - 10c2 - 10c3 - 10c4 = 0;  /* B vs C */
```
## `ge-zeros.py`
Used to get greater then zero constraints for variables.

### Usage
```lp
❯ python ge-zeros.py x1 x2 x3 x4 u1 u2 v1 v2
x1 >= 0;
x2 >= 0;
x3 >= 0;
x4 >= 0;
u1 >= 0;
u2 >= 0;
v1 >= 0;
v2 >= 0;
```
