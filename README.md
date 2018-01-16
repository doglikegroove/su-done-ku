# su-done-ku
A sudoku solver written in python

Update 16 Jan:

Our solver is coming along, but it needs to learn how to cross reference between units. See here:

5___97__1

____63_94

____12___

_3__4_5__

94__2__36

__6_5__8_

___13____

17_28____

3__97___5

        5|       28|       34|       48|        9|        7|      238|        6|        1|
       27|      128|       17|        5|        6|        3|      278|        9|        4|
        6|        9|       34|       48|        1|        2|      378|        5|       78|
        8|        3|       17|        6|        4|       19|        5|       27|      279|
        9|        4|        5|        7|        2|        8|        1|        3|        6|
       27|       12|        6|        3|        5|       19|        4|        8|      279|
        4|        5|       28|        1|        3|        6|        9|       27|      278|
        1|        7|        9|        2|        8|        5|        6|        4|        3|
        3|        6|       28|        9|        7|        4|       28|        1|        5|
        

The upper left hand box ([0][0] thru [2][2]) needs a '7'. That '7' can only exist on row [1]. Therefore, the '278' combo
at [1][6] shouldn't have a '7' as a possibility.

Our solver needs to bounce information from one type of unit (box) off of another type (row). 

We're probably going to want to refactor the code to make removal a separate function for easy re-use.
