"""
For this office hour, you will determine which of two strands of DNA is closest to a third strand.

Our recommendation for this office hour is to compare each strand character (nucleobase) by character, keeping track of the total "penalty" as you go.  This approach is known as computing the "edit distance" between strands. If the two strands of DNA have the same character, apply no penalty (0). If the two strands of DNA have different characters, apply a penalty of 1 (-1). If one of the strands has a gap (-) and the other has character, apply a penalty of 2 (-2). The DNA strand whose penalty is closest to 0 will be the "closest" to the target DNA strand.

strand1 = ["A", "T", "G", "C", "A", "T", "T", "C", "C", "A"]
strand2 = ["C", "T", "-", "C", "G", "-", "A", "A", "-", "C"]
strand3 = ["A", "T", "G", "C", "G", "T", "A", "A", "C", "-"]

Given the above 3 strands of DNA, determine which strand is more similar to strand2? (strand1 or strand3) I.e. Compare strand1 to strand2, then compare strand3 to strand2, and see which penalty is closer to 0.  Print out your result: "StrandX is most similar to strand2."  You may use unnested or nested loops for your solution, but keep in mind nested loops will provide a much shorter solution.
"""
