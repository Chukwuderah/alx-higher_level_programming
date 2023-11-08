#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    m_dict = dict(a_dictionary)
    for k, v in m_dict.items():
        m_dict[k] = v * 2
    return m_dict
