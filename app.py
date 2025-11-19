"""
Binary Search Visualization
CISC-121 Project - Algorithm Visualizer
Author: Daniel Cheah
Date: November 2025

This application demonstrates a visual representation of the binary search algorithm.
"""

import gradio as gr


nums = [1,2,3,4,5,6,7,8,9,10]
target = 3

def binary_search(nums, target):
    
    if len(nums) == 0:
        return "Error: Array cannot be empty"
    
    if nums != sorted(nums):
        return "Error: Array must be sorted for binary search"
    
    left = 0, right = len(nums)-1, curr_step = 0

    while left <= right:
        curr_step += 1
        mid = (left + right) // 2

        step_info = {

        }
    

        if nums[mid] == target:
            print(f"Target: {target} found")
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

binary_search(nums, target)