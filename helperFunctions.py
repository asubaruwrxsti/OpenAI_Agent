def loadEnv(file=".env"):
    # Load environment variables as a dictionary
    env = {}
    with open(f"{file}", "r") as f:
        for line in f:
            if line[0] != '#':
                key, value = line.strip().split('=')
                env[key] = value
    return env
