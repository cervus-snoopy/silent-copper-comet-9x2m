import os

ENTRY = "I texted my dad 'I got hired!' \u2014 autocorrect sent 'I got fired!' and he drove six hours to pick me up."


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    os.chmod(out_dir, 0o755)


if __name__ == "__main__":
    main()
