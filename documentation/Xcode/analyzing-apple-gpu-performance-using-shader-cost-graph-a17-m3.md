# Analyzing Apple GPU performance using the shader cost graph

**Framework**: Xcode

Discover potential shader performance issues by examining pipeline states.

#### Overview

One key method of triaging performance bottlenecks is to look at the most expensive shaders to understand which functions and lines are the most costly. The shader cost graph allows you to quickly find and triage expensive pipeline states and shaders.

> ❗ **Important**: The shader cost graph feature is available for iOS devices with A17 Pro or later, and Mac computers with M3 or later.

##### View the Shader Cost Graph

To open the shader cost graph, click the Performance button in the Metal debugger’s Debug navigator, and then click the Shaders tab above the Performance timeline.

> **Note**: The shader cost graph is available for pipeline states only.

When you select a pipeline state in the Timeline navigator, the shader cost graph for that pipeline state’s shaders appears on the right.

![A screenshot of the Metal debugger’s shader cost graph.](https://docs-assets.developer.apple.com/published/773d75e7dc21b9b02e57e468305390a0/gputools-metal-debugger-essentials-shader-cost-graph%402x.png)

##### Switch Between Shader Types

By default, selecting a render pipeline state shows the fragment shader cost graph. Selecting a compute pipeline state shows the compute shader cost graph.

You can switch between different shader types using the Vertex and Fragment tabs above the shader cost graph.

##### Navigate the Shader Cost Graph

The shader cost graph in the top section left-aligns the most expensive shader function calls, and shows the function call stack from top to bottom. The shader source code of the corresponding shader type appears below the graph.

You can select a function in the shader cost graph to view its shader source code below in the source editor.

##### Understand Per Line Costs

The percentage weights appear in the gutter of the shader source code to the left of the lines of code.

The pie chart to the right of each weight contains performance statistics to help you improve the shader code. Hover over a pie chart to display the detailed breakdown of the instructions of a line.

![A screenshot showing the popover that appears after clicking a pie chart icon. The popover contains information about runtime statistics, instruction types, and instruction data types.](https://docs-assets.developer.apple.com/published/1e40900868d2d8cdd2168c2c8461ba16/gputools-metal-debugger-essentials-shader-cost-graph-per-line-stats%402x.png)

The instruction details include the following runtime statistics infomation:

| Runtime statistics | Description |
| --- | --- |
| Instructions Executed (Total) | The total number of instructions that all threads executed across all SIMD groups of the shader. This includes threads that Metal masked off due to the shape of the geometry or conditional branches. |
| Instructions Executed (Active) | The total number of instructions that active threads executed across all SIMD groups of the shader. |
| Divergence | 1 - the number of active instructions divided by the total number of instructions. |
| ALU Cost | The percentage cost of the ALU instructions, such as floating-point or integer multiplication instructions. |
| Non-ALU Cost | The percentage cost of the non-ALU instructions, such as texture sampling instructions. |

The shader source line may consist of multiple instructions with different instruction types. For example, sampling a texture may involve math, sample, and synchronization instructions. The instruction details include the following possible instruction types and their cost:

- Math
- Comparison
- Select
- Bit Manipulation
- Conversion
- Permute
- Reduce
- Control Flow
- Predication
- Sample
- Synchronization
- Load Store
- Load
- Store
- Atomic
- Barrier
- Fragment Feedback
- Vertex Processing
- Image Access
- Data Movement
- Ray Tracing
- Image Block Load
- Image Block Write
- Image Write

Each arithmetic instruction may operate on different data types, such as half-floats or integers. The instruction details include the following possible data types and their cost:

- Float16
- Float32
- Integer
- Bits

##### Switch Between Per Line Metric Modes

In the shader source code control bar, you can choose different modes for the per-line shader profiling statistics in the gutter. Options include the following:

| Mode | Description |
| --- | --- |
| Cost | The sum of the weighted cost of the assembly instructions. |
| Number of Instructions | The total number of assembly instructions that active threads executed. |
| Thread Divergence | 1 - the total number of instructions from active threads divided by the number of theoretical maximum instructions that the system can execute. |

For more information about the Metal profiling tools for M3 and A17 Pro, see [`Discover new Metal profiling tools for M3 and A17 Pro`](https://developer.apple.comhttps://developer.apple.com/videos/play/tech-talks/111374/).

## See Also

- [Analyzing your Metal workload](analyzing-your-metal-workload.md)
  Investigate your app’s workload, dependencies, performance, and memory impact using the Metal debugger.
- [Analyzing resource dependencies](analyzing-resource-dependencies.md)
  Avoid unnecessary work in your Metal app by understanding the relationships between resources.
- [Analyzing memory usage](analyzing-memory-usage.md)
  Manage your Metal app’s memory usage by inspecting its resources.
- [Analyzing Apple GPU performance using a visual timeline](analyzing-apple-gpu-performance-using-a-visual-timeline.md)
  Locate performance issues using the Performance timeline.
- [Analyzing Apple GPU performance using counter statistics](analyzing-apple-gpu-performance-using-counter-statistics.md)
  Optimize performance by examining counters for individual passes and commands.
- [Analyzing Apple GPU performance with performance heat maps](analyzing-apple-gpu-performance-using-performance-heatmaps-a17-m3.md)
  Gain insights to SIMD group performance by inspecting source code execution.
- [Analyzing non-Apple GPU performance using counter statistics](analyzing-non-apple-gpu-performance-using-counter-statistics.md)
  Optimize performance by examining counters for individual passes and commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Xcode/analyzing-apple-gpu-performance-using-shader-cost-graph-a17-m3)*