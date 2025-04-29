"""
ArrayIntersection - Find intersection of two sorted arrays without duplicates.
"""

from typing import List


class ArrayIntersection:
    @staticmethod
    def intersect(arr1: List[int], arr2: List[int]) -> List[int]:
        i, j = 0, 0
        result = []

        while i < len(arr1) and j < len(arr2):
            if arr1[i] == arr2[j]:
                if not result or result[-1] != arr1[i]:
                    result.append(arr1[i])
                i += 1
                j += 1
            elif arr1[i] < arr2[j]:
                i += 1
            else:
                j += 1

        return result


if __name__ == "__main__":
    # Sample inputs
    arr1 = [1, 2, 2, 4, 5, 6]
    arr2 = [2, 2, 3, 5, 7]

    result = ArrayIntersection.intersect(arr1, arr2)
    print(f"Intersection: {result}")
