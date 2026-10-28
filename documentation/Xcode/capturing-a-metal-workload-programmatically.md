# Capturing a Metal workload programmatically

**Framework**: Xcode  
**Role**: Article

Analyze your app’s performance by invoking Metal’s frame capture.

## Overview

Use the [`MTLCaptureManager`](../Metal/mtlcapturemanager.md) to programmatically capture information about commands you send to a specific device object. For example, you can capture a specific frame or part of a frame, depending on your needs, by implementing a custom UI that triggers a capture, or by programmatically triggering a capture at runtime from within your app.

### Enable capturing programmatically

To enable Metal capture in your app, add the `MetalCaptureEnabled` key to your `Info.plist` file with a value of `YES`. In Xcode’s property list editor, this key appears as `Metal Capture Enabled`.

Alternatively, in macOS 14 and later, you can set the environment variable on your Metal app: `MTL_CAPTURE_ENABLED=1`.

> 💡 **Tip**: Enabling Metal capture has a tiny, but measurable, effect on your app’s CPU processing time. You may want to set the value of this key using a build setting in your project so that you can enable it for some builds, but not for your final release build.

### Capture a device or command queue

Create an [`MTLCaptureDescriptor`](../Metal/mtlcapturedescriptor.md) object that defines which commands you want to record and what needs to happen after the capture is complete. To capture commands for a specific [`MTLDevice`](../Metal/mtldevice.md) or [`MTLCommandQueue`](../Metal/mtlcommandqueue.md), set the capture descriptor’s [`captureObject`](../Metal/mtlcapturedescriptor/captureobject.md) property to point at the specific object to track, and call the [`startCapture(with:)`](../Metal/mtlcapturemanager/startcapture%28with%29.md) method. To stop capturing commands, call the [`stopCapture()`](../Metal/mtlcapturemanager/stopcapture%28%29.md) method.

```swift
func triggerProgrammaticCapture(device: MTLDevice) {
    let captureManager = MTLCaptureManager.shared()
    let captureDescriptor = MTLCaptureDescriptor()
    captureDescriptor.captureObject = self.device
    do {
        try captureManager.startCapture(with: captureDescriptor)
    } catch {
        fatalError("error when trying to capture: \(error)")
    }
}

func runMetalCommands(commandQueue: MTLCommandQueue) {
    let commandBuffer = commandQueue.makeCommandBuffer()!
    // Do Metal work.
    commandBuffer.commit()
    let captureManager = MTLCaptureManager.shared()
    captureManager.stopCapture()
}
```

The capture manager captures commands only within [`MTLCommandBuffer`](../Metal/mtlcommandbuffer.md) objects that you create after the capture starts and commit before the capture stops.

> 💡 **Tip**: When you capture a frame programmatically, you can capture Metal commands that span multiple frames. For example, by calling `startCapture` at the start of frame 1 and `stopCapture` after frame 3, the traces contain command data from all the buffers that the system commits in the three frames.

### Capture specific commands with a capture scope

To learn how to add custom scopes to your app, see [Creating and using custom capture scopes](./creating-and-using-custom-capture-scopes.md). To capture commands using a custom scope, create an [`MTLCaptureScope`](../Metal/mtlcapturescope.md) object and set the capture descriptor’s [`captureObject`](../Metal/mtlcapturedescriptor/captureobject.md) property to point to it.

> ❗ **Important**: Set the file extension of the `outputURL` to `.gputrace` to ensure that you can replay it later in the Metal debugger. For more information on replaying GPU trace files, see [Replaying a GPU trace file](./replaying-a-gpu-trace-file.md).

```swift
func setupProgrammaticCaptureScope(device: MTLDevice) {
    myCaptureScope = MTLCaptureManager.shared().makeCaptureScope(device: device)
    myCaptureScope?.label = "My Capture Scope"
}

func triggerProgrammaticCaptureScope() {
    guard let captureScope = myCaptureScope else { return }
    let captureManager = MTLCaptureManager.shared()
    let captureDescriptor = MTLCaptureDescriptor()
    captureDescriptor.captureObject = captureScope
    do {
        try captureManager.startCapture(with: captureDescriptor)
    } catch {
        fatalError("error when trying to capture: \(error)")
    }
}
```

To define boundaries for the scoped capture, call the [`MTLCaptureScope`](../Metal/mtlcapturescope.md) object’s [`begin()`](../Metal/mtlcapturescope/begin%28%29.md) and [`end()`](../Metal/mtlcapturescope/end%28%29.md) methods just before and after the commands that you want to capture. Xcode automatically stops capturing when your app reaches the corresponding `end()` method of the capture scope.

```swift
func runMetalCommands(commandQueue: MTLCommandQueue) {
    myCaptureScope?.begin()
    let commandBuffer = commandQueue.makeCommandBuffer()!
    // Do Metal work.
    commandBuffer.commit()
    myCaptureScope?.end()
}
```

> ❗ **Important**: The capture scope captures commands only within [`MTLCommandBuffer`](../Metal/mtlcommandbuffer.md) objects that you create after the scope begins and commit before the scope ends.

### Save the capture to your computer

If you want to analyze the capture later, you can skip launching the Metal debugger and save the GPU command information to a GPU trace file. Call [`supportsDestination(_:)`](../Metal/mtlcapturemanager/supportsdestination%28_%29.md) on the capture manager to make sure the feature is available before attempting to record a trace file.

```swift
let captureManager = MTLCaptureManager.shared()

guard captureManager.supportsDestination(.gpuTraceDocument) else {
    print("Capturing to a GPU trace file isn't supported.")
    return
}
```

Then, set the capture descriptor’s destination property to `MTLCaptureDestination.gpuTraceDocument` and specify the file’s destination.

```swift
let captureDescriptor = MTLCaptureDescriptor()
captureDescriptor.captureObject = self.device
captureDescriptor.destination = .gpuTraceDocument
captureDescriptor.outputURL = self.traceURL
...
```

For more information on replaying GPU trace files, see [Replaying a GPU trace file](./replaying-a-gpu-trace-file.md).

## See Also

### Essentials
- [Capturing a Metal workload in Xcode](./capturing-a-metal-workload-in-xcode.md)
  Analyze your app’s performance by configuring your project to use the Metal debugger.
- [Replaying a GPU trace file](./replaying-a-gpu-trace-file.md)
  Debug and profile your app’s performance using a GPU trace file in the Metal debugger.
- [Investigating visual artifacts](./investigating-visual-artifacts.md)
  Discover, diagnose, and fix visual artifacts in your app with the Metal debugger.
- [Optimizing GPU performance](./optimizing-gpu-performance.md)
  Find and address performance bottlenecks using the Metal debugger.
- [Debugging with interactive command-line tools](./debugging-with-interactive-command-line-tools.md)
  Investigate rendering issues in GPU traces without leaving the Terminal.
- [Investigating GPU issues with AI agents](./investigating-gpu-issues-with-ai-agents.md)
  Find the root cause of an issue in a large GPU trace by handing the trace to an AI agent for autonomous investigation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/capturing-a-metal-workload-programmatically)*