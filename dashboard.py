import json
import os
import shlex
import subprocess

import pandas as pd
import streamlit as st

SCRIPT = "tracepoint:raw_syscalls:sys_enter { @[comm] = count(); } interval:s:5 { print(@); clear(@); }"


def exec(cmd):
    popen = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, universal_newlines=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)


def execute_and_listen_for_updates():

    st.title("Real-time syscalls counter")
    table_placeholder = st.empty()
    total_placeholder = st.empty()

    try:
        command = shlex.split("bpftrace -f json -e '{}'".format(SCRIPT))
        for entry in exec(command):
            entry = json.loads(entry)
            if entry["type"] == "map":
                data_dict = entry["data"]["@"]
                proc_names, counts = [], []
                total = 0
                for k, v in data_dict.items():
                    proc_names.append(k)
                    counts.append(v)
                    total += v

                df = pd.DataFrame(
                    {"counts": counts},
                    index=proc_names
                )

                table_placeholder.table(df)
                total_placeholder.text("total system calls: " + str(total))

    except Exception as e:
        print('internal error:', e)
        os._exit(0)


if __name__ == "__main__":
    execute_and_listen_for_updates()
