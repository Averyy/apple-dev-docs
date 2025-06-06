# Metal developer workflows

**Framework**: Xcode

Locate and fix issues related to your app’s use of the Metal API and GPU functions.

#### Overview

Metal comes with a comprehensive suite of advanced developer tools to help you debug and optimize your Metal apps.

##### Runtime Diagnostics

You can enable API Validation when running your app to check for incorrect Metal API usage. For more information, see [`Validating your app’s Metal API usage`](validating-your-apps-metal-api-usage.md).

Enable Shader Validation when running your app to check for issues like out-of-bounds memory access, missing `useResource` calls, and stack overflows. For more information, see [`Validating your app’s Metal shader usage`](validating-your-apps-metal-shader-usage.md).

The Metal Performance HUD offers a visual overlay to catch performance issues while your app is running. For more information, see [`Monitoring your Metal app’s graphics performance`](monitoring-your-metal-apps-graphics-performance.md).

##### Runtime Performance Analysis

The Metal system trace tool in Instruments provides a visual timeline of the parallel work on the CPU and the GPU, and the memory usage of your Metal app.

![An Instruments screenshot displaying a capture in the Game Performance template.](https://docs-assets.developer.apple.com/published/cfb1310c32393bf3962f13e1e66f34b5/gputools-instruments-game-performance-hero%402x.png)

You can begin profiling with the Game Performance template (see [`Analyzing the performance of your Metal app`](analyzing-the-performance-of-your-metal-app.md)) or the Game Memory template (see [`Analyzing the memory usage of your Metal app`](analyzing-the-memory-usage-of-your-metal-app.md)).

##### Advanced Metal Debugging and Profiling

The Metal debugger in Xcode provides advanced tools for debugging and profiling your Metal app.

![A screenshot of the Metal debugger showing the Bound Resources viewer and attachments for a draw command.](https://docs-assets.developer.apple.com/published/a7cba2f6c40a790c84564b5ed827fa13/gputools-metal-debugger-hero%402x.png)

You can get summaries of your Metal workload with the Dependencies viewer and the Memory viewer, inspect individual resources, and selectively debug your shaders. For more information on debugging, see [`Investigating visual artifacts`](investigating-visual-artifacts.md).

In addition, you can optimize your Metal app by drilling down performance bottlenecks with the Performance timeline and the per-line shader profiling results. For more information on profiling, see [`Optimizing GPU performance`](optimizing-gpu-performance.md).

Learn more about [`Metal debugger`](metal-debugger.md).

## Topics

### Project preparation for debugging
- [Building your project with embedded shader sources](building-your-project-with-embedded-shader-sources.md)
  Prepare to debug your project’s shaders by including source code in the build.
- [Naming resources and commands](naming-resources-and-commands.md)
  Enhance the debugging of your Metal app using labels and grouping.
- [Creating and using custom capture scopes](creating-and-using-custom-capture-scopes.md)
  Capture specific GPU commands by using custom capture scopes.
### Runtime diagnostics
- [Inspecting live resources at runtime](inspecting-live-resources-at-runtime.md)
  Validate your resources by viewing the contents of your textures and buffers while debugging your Metal app.
- [Validating your app’s Metal API usage](validating-your-apps-metal-api-usage.md)
  Catch runtime issues in your Metal app using API Validation.
- [Validating your app’s Metal shader usage](validating-your-apps-metal-shader-usage.md)
  Catch common shader runtime issues using Shader Validation while your app is running.
- [Monitoring your Metal app’s graphics performance](monitoring-your-metal-apps-graphics-performance.md)
  Catch performance issues using the Metal Performance HUD while your app is running.
### Counters
- [Finding your Metal app’s GPU occupancy](finding-your-metal-apps-gpu-occupancy.md)
  Understand the GPU usage for executing shaders by using occupancy.
- [Reducing shader bottlenecks](reducing-shader-bottlenecks.md)
  Identify and minimize congestion points in a GPU’s subsystems by checking its limiter and utilization counters.
- [Measuring the GPU’s use of memory bandwidth](measuring-the-gpus-use-of-memory-bandwidth.md)
  Check whether your Metal app correctly reads and writes to memory by measuring the GPU’s memory bandwidth.

## See Also

- [Metal debugger](metal-debugger.md)
  Debug and profile your Metal workload with a GPU trace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/metal-developer-workflows)*