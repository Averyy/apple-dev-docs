# Replaying a GPU trace file

**Framework**: Xcode

Debug and profile your app’s performance using a GPU trace file in the Metal debugger.

#### Overview

Replaying a GPU trace file allows you to debug and profile previously captured GPU commands using the Metal debugger. For more information, see [`Capturing a Metal workload in Xcode`](capturing-a-metal-workload-in-xcode.md) or [`Capturing a Metal workload programmatically`](capturing-a-metal-workload-programmatically.md).

To replay a GPU trace file, open it in Xcode. Before clicking Replay, you can configure which device to use (if there’s more than one available), as well as configure whether to run with profiling.

![An Xcode screenshot of the Replay GPU Trace dialog with options to begin replaying a GPU trace file.](https://docs-assets.developer.apple.com/published/63299cd1e14acd0035b2afb3b4405eba/gputools-metal-debugger-essentials-replay%402x.png)

##### Configure Replay

If you have multiple devices, you need to select a device before you can replay the GPU trace file. Xcode automatically selects the most compatible device, but you can select a different device using the Device popover.

> ⚠️ **Warning**: GPU trace files are only compatible with devices of the same type, the same GPU, and the same operating system. Otherwise, performance may vary. For example, if you capture a Metal workload on a Mac with an AMD GPU, replaying the exported GPU trace file on a Mac with the Apple M1 chip may not work or behave the same.

GPU trace files are only compatible with devices of the same type, the same GPU, and the same operating system. Otherwise, performance may vary. For example, if you capture a Metal workload on a Mac with an AMD GPU, replaying the exported GPU trace file on a Mac with the Apple M1 chip may not work or behave the same.

You can optionally enable the Profile GPU Trace option to have Xcode automatically profile after replaying. Profiling has an initial performance impact on the Metal debugger, so only enable this option when debugging your app’s performance. You can always profile later as needed.

## See Also

- [Capturing a Metal workload in Xcode](capturing-a-metal-workload-in-xcode.md)
  Analyze your app’s performance by configuring your project to use the Metal debugger.
- [Capturing a Metal workload programmatically](capturing-a-metal-workload-programmatically.md)
  Analyze your app’s performance by invoking Metal’s frame capture.
- [Investigating visual artifacts](investigating-visual-artifacts.md)
  Discover, diagnose, and fix visual artifacts in your app with the Metal debugger.
- [Optimizing GPU performance](optimizing-gpu-performance.md)
  Find and address performance bottlenecks using the Metal debugger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/replaying-a-gpu-trace-file)*