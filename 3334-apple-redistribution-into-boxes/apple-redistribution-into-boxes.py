class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        capacity.sort(reverse=True)

        num_boxes = 0
        for box_size in capacity:
            if total_apples <= 0:
                break
            total_apples -= box_size
            num_boxes += 1

        return num_boxes