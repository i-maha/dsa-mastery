class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen_index = {}
        window_start = 0
        max_length = 0
        for window_end, current_character in enumerate(s):
            if current_character in last_seen_index:
                window_start = max(window_start, last_seen_index[current_character] + 1)
            last_seen_index[current_character] = window_end
            current_window_length = window_end - window_start + 1
            max_length = max(max_length, current_window_length)
        return max_length
