# Capturing a Metal workload in Xcode

**Framework**: Xcode

Analyze your app’s performance by configuring your project to use the Metal debugger.

#### Overview

You can use Xcode to capture your app’s Metal workload. First, ensure that the GPU Frame Capture option is enabled in the runtime diagnostics options. Then, when your app is running, click the Metal Capture button in the debug bar, select a scope, and click Capture.

##### Configure the Gpu Frame Capture Options

Xcode automatically enables the GPU Frame Capture option if your target links to the [`Metal`](https://developer.apple.com/documentation/metal) framework, or any other framework that uses the Metal API. If you’re collaborating on a project, it’s possible that someone else may have disabled GPU Frame Capture. To ensure it’s enabled, follow these steps:

1. In the Xcode toolbar, choose Edit Scheme from the Scheme menu. ![An Xcode screenshot showing the Scheme menu with the Edit Scheme menu item highlighted.](/images/com.apple.Xcode/gputools-metal-debugger-essentials-capture-edit-scheme@2x.png)
2. Select the Run scheme action.
3. Select the Options tab.
4. Choose a GPU Frame Capture option and click Close. ![A screenshot of the Xcode scheme editor highlighting the GPU Frame Capture option.](/images/com.apple.Xcode/gputools-metal-debugger-essentials-capture-options@2x.png)

The GPU Frame Capture options include the following:

- **Automatically**: Captures Metal or OpenGL ES API usage in your app. If your target doesn’t link to the Metal framework or the OpenGL ES framework, the Metal Capture button doesn’t appear in the debug bar. If your app uses both the Metal  API and the OpenGL ES API, you can click and hold the Capture GPU Frame icon to choose which API usage to capture.
- **Metal**: Captures only Metal API usage in your app. If your app doesn’t use the Metal API, Xcode disables the Metal Capture button in the debug bar.
- **Disabled**: Doesn’t capture Metal usage in your app. GPU Frame Capture has a tiny, but measurable, effect on your app’s CPU processing time, so choose this option when you want to test your app’s maximum performance level.

##### Capture Your Metal Workload While Debugging

While debugging your app, you can capture a GPU trace by following these steps:

1. Click the Metal Capture button in the debug bar. ![A screenshot of the Metal Capture popover, accessible from the Metal Capture button in the debug bar.](/images/com.apple.Xcode/gputools-metal-debugger-essentials-capture-popup@2x.png)
2. Select the scope that you want to capture. This can be a frame, Metal layer, command queue, device, or any custom scopes that you set up previously. For more information, see [`Creating and using custom capture scopes`](creating-and-using-custom-capture-scopes.md).
3. Select the count. Depending on the scope, this might include the number of frames or command buffers.
4. Click Capture.

Xcode automatically starts capturing a GPU trace when the scope starts, then finishes the capture based on the scope and count you select. To manually stop the capture, you can click the Finish button at any time.

##### Capture Your Metal Workload After Deployment

Capture a GPU trace after deploying your app by following these steps:

1. In Xcode, choose Debug > Debug Executable.
2. Select your app in Finder and click Choose. Xcode automatically brings up the scheme editor.
3. Click the Options tab, choose a GPU Frame Capture option, and click Close. ![A screenshot of the Xcode scheme editor highlighting the GPU Frame Capture option.](/images/com.apple.Xcode/gputools-metal-debugger-essentials-capture-choose-options@2x.png)
4. Run your app by choosing Product > Run.
5. Click the Metal Capture button in the debug bar. ![An Xcode screenshot of the Metal Capture popover, accessible from the Metal Capture button in the debug bar.](/images/com.apple.Xcode/gputools-metal-debugger-essentials-capture-choose-capture@2x.png)
6. Select the scope and count that you want to capture.
7. Click Capture.

Xcode automatically starts capturing a GPU trace when the scope starts, then finishes the capture based on the count you select. To manually stop the capture, you can click the Finish button at any time.

##### Configure Advanced Capture Options

The Metal Capture popover includes an Advanced section with additional options for controlling capture behavior. To reveal these options, click Show next to Advanced in the popover.

![A screenshot of the Metal Capture popover with the Advanced section expanded, showing additional capture options.](/images/com.apple.Xcode/gputools-metal-debugger-essentials-capture-popup-expanded@2x.png)

The advanced capture options include the following:

- **Keyboard shortcut**: Choose a keyboard shortcut to start a capture while your app is in the foreground. This option is only available on macOS.
- **Profile after replay**: Automatically profile your captured workload with default settings after Xcode finishes replaying it. Profiling has an initial performance impact on the Metal debugger, so only enable this option when debugging your app’s performance. You can always profile later as needed.
- **Include MetalFX temporal scaler history**: Record historical data for MetalFX temporal scalers to improve captured texture quality during replay. Enabling this option can make captures slower. This option is available when your app uses MetalFX temporal scaling.
- **Optimize shared memory capture**: Control how Xcode optimizes capturing CPU writes to resources using shared memory storage, which can improve capture performance and reduce the GPU trace’s size on disk. - **Automatic**: Xcode enables the optimization when Xcode can determine that the environment supports it safely, and disables it when system call interposition is unavailable.
- **Always**: Force the optimization on regardless of environment. Use this when you have large or slow GPU frame captures and know your app doesn’t write to shared-memory buffers via system calls.
- **Never**: Disable the optimization entirely. Use this if you suspect the optimization is producing incorrect results.

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
- [Debugging with interactive command-line tools](debugging-with-interactive-command-line-tools.md)
  Investigate rendering issues in GPU traces without leaving the Terminal.
- [Investigating GPU issues with AI agents](investigating-gpu-issues-with-ai-agents.md)
  Find the root cause of an issue in a large GPU trace by handing the trace to an AI agent for autonomous investigation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/capturing-a-metal-workload-in-xcode)*