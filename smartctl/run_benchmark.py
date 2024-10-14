import json
import subprocess
from time import sleep

from typing import List


def run_program(i: int, file_name: str, interval: float) -> None:
    # compile_command2 = ["sudo", "smartctl", "-t", "short", "/dev/sda"]
    # subprocess.run(compile_command2, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
    compile_command = ["sudo", "smartctl", "-A", "-j", "/dev/sda"]
    output = subprocess.run(compile_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
    json_object = json.loads(output.stdout)
    prev = json_object["ata_smart_attributes"]["table"][4]['raw']['value']
    res = []

    for _ in range(i):
        # subprocess.run(compile_command2, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
        output = subprocess.run(compile_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
        json_object = json.loads(output.stdout)
        curr = json_object["ata_smart_attributes"]["table"][4]['raw']['value']
        res.append(curr - prev)
        prev = curr
        sleep(interval)

    with open(file_name, "w") as file:
        file.write(str(res))


if __name__ == "__main__":
    run_program(1000, "files_copyng_file2.txt", 0.01)
