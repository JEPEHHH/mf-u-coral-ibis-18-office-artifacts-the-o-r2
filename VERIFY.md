# Verification

Run command used:

    MAKEFUN_OUTPUT_DIR="$PWD/verify_output" python3 main.py

Observed output of `entry.txt`:

- bytes: 147
- characters on the placard line: 146 (limit 180)
- nonblank UTF-8 text: yes
- content: Coronation stapler of the Lower Cubicle Dynasties, c. 2014 CE. Bronze, bone, and one stubborn staple. Donor: the intern who filed it under 'misc'.

Gate check (1-180 characters, not whitespace only): PASS.
The run was repeated and produced identical bytes; no network, keys or
packages are used. The temporary output directory was removed afterwards.
