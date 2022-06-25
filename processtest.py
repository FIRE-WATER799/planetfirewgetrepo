import asyncio
async def run_command_shell(command):
    """Run command in subprocess (shell).

    Note:
        This can be used if you wish to execute e.g. "copy"
        on Windows, which can only be executed in the shell.
    """
    # Create subprocess
    process = await asyncio.create_subprocess_shell(
        command, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )

    # Status
    print("Started:", command, "(pid = " + str(process.pid) + ")", flush=True)

    # Wait for the subprocess to finish
    stdout, stderr = await process.communicate()

    # Progress
    if process.returncode == 0:
        print("Done:", command, "(pid = " + str(process.pid) + ")", flush=True)
    else:
        print(
            "Failed:", command, "(pid = " + str(process.pid) + ")", flush=True
        )

    # Result
    result = stdout.decode().strip()

    # Return stdout
    return result

output = asyncio.run(run_command_shell("java --version"))
print(output)
