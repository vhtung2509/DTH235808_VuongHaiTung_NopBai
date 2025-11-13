from os import path
def DocFile(tenFile):
    if not path.exists(tenFile):
        return []
    with open(tenFile, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

def GhiFile(tenFile, arrLines):
    with open(tenFile, 'w', encoding='utf-8') as f:
        for line in arrLines:
            f.write(line + '\n')
            
            