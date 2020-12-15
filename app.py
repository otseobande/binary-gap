def binary_gap(number: int):
    if number < 1 or number > 2_147_483_647:
        raise Exception('Number is out or range (1 to 2,147,483,647)')

    bin_num = bin(number)[2:]
    bin_values = list(bin_num)

    gaps = []
    current_gap_count = 0
    gap_started = False

    for val in bin_values:
        if val == '1':
            if gap_started:
                gaps.append(current_gap_count)
                gap_started = False
            else:
                gap_started = True
        elif gap_started:
            current_gap_count += 1

    return max(gaps) if len(gaps) > 0 else 0

