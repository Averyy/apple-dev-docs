# Analyzing Apple GPU performance using a visual timeline

**Framework**: Xcode

Locate performance issues using the Performance timeline.

#### Overview

> ❗ **Important**: The Performance timeline feature is only applicable to Apple GPUs. For other GPU architectures, see [`Analyzing non-Apple GPU performance using counter statistics`](analyzing-non-apple-gpu-performance-using-counter-statistics.md).

Apple GPUs run vertex, fragment, and compute tasks in parallel whenever possible. To explore the parallel nature of Apple GPUs, the Performance timeline helps you visualize the various passes and stages running simultaneously.

![A screenshot of the Performance timeline, showing the Vertex, Fragment, Compute, and Counters tracks. A render pass is selected and the sidebar displays its detailed information.](https://docs-assets.developer.apple.com/published/0c68d41eacfe7d23f49a088caad5268f/gputools-metal-debugger-gt-overview%402x.png)

For information on using the Performance timeline to optimize your Metal workload and profiling your workload in different GPU execution modes, see [`Optimizing GPU performance`](optimizing-gpu-performance.md).

##### View Your Shaders in the Timeline

The top section has the Vertex, Fragment, and Compute GPU tracks, which display the beginning time and duration of individual passes running with overlap. Below the GPU tracks are the aggregated shader tracks that combine the individual shaders. You can view the timeline of individual shaders in a waterfall-like fashion by expanding the aggregated shader tracks.

The bottom section has a separate Counters timeline, which includes GPU counters such as Occupancy, Limiter, and Bandwidth. The counters can help you diagnose performance bottlenecks. You can focus on counter subsets by switching between different counter tabs.

##### Display Additional Information

Clicking any track in the Performance timeline selects it and displays additional information about the track in the sidebar.

Similarly, clicking any element in the Performance timeline selects it and displays additional information about the element in the sidebar.

![A screenshot of the Performance timeline that highlights the Max Theoretical Occupancy line in the runtime shader instruction costs section in the sidebar, which shows 100 percent.](https://docs-assets.developer.apple.com/published/45f59ed20fac1c788bd5419d04afdfff/gputools-metal-debugger-gt-max-theoretical-occupancy%402x.png)

##### Limit Your Scope with Filters

Adjust the track-filtering criteria with the filter field at the bottom of the GPU timeline or Counters timeline. You can type filter terms into the field, and the GPU timeline or Counters timeline shows tracks with names that match those terms. For example, you can simplify the Counters timeline to only show limiter counters by adding “limiter” to the filter field.

![A screenshot of the Performance timeline that highlights the Counters tracks. The filter includes the word limiter, and the Counters timeline shows only the limiter counters.](https://docs-assets.developer.apple.com/published/0410cc52aa2fda5eb69249e92e4de8b1/gputools-metal-debugger-gt-filter%402x.png)

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