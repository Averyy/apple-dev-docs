# Analyzing Apple GPU performance using counter statistics

**Framework**: Xcode

Optimize performance by examining counters for individual passes and commands.

#### Overview

> ❗ **Important**: The Performance counters feature is only applicable to Apple GPUs. For other GPU architectures, see [`Analyzing non-Apple GPU performance using counter statistics`](analyzing-non-apple-gpu-performance-using-counter-statistics.md).

The Performance counters show performance statistics from your app’s passes or commands in the GPU trace. These counters measure hardware-related activities on the GPU, ranging from memory bandwidth to the number of vertices, the number of rasterized fragments, and the texture-filtering limiter and utilization percentages.

![A screenshot of the Performance counters displaying per-pass performance limiters counters.](https://docs-assets.developer.apple.com/published/e3969e27a9bca78e8106922fdb0ca9bb/gputools-metal-debugger-ct-overview%402x.png)

The Metal debugger collects data from the passes running without overlap, so only one pass runs at a time on the device when the profiler measures the performance. Additionally, it includes deterministic counters that don’t vary by time, such as the number of vertices in a render pass.

##### View Different Counter Sets for Passes or Commands

At the top of the graph, you can click the Encoders or the GPU Commands tab to choose to view the counters by pass or command granularity. Then, you can choose which counter set to use for viewing the collection of counters. In addition, clicking the Edit Counters button on the right allows you to create counter sets or to customize existing ones to suit your performance optimization workflow.

##### View Performance Counters in the Assistant Editor

The assistant editor allows you to see additional information for individual passes and commands. You can enable the assistant editor by clicking the Adjust Editor Options button and choosing the Assistant option.

![A screenshot of the Adjust Editor Options menu highlighting the Assistant menu item.](https://docs-assets.developer.apple.com/published/7c6bbd00b264611eef5f9d18c56bed4b/gputools-metal-debugger-ct-menu-enable-assistant-editor%402x.png)

Selecting a pass or command shows its performance counters in the assistant editor. If you see something other than performance counters, you can select Performance from the drop-down menu at the top left of the editor.

![A screenshot of the Assistant Editor drop-down menu highlighting the Performance menu item.](https://docs-assets.developer.apple.com/published/5c40e29da58eb1abde53d13d6a0966d1/gputools-metal-debugger-ct-assistant-menu-performance%402x.png)

The performance counters in the assistant editor let you inspect all the counters for a specific pass or command. By analyzing values that may be hotspots, counters can suggest a specific cause of your app’s performance problem. For example, if the number of vertices is twice as high as you expect, it’s likely that your code has duplicate meshes or render encoder draw calls.

![A screenshot of the Metal debugger showing the Performance counters and the Performance Statistics viewer side by side.](https://docs-assets.developer.apple.com/published/20627784f99f50ac300c487f9a2e7e2d/gputools-metal-debugger-ct-performance%402x.png)

For more information, see [`Analyzing draw command and compute dispatch performance with GPU counters`](analyzing-draw-command-and-compute-dispatch-performance-with-gpu-counters.md).

##### View Pipeline Statistics for a Command

Selecting a command allows you to look at its pipeline statistics in the assistant editor. You can select Pipeline Statistics from the Assistant Editor drop-down menu to view information about the pipeline state and its performance statistics.

![A screenshot of the Assistant Editor drop-down menu highlighting the Pipeline Statistics menu item.](https://docs-assets.developer.apple.com/published/d41466b27f19c9e62f834757a388492b/gputools-metal-debugger-ct-assistant-menu-pipeline-statistics%402x.png)

The pipeline statistics in the assistant editor let you look at compiler metrics and execution timing. The top portion of the assistant editor area lists the time each pipeline stage took to complete in separate categories. Below, it lists the commands that use the same pipeline stage, as well as their shader GPU time.

![A screenshot of the Metal debugger showing the Performance counters and the Pipeline Statistics viewer side by side.](https://docs-assets.developer.apple.com/published/cb6d09659e1b1ee5403b797d86f21c8c/gputools-metal-debugger-ct-pipeline-statistics%402x.png)

For more information, see [`Analyzing draw command and compute dispatch performance with pipeline statistics`](analyzing-draw-command-and-compute-dispatch-performance-with-pipeline-statistics.md).

##### Optimize Your Workload

There are a few interesting metrics you can investigate when beginning to optimize your workload:

Sometimes, counters data may only hint at a problem, and you can benefit by leveraging additional Metal tools. For example, if your fragment shader time is unexpectedly high, you can use the Shader editor to discover which specific lines in your fragment shader are slowing down the execution. For more information, see [`Inspecting shaders`](inspecting-shaders.md).

## See Also

- [Analyzing your Metal workload](analyzing-your-metal-workload.md)
  Investigate your app’s workload, dependencies, performance, and memory impact using the Metal debugger.
- [Analyzing resource dependencies](analyzing-resource-dependencies.md)
  Avoid unnecessary work in your Metal app by understanding the relationships between resources.
- [Analyzing memory usage](analyzing-memory-usage.md)
  Manage your Metal app’s memory usage by inspecting its resources.
- [Analyzing Apple GPU performance using a visual timeline](analyzing-apple-gpu-performance-using-a-visual-timeline.md)
  Locate performance issues using the Performance timeline.
- [Analyzing Apple GPU performance with performance heat maps](analyzing-apple-gpu-performance-using-performance-heatmaps-a17-m3.md)
  Gain insights to SIMD group performance by inspecting source code execution.
- [Analyzing Apple GPU performance using the shader cost graph](analyzing-apple-gpu-performance-using-shader-cost-graph-a17-m3.md)
  Discover potential shader performance issues by examining pipeline states.
- [Analyzing non-Apple GPU performance using counter statistics](analyzing-non-apple-gpu-performance-using-counter-statistics.md)
  Optimize performance by examining counters for individual passes and commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/analyzing-apple-gpu-performance-using-counter-statistics)*