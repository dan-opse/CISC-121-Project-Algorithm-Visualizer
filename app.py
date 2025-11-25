"""
Binary Search Visualization App
CISC-121 - Algorithm Visualizer
Author: Daniel Cheah
Date: November 25, 2025

This application demonstrates the Binary Search algorithm through
an interactive visualization using Gradio.
"""

import gradio as gr
import json

def binary_search_with_steps(nums, target):
    """
    Performs binary search and returns visualization data for each step.
    
    Args:
        array_str (str): Comma-separated numbers representing the sorted array
        target (str): The target value to search for
    
    Returns:
        tuple: (result_message, steps_html, complexity_info)
    """
    try:
        
        if len(nums) == 0:
            return "Error: Array cannot be empty", "", ""
        
        # Check if array is sorted
        if nums != sorted(nums):
            return "Error: Array must be sorted for binary search", "", ""
        
        # Perform binary search with step tracking
        steps = []
        left = 0
        right = len(nums) - 1
        found_index = -1
        step_num = 0
        
        while left <= right:
            step_num += 1
            mid = (left + right) // 2
            
            # Create visualization for current step
            step_info = {
                'step': step_num,
                'left': left,
                'right': right,
                'mid': mid,
                'mid_value': nums[mid],
                'array': nums.copy(),
                'comparing': f"Comparing middle element array[{mid}] = {nums[mid]} with target {target}"
            }
            
            if nums[mid] == target:
                found_index = mid
                step_info['result'] = f"✓ Found {target} at index {mid}!"
                steps.append(step_info)
                break
            elif nums[mid] < target:
                step_info['action'] = f"{nums[mid]} < {target}, search right half"
                steps.append(step_info)
                left = mid + 1
            else:
                step_info['action'] = f"{nums[mid]} > {target}, search left half"
                steps.append(step_info)
                right = mid - 1
        
        # Generate result message
        if found_index != -1:
            result = f"Success. Found {target} at index {found_index} in {step_num} steps."
        else:
            result = f"{target} not found in the array after {step_num} steps."
        
        # Generate HTML visualization
        steps_html = generate_steps_html(steps, nums, target, found_index)
        
        # Complexity analysis
        complexity_info = f"""
        ### Algorithm Analysis:
        - **Array size**: {len(nums)} elements
        - **Steps taken**: {step_num}
        - **Time Complexity**: O(log n) = O(log {len(nums)}) ≈ {step_num} maximum steps
        - **Space Complexity**: O(1) - uses constant extra space
        - **Best Case**: O(1) - target is at middle
        - **Worst Case**: O(log n) - target at end or not present
        """
        
        return result, steps_html, complexity_info
        
    except ValueError:
        return "Error: Please enter valid numbers", "", ""
    except Exception as e:
        return f"Error: {str(e)}", "", ""


def generate_steps_html(steps, array, target, found_index):
    """
    Generates HTML visualization for each step of binary search.
    
    Args:
        steps (list): List of step dictionaries
        array (list): The search array
        target (float): Target value
        found_index (int): Index where target was found (-1 if not found)
    
    Returns:
        str: HTML string with step-by-step visualization
    """
    html = "<div style='font-family: Arial, sans-serif;'>"
    
    for step in steps:
        html += f"<div style='margin: 20px 0; padding: 15px; background: #f0f8ff; border-left: 4px solid #4682b4; border-radius: 5px;'>"
        html += f"<h3 style='color: #2c3e50; margin-top: 0;'>Step {step['step']}</h3>"
        html += f"<p style='margin: 10px 0;'><strong>{step['comparing']}</strong></p>"
        
        # Visual array representation
        html += "<div style='display: flex; gap: 5px; margin: 15px 0; flex-wrap: wrap;'>"
        for i, val in enumerate(step['array']):
            # Determine box color based on position
            if i == step['mid']:
                color = '#ffd700'  # Gold for middle
                border = '3px solid #ff8c00'
            elif i >= step['left'] and i <= step['right']:
                color = '#87ceeb'  # Sky blue for search range
                border = '2px solid #4682b4'
            else:
                color = '#d3d3d3'  # Gray for excluded
                border = '2px solid #a9a9a9'
            
            html += f"""
            <div style='min-width: 50px; padding: 10px; background: {color}; 
                        border: {border}; border-radius: 5px; text-align: center;'>
                <div style='font-weight: bold; font-size: 16px;'>{val}</div>
                <div style='font-size: 10px; color: #666;'>idx {i}</div>
            </div>
            """
        html += "</div>"
        
        # Step information
        html += f"<p style='margin: 10px 0;'>"
        html += f"<span style='background: #87ceeb; padding: 3px 8px; border-radius: 3px; margin-right: 10px;'>Left: {step['left']}</span>"
        html += f"<span style='background: #ffd700; padding: 3px 8px; border-radius: 3px; margin-right: 10px;'>Mid: {step['mid']}</span>"
        html += f"<span style='background: #87ceeb; padding: 3px 8px; border-radius: 3px;'>Right: {step['right']}</span>"
        html += "</p>"
        
        # Action or result
        if 'result' in step:
            html += f"<p style='color: #28a745; font-weight: bold; font-size: 16px;'>{step['result']}</p>"
        elif 'action' in step:
            html += f"<p style='color: #333;'><em>{step['action']}</em></p>"
        
        html += "</div>"
    
    # Legend
    html += """
    <div style='margin: 20px 0; padding: 15px; background: #fff; border: 1px solid #ddd; border-radius: 5px;'>
        <h4>Legend:</h4>
        <div style='display: flex; gap: 20px; flex-wrap: wrap;'>
            <div><span style='display: inline-block; width: 20px; height: 20px; background: #87ceeb; border: 2px solid #4682b4; vertical-align: middle;'></span> Search Range</div>
            <div><span style='display: inline-block; width: 20px; height: 20px; background: #ffd700; border: 3px solid #ff8c00; vertical-align: middle;'></span> Middle Element (Current)</div>
            <div><span style='display: inline-block; width: 20px; height: 20px; background: #d3d3d3; border: 2px solid #a9a9a9; vertical-align: middle;'></span> Excluded Range</div>
        </div>
    </div>
    """
    
    html += "</div>"
    return html


# Create Gradio Interface
with gr.Blocks(title="Binary Search Visualizer", theme=gr.themes.Soft()) as app:
    gr.Markdown("""
    # 🔍 Binary Search Algorithm Visualizer
    
    **Binary Search** is an efficient algorithm for finding a target value in a **sorted array**.
    It works by repeatedly dividing the search interval in half.
    
    ### How it works:
    1. Start with the entire sorted array
    2. Compare the target with the middle element
    3. If equal, we found it!
    4. If target is smaller, search the left half
    5. If target is larger, search the right half
    6. Repeat until found or range is empty
    
    **Time Complexity**: O(log n) - Much faster than linear search for large arrays!
    """)
    
    with gr.Row():
        with gr.Column():
            array_input = gr.Textbox(
                label="Enter Sorted Array (comma-separated)",
                placeholder="e.g., 2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78",
                value="2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78",
                lines=2
            )
            target_input = gr.Textbox(
                label="Enter Target Value",
                placeholder="e.g., 23",
                value="23"
            )
            search_btn = gr.Button("🔍 Start Binary Search", variant="primary", size="lg")
        
        with gr.Column():
            result_output = gr.Textbox(
                label="Search Result",
                lines=2
            )
    
    steps_output = gr.HTML(label="Step-by-Step Visualization")
    complexity_output = gr.Markdown(label="Algorithm Analysis")
    
    gr.Markdown("""
    ---
    ### Example Test Cases:
    
    Try these examples:
    1. **Array**: `1, 3, 5, 7, 9, 11, 13, 15` | **Target**: `7` (Found)
    2. **Array**: `2, 4, 6, 8, 10, 12, 14` | **Target**: `5` (Not Found)
    3. **Array**: `10, 20, 30, 40, 50` | **Target**: `10` (Best Case - First comparison)
    4. **Array**: `1, 2, 3, 4, 5, 6, 7, 8, 9, 10` | **Target**: `1` (Edge Case)
    
    ### ⚠️ Important Notes:
    - The array **must be sorted** in ascending order
    - Works with integers and decimal numbers
    - Time complexity is O(log n), making it very efficient for large arrays
    
    ---
    **Created for CISC-121 Project** | Queen's University | 2025
    """)
    
    # Connect the search button to the function
    search_btn.click(
        fn=binary_search_with_steps,
        inputs=[array_input, target_input],
        outputs=[result_output, steps_output, complexity_output]
    )

# Launch the app
if __name__ == "__main__":
    app.launch()