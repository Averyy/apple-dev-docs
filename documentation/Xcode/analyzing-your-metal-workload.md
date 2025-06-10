# Analyzing your Metal workload

**Framework**: Xcode

Investigate your app’s workload, dependencies, performance, and memory impact using the Metal debugger.

#### Overview

The Metal debugger provides useful tools for analyzing many aspects of how your app uses the GPU.

After capturing a Metal workload (see [`Capturing a Metal workload in Xcode`](capturing-a-metal-workload-in-xcode.md)) or replaying a GPU trace (see [`Replaying a GPU trace file`](replaying-a-gpu-trace-file.md)), the Metal debugger presents the Summary viewer. The Summary viewer includes a preview of the last presented drawable in your app on the left, several statistics on the right, and a list of automatically generated recommendations, called Insights, at the bottom.

To the left of the Summary viewer is the Debug navigator, which enables quick access to top-level information about your Metal workload. You can explore all of the GPU commands in your capture, as well as all of the pipeline states it uses.

![A screenshot of the Metal debugger showing the Debug navigator and the Summary viewer. The Debug navigator includes top-level gauges, the Outline popup menu, the GPU trace outline, and a filter bar.](https://docs-assets.developer.apple.com/published/33b57024a9675b7e181693051f4397d2/gputools-metal-debugger-debug-navigator-summary-page%402x.png)

##### View Statistics for Your Metal Workload

The Metal debugger automatically calculates several statistics and displays them on the right side of the Summary viewer.

The Overview section includes the number of command buffers, command encoders, and draw commands or compute dispatches. It takes CPU time to encode commands, and GPU time to execute them. If your app is creating too many command buffers or command encoders that start to have a significant impact on performance, consider reducing the workload. You can click the Show Dependencies button to open the Dependencies viewer and learn how your command encoders connect with one another (see [`Analyzing resource dependencies`](analyzing-resource-dependencies.md)).

![A screenshot of the Summary viewer highlighting the Overview section.](https://docs-assets.developer.apple.com/published/a6a7a7b7fcce85a573a213dda23ef005/gputools-metal-debugger-sp-overview%402x.png)

The Performance section includes the total GPU time and the number of vertices. If your workload has a high GPU time, consider optimizing its performance (see [`Optimizing GPU performance`](optimizing-gpu-performance.md)). You can also click the Show Performance button to display the Performance timeline and discover which aspects of your Metal workload are taking the most time (see [`Analyzing Apple GPU performance using a visual timeline`](analyzing-apple-gpu-performance-using-a-visual-timeline.md)).

![A screenshot of the Summary viewer highlighting the Performance section.](https://docs-assets.developer.apple.com/published/355c61c05ccf0e4e5948c00698450b8f/gputools-metal-debugger-sp-performance%402x.png)

> **Note**: If you don’t select the Profile after Replay checkbox in the Metal Capture popover (see [`Capturing a Metal workload in Xcode`](capturing-a-metal-workload-in-xcode.md)) or the Profile GPU Trace checkbox in the Replay window (see [`Replaying a GPU trace file`](replaying-a-gpu-trace-file.md)), the performance section doesn’t show any statistics. To see the statistics, click the Profile button and wait for profiling to finish.

![A screenshot of the Performance section when there isn’t any profiling data displaying. The Profile button is highlighted.](https://docs-assets.developer.apple.com/published/684e8b3148503f6c9bbfad5864245538/gputools-metal-debugger-sp-no-profile%402x.png)

The Memory section includes a brief overview of GPU memory for various resource types, such as textures and buffers. If your Metal workload is using a large amount of memory, consider optimizing the memory use. You can also click the Show Memory button to open the Memory viewer and discover which aspects of your Metal workload are using the most memory (see [`Analyzing memory usage`](analyzing-memory-usage.md)).

![A screenshot of the Summary viewer highlighting the Memory section.](https://docs-assets.developer.apple.com/published/868766f4a87065b54e3618acba14b913/gputools-metal-debugger-sp-memory%402x.png)

##### Browse Api Calls

By default, the Metal debugger shows an outline of captured Metal commands — grouped by command buffers, passes, and debug groups — in the Debug navigator. In addition, for render passes, the outline includes a list of render attachment thumbnail images.

![A screenshot of the Metal debugger highlighting the Debug navigator.](https://docs-assets.developer.apple.com/published/f6ea610234dd4583bc692c4919b73f5a/gputools-metal-debugger-debug-navigator-group-by-api%402x.png)

It’s common for a render pass to issue a massive number of draw commands. You can skim through the draw commands by moving your pointer over the rows to quickly locate a draw command of interest. The Metal debugger shows a preview of the first attachment in the popover.

![A screenshot of the Debug navigator showing the popover that appears when the pointer hovers over any command in the outline.](https://docs-assets.developer.apple.com/published/006a04ff7f20fd69ca2dd01d19de59cb/gputools-metal-debugger-debug-navigator-skim%402x.png)

##### Browse Pipeline States

Instead of viewing the hierarchy of Metal commands, you can begin exploring your captured Metal workload from pipeline states. Click the Outline popup menu and select Group by Pipeline State.

![A screenshot of the Metal debugger’s Debug navigator showing the commands grouped by pipeline states.](https://docs-assets.developer.apple.com/published/796446141540d5b1c73aaa6e395a85a8/gputools-metal-debugger-debug-navigator-group-by-pso%402x.png)

The Metal debugger shows a list of pipeline states. Expanding a pipeline state allows you to see its shaders. Further expansion shows all the draw commands and compute dispatches that use that pipeline state.

With profiling data, the Debug navigator displays the percentage of samples from the shaders of each pipeline state when running the workload with overlap. In a shader-bound workload, this sorted list of pipeline states is helpful in identifying the most expensive pipeline state.

##### Improve Your Metal Workload with Insights

The Metal debugger automatically generates a number of recommendations, called Insights, and includes them at the bottom of the Summary viewer to help you improve your Metal workload. The Insights information includes the following categories:

![A screenshot of the Insights section in the Summary viewer showing a memory insight.](https://docs-assets.developer.apple.com/published/54302fcdad52b0e9ae97a1b5b68baa14/gputools-metal-debugger-sp-insights%402x.png)

![A screenshot of the Insights section in the Summary viewer showing an API usage insight.](https://docs-assets.developer.apple.com/published/e780d4fe50f19ebe89a78e2d2b428a15/gputools-metal-debugger-sp-api-usage%402x.png)

Click the Insights button next to the command in the Debug navigator to see in-depth details and recommendations that may improve your command.

![A screenshot of the Insights popover with detailed information and recommendations for a command in the Debug navigator.](https://docs-assets.developer.apple.com/published/b2dd632c00ba7fd1b38d185c8d301676/gputools-metal-debugger-debug-navigator-insights-popover%402x.png)

##### Limit Your Scope with Filters

Use the filter bar at the bottom of the Debug navigator to adjust filtering criteria. You can type filter terms into the filter bar’s text field, and the outline in the Debug navigator shows only rows with labels that match those filter terms.

When there are two or more filter terms, you can click the filter button to choose whether to match any or all of the terms. For any filter term, you can click it to choose to include or exclude resources that match that term.

The following additional filter tools appear to the right:

## See Also

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
- [Analyzing Apple GPU performance using the shader cost graph](analyzing-apple-gpu-performance-using-shader-cost-graph-a17-m3.md)
  Discover potential shader performance issues by examining pipeline states.
- [Analyzing non-Apple GPU performance using counter statistics](analyzing-non-apple-gpu-performance-using-counter-statistics.md)
  Optimize performance by examining counters for individual passes and commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/analyzing-your-metal-workload)*