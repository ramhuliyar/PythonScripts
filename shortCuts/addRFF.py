import re
import os

with open('igpSC.txt', 'r') as reader:
    rffAppend = '-rgFeatures {{feature::supported IxrIgpShortcut "Dut-C Dut-F"}}'
    with open('igpSCModified.txt', 'w') as writer:
        for line in reader:
            if re.match('registerTest', line):
                writer.write(line.rstrip() + ' ' + rffAppend + '\n')
            else:
                writer.write(line)

with open('igpSCModified.txt', 'r') as reader:
    for line in reader:
        print(line)


def str2unix(input_str: str) -> str:
    r"""
    Converts the string from \r\n line endings to \n

    Parameters
    ----------
    input_str
        The string whose line endings will be converted

    Returns
    -------
        The converted string
    """
    r_str = input_str.replace('\r\n', '\n')
    return r_str
        
