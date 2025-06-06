# Inspecting shaders

**Framework**: Xcode

Improve your app’s shader performance by examining and editing your shaders.

#### Overview

The Metal debugger allows you to view and edit shaders with the Shader editor. After opening a shader, you can view and edit its source code, or the source code of any other file within the Metal library that the executed function requires. For more information, see [`Inspecting the bound resources for a command`](inspecting-the-bound-resources-for-a-command.md).

When you profile the Metal workload, you can see per-line performance metrics. As you make changes, you can reload the shader to update the Metal workload and performance numbers.

> ❗ **Important**: Include source code when you capture a Metal workload because the Shader editor needs it to function correctly. For more information, see [`Building your project with embedded shader sources`](building-your-project-with-embedded-shader-sources.md).

Include source code when you capture a Metal workload because the Shader editor needs it to function correctly. For more information, see [`Building your project with embedded shader sources`](building-your-project-with-embedded-shader-sources.md).

##### Navigate Your Shader

The Shader editor shows your source code in the context of an executed function, and includes familiar Xcode source-editing abilities, like [`Fixing issues in your code as you type`](fixing-issues-in-your-code-as-you-type.md).

In addition to the source containing the executed function, you can also edit other files within the Metal library that the executed function requires. Click the Toggle Left Sidebar button on the bottom left to reveal the source files outline. Then, select another file.

![A screenshot of the Shader editor showing a list of shader source files on the left and the contents of the selected shader source file on the right.](https://docs-assets.developer.apple.com/published/2676ede9b5b80647e96166d46d3c2027/gputools-metal-debugger-se-source%402x.png)

##### View Per Line Performance Metrics

You can view per-line performance metrics in the Shader editor after profiling finishes. This happens automatically if you select Profile after Replay in the Metal Capture popover (see [`Capturing a Metal workload in Xcode`](capturing-a-metal-workload-in-xcode.md)) or Profile GPU Trace in the Replay window (see [`Replaying a GPU trace file`](replaying-a-gpu-trace-file.md)). Alternatively, you can profile directly within the Shader editor by clicking the Generate button in the top right corner.

![A screenshot of the Shader editor highlighting the Generate button at the top right.](https://docs-assets.developer.apple.com/published/0a3618d437b6f53d12ed4a946db4314d/gputools-metal-debugger-se-profile-generate%402x.png)

Then, wait for profiling to finish. You can see its status in the activity bar at the top of your Xcode window.

After profiling your Metal workload, the Shader editor shows statistics on each line. For devices with a GPU in the Apple 4 family or later, there’s a pie chart to the right of the numeric statistics to help you improve the performance for a function or a line of code. For more information on Apple GPU family 4 devices, see [`Tailor Your Apps for Apple GPUs and Tile-Based Deferred Rendering`](https://developer.apple.com/documentation/Metal/tailor-your-apps-for-apple-gpus-and-tile-based-deferred-rendering) and [`Metal feature set tables`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf).

![A screenshot of the Shader editor highlighting the per-line shader profiling data next to the source code. It displays weights in percentages and categorical breakdowns in pie charts.](https://docs-assets.developer.apple.com/published/3deba516335f4981cfc8c4c13c3e8073/gputools-metal-debugger-se-numbers%402x.png)

You can hover the pointer over the pie chart to enlarge it and show more detail about the work that the GPU performed while executing the line of code. The work a GPU performs can be categorized as memory, ALU, synchronization, or control flow.

![A screenshot of the Shader editor showing the categorical performance breakdown of a shader line in the popover.](https://docs-assets.developer.apple.com/published/dd7ed266d6266e81a5bb9e9cb0837ce4/gputools-metal-debugger-se-profiler-numbers%402x.png)

By understanding the activities that the GPU executes for each line in your shader, you can infer any necessary code changes to improve the shader performance.

| GPU activity | Explanation and recommendations |
| --- | --- |
| ALU | The amount of time that the GPU spends in the arithmetic logic unit. Change floats to half-floats where possible to reduce the time in the ALU. Also, try to minimize your use of complex instructions like `sqrt`, `sin`, `cos`, and `recip`. |
| Memory | The amount of time that the GPU spends waiting for access to your app’s buffers or texture memory. Reduce time by downsampling textures, or, if you’re not spending much time in memory, improve your texture resolution instead. |
| Control flow | The amount of time that the GPU spends in conditional, increment, or jump instructions as a result of branches or loops in your shader. Use a constant iteration count to minimize control flow time for loops because the Metal compiler can generate optimized code in those cases. |
| Synchronization | The amount of time that the GPU spends waiting for a required resource or event before execution can begin. Synchronization types are described below. |
| Synchronization (wait memory) | The amount of time that the GPU spends waiting for dependent memory accesses, such as texture sampling or buffer read/write. |
| Synchronization (wait pixel) | The amount of time that the GPU spends waiting for underlying pixels to release resources. In addition to color attachments, pixels can come from depth or stencil buffers or user-defined resources. Blending is a common cause of pixel waiting. Use raster order groups to reduce the wait time. |
| Synchronization (barrier) | The amount of time that the GPU spends when a thread reaches a barrier and the GPU waits for remaining threads in the same group to arrive at the barrier before proceeding. |
| Synchronization (atomics) | The amount of time that the GPU spends on atomic instructions. |

To ensure you see the most up-to-date profiling numbers, set your app’s deployment target to the matching OS version, even if temporarily. The Shader editor displays a warning at the top if the deployment target doesn’t match your OS version.

![A screenshot showing a warning about a mismatching deployment target and OS version.](https://docs-assets.developer.apple.com/published/8f28d38c613b07944bf8035498be374d/gputools-metal-debugger-se-profile-warnings%402x.png)

You can change the deployment target in the Xcode project settings. If you change the deployment target temporarily, don’t forget to change it back before deploying your app.

![A screenshot of the Xcode project editor showing the drop-down menu to choose a minimum deployment target.](https://docs-assets.developer.apple.com/published/c2400502e7aeb292ef214224d02589ab/gputools-metal-debugger-se-deployment-target%402x.png)

##### Update Your Shader

After changing a shader, you can update the captured frame with the new source code by clicking the Reload Shaders button in the debug bar.

![A screenshot of the Reload Shaders button in the debug bar.](https://docs-assets.developer.apple.com/published/3772f6e2fc52fa9d8f2252a384c418df/gputools-metal-debugger-se-reload%402x.png)

After updating the captured frame, Xcode does the following:

- Redraws the app window.
- Updates the profiler statistics and pie charts.
- Redraws attachments in the assistant editor.
- Maintains your place in the captured frame, providing an interactive environment to enhance your shader performance tuning.

> ❗ **Important**: To avoid getting misleading results between different runs, using a consistent performance state is useful when iterating on your shader.

To avoid getting misleading results between different runs, using a consistent performance state is useful when iterating on your shader.

You can profile using a specific performance state by clicking the GPU Profiler button in the debug bar.

![A screenshot of the GPU Profiler button.](https://docs-assets.developer.apple.com/published/68df1c3d2ba412e5c521788ae7a981a1/gputools-metal-debugger-se-induce-performance-0%402x.png)

Then, select your desired performance state.

![A screenshot of the GPU Profiler popover to choose a performance state.](https://docs-assets.developer.apple.com/published/61daf532caabadf630af1cb1f3cd3bbf/gputools-metal-debugger-se-induce-performance-1%402x.png)

If your shader is producing incorrect results, you can also debug it. For more information, see [`Debugging the shaders within a draw command or compute dispatch`](debugging-the-shaders-within-a-draw-command-or-compute-dispatch.md).

## See Also

- [Inspecting acceleration structures](inspecting-acceleration-structures.md)
  Reveal ray intersection bottlenecks by examining your acceleration structures.
- [Inspecting buffers](inspecting-buffers.md)
  Confirm your buffer formats by examining buffer content.
- [Inspecting pipeline states](inspecting-pipeline-states.md)
  Determine how your render and compute passes behave by examining their properties.
- [Inspecting sampler states](inspecting-sampler-states.md)
  Verify your sampler state configurations by examining their properties.
- [Inspecting textures](inspecting-textures.md)
  Discover issues in your textures by examining their content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/inspecting-shaders)*