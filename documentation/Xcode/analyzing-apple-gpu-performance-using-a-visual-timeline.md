# Analyzing Apple GPU performance using a visual timeline

**Framework**: Xcode

Locate performance issues using the Performance timeline.

#### Overview

> ❗ **Important**: The Performance timeline feature is only applicable to Apple GPUs. For other GPU architectures, see [`Analyzing non-Apple GPU performance using counter statistics`](analyzing-non-apple-gpu-performance-using-counter-statistics.md).

Apple GPUs run vertex, fragment, and compute tasks in parallel whenever possible. To explore the parallel nature of Apple GPUs, the Performance timeline helps you visualize the various passes and stages running simultaneously.

![A screenshot of the Performance timeline, showing the Vertex, Fragment, Compute, and Counters tracks. A render pass is selected and the sidebar displays its detailed information.](/images/com.apple.Xcode/gputools-metal-debugger-gt-overview@2x.png)

For information on using the Performance timeline to optimize your Metal workload and profiling your workload in different GPU execution modes, see [`Optimizing GPU performance`](optimizing-gpu-performance.md).

##### View Your Shaders in the Timeline

The top section has the Vertex, Fragment, and Compute GPU tracks, which display the beginning time and duration of individual passes running with overlap. Below the GPU tracks are the aggregated shader tracks that combine the individual shaders. You can view the timeline of individual shaders in a waterfall-like fashion by expanding the aggregated shader tracks.

The bottom section has a separate Counters timeline, which includes GPU counters such as Occupancy, Limiter, and Bandwidth. The counters can help you diagnose performance bottlenecks. You can focus on counter subsets by switching between different counter tabs.

- **Occupancy**: A GPU has a maximum number of threads that it can execute at the same time. Occupancy is a measurement of how much of this capacity the GPU is using. For more information, see [`Finding your Metal app’s GPU occupancy`](finding-your-metal-apps-gpu-occupancy.md).
- **Limiter and utilization**: GPUs process many different kinds of actions in parallel, including arithmetic, memory access, and rasterization. Limiter counters include time the GPU spends executing work and any stalls in a subsystem that prevent the GPU from starting new work. Utilization counters include time the GPU spends executing work in a subsystem without stalls. For more information, see [`Reducing shader bottlenecks`](reducing-shader-bottlenecks.md).
- **Bandwidth**: The GPU Read Bandwidth and GPU Write Bandwidth counters measure how much and how often the GPU is accessing system memory. For more information, see [`Measuring the GPU’s use of memory bandwidth`](measuring-the-gpus-use-of-memory-bandwidth.md).

##### Display Additional Information

Clicking any track in the Performance timeline selects it and displays additional information about the track in the sidebar.

- **GPU track**: Selecting a GPU track, such as Vertex, Fragment, or Compute, shows a table summarizing the elements in the track. The Performance timeline filters the elements using the current time range selection. You can click the table’s Duration column to sort the elements by duration.
- **Aggregated shader track**: Selecting an aggregated shader track lists all shaders with their durations. The Performance timeline filters the shaders using the current time range selection.
- **Counter track**: Selecting any counter track lists all counters with their mean values in the sidebar. The Performance timeline aggregates the mean values using the current time range selection.

Similarly, clicking any element in the Performance timeline selects it and displays additional information about the element in the sidebar.

- **Encoder**: Selecting an encoder shows its statistics. For a render pass, there are previews of the render attachments as well.
- **Load and store action**: Selecting a load or store action shows metadata from the relevant render pass.
- **Shader**: Selecting a shader shows its statistics, such as compiler statistics and runtime shader instruction costs. In addition, the compiler statistics section includes the Max Theoretical Occupancy of the shader. For more information on occupancy, see [`Finding your Metal app’s GPU occupancy`](finding-your-metal-apps-gpu-occupancy.md).

![A screenshot of the Performance timeline that highlights the Max Theoretical Occupancy line in the runtime shader instruction costs section in the sidebar, which shows 100 percent.](/images/com.apple.Xcode/gputools-metal-debugger-gt-max-theoretical-occupancy@2x.png)

##### Limit Your Scope with Filters

Adjust the track-filtering criteria with the filter field at the bottom of the GPU timeline or Counters timeline. You can type filter terms into the field, and the GPU timeline or Counters timeline shows tracks with names that match those terms. For example, you can simplify the Counters timeline to only show limiter counters by adding “limiter” to the filter field.

![A screenshot of the Performance timeline that highlights the Counters tracks. The filter includes the word limiter, and the Counters timeline shows only the limiter counters.](/images/com.apple.Xcode/gputools-metal-debugger-gt-filter@2x.png)

For any filter term, you can click it and choose to include or exclude tracks that match that term.

##### Search for Specific Elements

Choose Find > Find to display the search bar above the Performance timeline. You can type search terms into the search bar’s text field to find matching command encoders and shaders.

For any search term, you can click it and choose to include or exclude elements that match the term.

The two arrow buttons to the right of the text field let you move to the previous or the next matching element in the timeline.

##### Focus on the Time for an Element

Focusing on the time for an element collapses the nonrelevant time ranges in the Performance timeline:

- To focus on an encoder, Control-click the element in the timeline and select Focus on Encoder.
- To focus on a shader, Control-click the element in the timeline and select Focus on Shader.

To exit the focus mode, click the Expand Timeline button at the bottom of the Performance timeline.

##### Minimize Performance Bottlenecks

- Look for abnormally long passes. Check whether the GPU time for various tasks matches your expectation or exceeds the budget time.
- Try overlapping GPU tasks. Apple GPUs run vertex, fragment, and compute tasks in parallel whenever possible. For example, independent render passes and compute passes can run in parallel. If you observe nonoverlapping work, check whether your GPU work is overserialized. Also, use concurrent compute passes wherever possible so dispatches that touch different resources can execute concurrently.
- Avoid too many small passes. There’s setup time between passes, so having small passes adds latency.
- Use the counters as insights for improving passes in the critical path. The counter tracks available below the GPU tracks show a few key performance metrics. Aim for higher occupancy with efficient GPU work. Use limiters as clues to offload some work to underutilized subsystems on the GPU. In addition, you can Control-click any pass in the Performance timeline and choose Reveal in Counters to view more detailed counters data for a pass. For more information on counters, see [`Finding your Metal app’s GPU occupancy`](finding-your-metal-apps-gpu-occupancy.md) and [`Reducing shader bottlenecks`](reducing-shader-bottlenecks.md).
- Prioritize optimizing passes in the critical path. When inspecting a pass, you can focus on the running shaders in the aggregated shader track below the GPU track. In addition, you can Control-click any shader in the Performance timeline and choose Open Shader. In the Shader editor, you can find per-line shader profiling statistics for identifying hot spots.

## See Also

- [Analyzing your Metal workload](analyzing-your-metal-workload.md)
  Investigate your app’s workload, dependencies, performance, and memory impact using the Metal debugger.
- [Analyzing resource dependencies](analyzing-resource-dependencies.md)
  Avoid unnecessary work in your Metal app by understanding the relationships between resources.
- [Analyzing memory usage](analyzing-memory-usage.md)
  Manage your Metal app’s memory usage by inspecting its resources.
- [Analyzing Apple GPU performance using counter statistics](analyzing-apple-gpu-performance-using-counter-statistics.md)
  Optimize performance by examining counters for individual passes and commands.
- [Analyzing Apple GPU performance with performance heat maps](analyzing-apple-gpu-performance-using-performance-heatmaps-a17-m3.md)
  Gain insights to SIMD group performance by inspecting source code execution.
- [Analyzing Apple GPU performance using the shader cost graph](analyzing-apple-gpu-performance-using-shader-cost-graph-a17-m3.md)
  Discover potential shader performance issues by examining pipeline states.
- [Analyzing non-Apple GPU performance using counter statistics](analyzing-non-apple-gpu-performance-using-counter-statistics.md)
  Optimize performance by examining counters for individual passes and commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/analyzing-apple-gpu-performance-using-a-visual-timeline)*