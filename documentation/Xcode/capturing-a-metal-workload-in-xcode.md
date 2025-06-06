# Capturing a Metal workload in Xcode

**Framework**: Xcode

Analyze your app’s performance by configuring your project to use the Metal debugger.

#### Overview

You can use Xcode to capture your app’s Metal workload. First, ensure that the GPU Frame Capture option is enabled in the runtime diagnostics options. Then, when your app is running, click the Metal Capture button in the debug bar, select a scope, and click Capture.

##### Configure the Gpu Frame Capture Options

Xcode automatically enables the GPU Frame Capture option if your target links to the [`Metal`](https://developer.apple.com/documentation/Metal) framework, or any other framework that uses the Metal API. If you’re collaborating on a project, it’s possible that someone else may have disabled GPU Frame Capture. To ensure it’s enabled, follow these steps:

1. In the Xcode toolbar, choose Edit Scheme from the Scheme menu. ![An Xcode screenshot showing the Scheme menu with the Edit Scheme menu item highlighted.](https://docs-assets.developer.apple.com/published/52f80993d6dca820d9e146ee65e533d2/gputools-metal-debugger-essentials-capture-edit-scheme%402x.png)
2. Select the Run scheme action.
3. Select the Options tab.
4. Choose a GPU Frame Capture option and click Close. ![A screenshot of the Xcode scheme editor highlighting the GPU Frame Capture option.](https://docs-assets.developer.apple.com/published/04a267f398a9b9ecd2a91c97369a6a77/gputools-metal-debugger-essentials-capture-options%402x.png)

The GPU Frame Capture options include the following:

##### Capture Your Metal Workload While Debugging

While debugging your app, you can capture a GPU trace by following these steps:

1. Click the Metal Capture button in the debug bar. ![A screenshot of the Metal Capture popover, accessible from the Metal Capture button in the debug bar.](https://docs-assets.developer.apple.com/published/0d9ef2422d5cb72d633bac5301693550/gputools-metal-debugger-essentials-capture-popup%402x.png)
2. Select the scope that you want to capture. This can be a frame, Metal layer, command queue, device, or any custom scopes that you set up previously. For more information, see [`Creating and using custom capture scopes`](creating-and-using-custom-capture-scopes.md).
3. Select the count. Depending on the scope, this might include the number of frames or command buffers.
4. Optionally, select Profile after Replay so that Xcode automatically profiles after capturing. Profiling has an initial performance impact on the Metal debugger, so only enable this option when debugging your app’s performance. You can always profile later as needed. For more information, see [`Replaying a GPU trace file`](replaying-a-gpu-trace-file.md).
5. Click Capture.

Xcode automatically starts capturing a GPU trace when the scope triggers, and then finishes the capture based on the scope and count you select. To manually stop the capture, you can click the Finish button at any time.

> 💡 **Tip**: In macOS, you can start a capture by selecting an option from the “Capture shortcut” menu, and then pressing that keyboard shortcut while the app is active.

In macOS, you can start a capture by selecting an option from the “Capture shortcut” menu, and then pressing that keyboard shortcut while the app is active.

##### Capture Your Metal Workload After Deployment

Capture a GPU trace after deploying your app by following these steps:

1. In Xcode, choose Debug > Debug Executable.
2. Select your app in Finder and click Choose. Xcode automatically brings up the scheme editor.
3. Click the Options tab, choose a GPU Frame Capture option, and click Close. ![A screenshot of the Xcode scheme editor highlighting the GPU Frame Capture option.](https://docs-assets.developer.apple.com/published/7ef16897d680c1e5d44bf10306a0ee33/gputools-metal-debugger-essentials-capture-choose-options%402x.png)
4. Run your app by choosing Product > Run.
5. Click the Metal Capture button in the debug bar. ![An Xcode screenshot of the Metal Capture popover, accessible from the Metal Capture button in the debug bar.](https://docs-assets.developer.apple.com/published/2c7fc71b578a089d734d249b4e245d8d/gputools-metal-debugger-essentials-capture-choose-capture%402x.png)
6. Select the scope and count that you want to capture. You can optionally select Profile after Replay. For more information, see [`Replaying a GPU trace file`](replaying-a-gpu-trace-file.md).
7. Click Capture.

Xcode automatically starts capturing a GPU trace when the scope triggers, and then finishes the capture based on the count you select. To manually stop the capture, you can click the Finish button at any time.

> 💡 **Tip**: In macOS, you can start a capture by selecting an option from the “Capture shortcut” menu, and then pressing that keyboard shortcut while the app is active.

In macOS, you can start a capture by selecting an option from the “Capture shortcut” menu, and then pressing that keyboard shortcut while the app is active.

##### Save the Capture to Your Computer

To save your captured Metal workload as a GPU trace, choose File > Export. For more information on replaying GPU trace files, see [`Replaying a GPU trace file`](replaying-a-gpu-trace-file.md).

## See Also

- [Capturing a Metal workload programmatically](capturing-a-metal-workload-programmatically.md)
  Analyze your app’s performance by invoking Metal’s frame capture.
- [Replaying a GPU trace file](replaying-a-gpu-trace-file.md)
  Debug and profile your app’s performance using a GPU trace file in the Metal debugger.
- [Investigating visual artifacts](investigating-visual-artifacts.md)
  Discover, diagnose, and fix visual artifacts in your app with the Metal debugger.
- [Optimizing GPU performance](optimizing-gpu-performance.md)
  Find and address performance bottlenecks using the Metal debugger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/capturing-a-metal-workload-in-xcode)*