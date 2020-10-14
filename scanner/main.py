from domain.SymbolTable import ST

identifiers = ['a', 'b', 'ab', 'ba']
constants = ['1', '2', '3', '"123"']
everything = identifiers + constants
size = 17

st = ST(size)

for x in everything:
    st.add(x)

print(st)

assert (st.getPosition('ab') == (14, 0))
assert (st.getPosition('ba') == (14, 1))
assert (st.contains('"123"') is True)
print("Tests passed")