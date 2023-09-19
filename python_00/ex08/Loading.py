def ft_tqdm(iterable):
    """
        yield returns value back to caller but retains enough state
        to resume where the function left of

        total = max range number
        length = progress bar

        /r returns the cursor to the beginning of the line
        division using // will return int
    """

    if iterable is None:
        total = 100
    else:
        total = len(iterable)

    length = 100

    for item in iterable:
        num = item + 1
        yield item
        progress = (length * num // total)
        bar = "=" * progress + "-" * (length - progress)

        print(f"{progress}%[{bar}] {num}/{total}", end="\r")
    bar = "=" * (length - 1) + ">"
    print(f"{progress}%[{bar}] {num}/{total}", end="\r")
