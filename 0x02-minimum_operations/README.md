# Minimum Operations

In a text file, there is a single character ``H``. Your text editor can execute only two operations in this file: ``Copy All`` and ``Paste``. Given a number ``n``, write a method that calculates the fewest number of operations needed to result in exactly ``n H`` characters in the file.

## Aproach
We can break our moves into groups of (copy, paste, ..., paste). Let ``C`` denote copying and P denote pasting. Then for example, in the sequence of moves ``CPPCPPPPCP``, the groups would be ```[CPP][CPPPP][CP]```.

Say these groups have lengths ``g_1, g_2, ....`` After parsing the first group, there are ``g_1`` 'A's. After parsing the second group, there are ``g_1 * g_2`` 'A's, and so on. At the end, there are ``g_1 * g_2 * ... * g_n`` 'A's.

We want exactly ```N = g_1 * g_2 * ... * g_n```. If any of the ``g_i`` are composite, say ``g_i = p * q``, then we can split this group into two groups (the first of which has one copy followed by ``p-1`` pastes, while the second group having one copy and ``q-1`` pastes).

Such a split never uses more moves: we use ``p+q`` moves when splitting, and ``pq`` moves previously. As ``p+q <= pq`` is equivalent to ``1 <= (p-1)(q-1)``, which is true as long as p >= 2 and q >= 2.

<b>Algorithm By</b> the above argument, we can suppose g_1, g_2, ... is the prime factorization of N, and the answer is therefore the sum of these prime factors.