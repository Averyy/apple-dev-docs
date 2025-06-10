# Capturing a Metal workload programmatically

**Framework**: Xcode

Analyze your app’s performance by invoking Metal’s frame capture.

#### Overview

Use the [`MTLCaptureManager`](https://developer.apple.com/documentation/Metal/MTLCaptureManager) to programmatically capture information about commands you send to a specific device object. For example, you can capture a specific frame or part of a frame, depending on your needs, by implementing a custom UI that triggers a capture, or by programmatically triggering a capture at runtime from within your app.

##### Enable Capturing Programmatically

To enable Metal capture in your app, add the `MetalCaptureEnabled` key to your `Info.plist` file with a value of `YES`. In Xcode’s property list editor, this key appears as `Metal Capture Enabled`.

Alternatively, in macOS 14 and later, you can set the environment variable on your Metal app: `MTL_CAPTURE_ENABLED=1`.

> 💡 **Tip**: Enabling Metal capture has a tiny, but measurable, effect on your app’s CPU processing time. You may want to set the value of this key using a build setting in your project so that you can enable it for some builds, but not for your final release build.

##### Capture a Device or Command Queue

Create an [`MTLCaptureDescriptor`](https://developer.apple.com/documentation/Metal/MTLCaptureDescriptor) object that defines which commands you want to record and what needs to happen after the capture is complete. To capture commands for a specific [`MTLDevice`](https://developer.apple.com/documentation/Metal/MTLDevice) or [`MTLCommandQueue`](https://developer.apple.com/documentation/Metal/MTLCommandQueue), set the capture descriptor’s [`captureObject`](https://developer.apple.com/documentation/Metal/MTLCaptureDescriptor/captureObject) property to point at the specific object to track, and call the [`startCapture(with:)`](https://developer.apple.com/documentation/Metal/MTLCaptureManager/startCapture(with:)) method. To stop capturing commands, call the [`stopCapture()`](https://developer.apple.com/documentation/Metal/MTLCaptureManager/stopCapture()) method.

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

The capture manager captures commands only within [`MTLCommandBuffer`](https://developer.apple.com/documentation/Metal/MTLCommandBuffer) objects that you create after the capture starts and commit before the capture stops.

> 💡 **Tip**: When you capture a frame programmatically, you can capture Metal commands that span multiple frames. For example, by calling `startCapture` at the start of frame 1 and `stopCapture` after frame 3, the traces contain command data from all the buffers that the system commits in the three frames.

##### Capture Specific Commands with a Capture Scope

To learn how to add custom scopes to your app, see [`Creating and using custom capture scopes`](creating-and-using-custom-capture-scopes.md). To capture commands using a custom scope, create an [`MTLCaptureScope`](https://developer.apple.com/documentation/Metal/MTLCaptureScope) object and set the capture descriptor’s [`captureObject`](https://developer.apple.com/documentation/Metal/MTLCaptureDescriptor/captureObject) property to point to it.

> ❗ **Important**: Set the file extension of the `outputURL` to `.gputrace` to ensure that you can replay it later in the Metal debugger. For more information on replaying GPU trace files, see [`Replaying a GPU trace file`](replaying-a-gpu-trace-file.md).

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

To define boundaries for the scoped capture, call the [`MTLCaptureScope`](https://developer.apple.com/documentation/Metal/MTLCaptureScope) object’s [`begin()`](https://developer.apple.com/documentation/Metal/MTLCaptureScope/begin()) and [`end()`](https://developer.apple.com/documentation/Metal/MTLCaptureScope/end()) methods just before and after the commands that you want to capture. Xcode automatically stops capturing when your app reaches the corresponding `end()` method of the capture scope.

```swift
func runMetalCommands(commandQueue: MTLCommandQueue) {
    myCaptureScope?.begin()
    let commandBuffer = commandQueue.makeCommandBuffer()!
    // Do Metal work.
    commandBuffer.commit()
    myCaptureScope?.end()
}
```

> ❗ **Important**: The capture scope captures commands only within [`MTLCommandBuffer`](https://developer.apple.com/documentation/Metal/MTLCommandBuffer) objects that you create after the scope begins and commit before the scope ends.

##### Save the Capture to Your Computer

If you want to analyze the capture later, you can skip launching the Metal debugger and save the GPU command information to a GPU trace file. Call [`supportsDestination(_:)`](https://developer.apple.com/documentation/Metal/MTLCaptureManager/supportsDestination(_:)) on the capture manager to make sure the feature is available before attempting to record a trace file.

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

For more information on replaying GPU trace files, see [`Replaying a GPU trace file`](replaying-a-gpu-trace-file.md).

## See Also

- [Capturing a Metal workload in Xcode](capturing-a-metal-workload-in-xcode.md)
  Analyze your app’s performance by configuring your project to use the Metal debugger.
- [Replaying a GPU trace file](replaying-a-gpu-trace-file.md)
  Debug and profile your app’s performance using a GPU trace file in the Metal debugger.
- [Investigating visual artifacts](investigating-visual-artifacts.md)
  Discover, diagnose, and fix visual artifacts in your app with the Metal debugger.
- [Optimizing GPU performance](optimizing-gpu-performance.md)
  Find and address performance bottlenecks using the Metal debugger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/capturing-a-metal-workload-programmatically)*