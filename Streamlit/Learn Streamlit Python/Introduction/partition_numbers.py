import streamlit as st
import pandas as pd

def pentagonal_i(i):
    return (3 * i ** 2 - i) / 2


def pentagonal_numbers_up_to_n(n):
    pents = []
    count = 1
    while True:
        p1 = int(pentagonal_i(count))
        if p1 <= n:
            pents.append(p1)
        else:
            break
        p2 = int(pentagonal_i(-count))
        if p2 <= n:
            pents.append(p2)
        else:
            break
        count += 1
    return pents


def partition_number_n_recursive(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        pents_up_to_n = pentagonal_numbers_up_to_n(n)
        signs = []
        setter = True
        for i in range(len(pents_up_to_n) // 2 + 1):
            if setter:
                signs += [1, 1]
            else:
                signs += [-1, -1]
            setter = not setter
        signs = signs[: len(pents_up_to_n)]
        recursive_calls = list(range(n + 1))[::-1]
        return sum([signs[i]*partition_number_n_recursive(recursive_calls[p]) for (i, p) in enumerate(pents_up_to_n)])



st.title("Partition Numbers")

partition_number_to_calc = st.number_input("Which partition number?", 1, 999, 13)

with st.expander("Recursive Solver"):
    try:
        sol = partition_number_n_recursive(partition_number_to_calc)
        st.write(sol)
    except Exception as e:
        st.exception(e) 


