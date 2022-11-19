from collections import Counter


def get_minimum_window(original: str, check: str) -> str:
    count_check = Counter(check)
    count_subs = Counter()
    contained = dict()

    left, right = 0, 0
    subs = ""
    minsubs = ""

    while right < len(original):

        while len(contained) < len(count_check) and right < len(original):
            if original[right] in count_check:
                count_subs.update(original[right])

                if count_subs[original[right]] >= count_check[original[right]]:
                    contained[original[right]] = True
            right += 1

        while original[left] not in count_check or count_subs[original[left]] > count_check[original[left]]:
            if count_subs[original[left]] > count_check[original[left]]:
                count_subs[original[left]] -= 1
            left += 1

        if count_check == count_subs:
            subs = original[left:right]

        if len(subs) < len(minsubs) or len(minsubs) == 0:
            minsubs = subs
        elif len(subs) == len(minsubs):
            minsubs = min(subs, minsubs)

        count_subs[original[left]] -= 1
        if original[left] in contained:
            del contained[original[left]]
        left += 1

    return minsubs
