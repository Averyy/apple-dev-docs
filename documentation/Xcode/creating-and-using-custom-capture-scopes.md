# Creating and using custom capture scopes

**Framework**: Xcode

Capture specific GPU commands by using custom capture scopes.

#### Overview

When you capture a frame using the default capture scope by clicking the Metal Capture button in Xcode’s debug bar, the resulting capture contains all of the data for a single frame. In some cases, you may want to debug a partial frame rather than an entire frame. You can accomplish this by setting up and using a custom capture scope that lets you choose exactly which Metal commands to record.

> **Note**: Don’t allocate custom capture scopes yourself. Instead, call one of the [`MTLCaptureManager`](https://developer.apple.com/documentation/Metal/MTLCaptureManager) methods: [`makeCaptureScope(device:)`](https://developer.apple.com/documentation/Metal/MTLCaptureManager/makeCaptureScope(device:)) or [`makeCaptureScope(commandQueue:)`](https://developer.apple.com/documentation/Metal/MTLCaptureManager/makeCaptureScope(commandQueue:)).

Don’t allocate custom capture scopes yourself. Instead, call one of the [`MTLCaptureManager`](https://developer.apple.com/documentation/Metal/MTLCaptureManager) methods: [`makeCaptureScope(device:)`](https://developer.apple.com/documentation/Metal/MTLCaptureManager/makeCaptureScope(device:)) or [`makeCaptureScope(commandQueue:)`](https://developer.apple.com/documentation/Metal/MTLCaptureManager/makeCaptureScope(commandQueue:)).

##### Define Capture Boundaries

Call [`begin()`](https://developer.apple.com/documentation/Metal/MTLCaptureScope/begin()) on your capture scope to instruct the Metal debugger to record your app’s subsequent Metal activity. To stop recording a frame and to present the Metal debugger, call [`end()`](https://developer.apple.com/documentation/Metal/MTLCaptureScope/end()).

```swift
// Create myCaptureScope outside of your rendering loop.
myCaptureScope.begin()

if let commandBuffer = commandQueue.makeCommandBuffer() {
    // Do Metal work.
    commandBuffer.commit()
}

myCaptureScope.end()
```

> ❗ **Important**: Create capture scopes outside your rendering or compute loop, situating your calls between [`begin()`](https://developer.apple.com/documentation/Metal/MTLCaptureScope/begin()) and [`end()`](https://developer.apple.com/documentation/Metal/MTLCaptureScope/end()). For Metal capture to work correctly, you need to hold a strong reference to an active capture scope for the duration of the work that the capture scope contains.

Create capture scopes outside your rendering or compute loop, situating your calls between [`begin()`](https://developer.apple.com/documentation/Metal/MTLCaptureScope/begin()) and [`end()`](https://developer.apple.com/documentation/Metal/MTLCaptureScope/end()). For Metal capture to work correctly, you need to hold a strong reference to an active capture scope for the duration of the work that the capture scope contains.

##### Label Your Capture Scope

To identify your custom capture scope when capturing a trace from the Metal Capture popover, set your capture scope’s label property.

```swift
myCaptureScope.label = "My Capture Scope"
```

When you’re ready to capture a frame, click the Metal Capture button in the debug bar. There, you can find your custom capture scope with the matching label available in the list for capturing.

Keep a strong reference to the capture scope in your code for as long as you want the option to be visible in Xcode.

##### Make a Custom Capture Scope the Default

When you perform a capture from Xcode, it defaults to the capture scope that [`defaultCaptureScope`](https://developer.apple.com/documentation/Metal/MTLCaptureManager/defaultCaptureScope) specifies. If the value of this property is `nil`, Xcode defines the default capture scope using drawable presentation boundaries; for example, using your calls to the methods [`present(_:)`](https://developer.apple.com/documentation/Metal/MTLCommandBuffer/present(_:)) or [`present()`](https://developer.apple.com/documentation/Metal/MTLDrawable/present()).

To change the default scope, create an [`MTLCaptureScope`](https://developer.apple.com/documentation/Metal/MTLCaptureScope) instance and assign it to [`defaultCaptureScope`](https://developer.apple.com/documentation/Metal/MTLCaptureManager/defaultCaptureScope).

```swift
MTLCaptureManager.shared().defaultCaptureScope = myCaptureScope
```

## See Also

- [Building your project with embedded shader sources](building-your-project-with-embedded-shader-sources.md)
  Prepare to debug your project’s shaders by including source code in the build.
- [Naming resources and commands](naming-resources-and-commands.md)
  Enhance the debugging of your Metal app using labels and grouping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/creating-and-using-custom-capture-scopes)*