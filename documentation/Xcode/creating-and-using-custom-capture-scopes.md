# Creating and using custom capture scopes

**Framework**: Xcode  
**Role**: Article

Capture specific GPU commands by using custom capture scopes.

#### Overview

When you capture a frame using the default capture scope by clicking the Metal Capture button in Xcode’s debug bar, the resulting capture contains all of the data for a single frame. In some cases, you may want to debug a partial frame rather than an entire frame. You can accomplish this by setting up and using a custom capture scope that lets you choose exactly which Metal commands to record.

> **Note**: Don’t allocate custom capture scopes yourself. Instead, call one of the [`MTLCaptureManager`](../Metal/mtlcapturemanager.md) methods: [`makeCaptureScope(device:)`](../Metal/mtlcapturemanager/makecapturescope%28device%29.md) or [`makeCaptureScope(commandQueue:)`](../Metal/mtlcapturemanager/makecapturescope%28commandqueue%29-1rozd.md).

##### Define capture boundaries

Call [`begin()`](../Metal/mtlcapturescope/begin%28%29.md) on your capture scope to instruct the Metal debugger to record your app’s subsequent Metal activity. To stop recording a frame and to present the Metal debugger, call [`end()`](../Metal/mtlcapturescope/end%28%29.md).

```swift
// Create myCaptureScope outside of your rendering loop.
myCaptureScope.begin()

if let commandBuffer = commandQueue.makeCommandBuffer() {
    // Do Metal work.
    commandBuffer.commit()
}

myCaptureScope.end()
```

> ❗ **Important**: Create capture scopes outside your rendering or compute loop, situating your calls between [`begin()`](../Metal/mtlcapturescope/begin%28%29.md) and [`end()`](../Metal/mtlcapturescope/end%28%29.md). For Metal capture to work correctly, you need to hold a strong reference to an active capture scope for the duration of the work that the capture scope contains.

##### Label your capture scope

To identify your custom capture scope when capturing a trace from the Metal Capture popover, set your capture scope’s label property.

```swift
myCaptureScope.label = "My Capture Scope"
```

When you’re ready to capture a frame, click the Metal Capture button in the debug bar. There, you can find your custom capture scope with the matching label available in the list for capturing.

Keep a strong reference to the capture scope in your code for as long as you want the option to be visible in Xcode.

##### Make a custom capture scope the default

When you perform a capture from Xcode, it defaults to the capture scope that [`defaultCaptureScope`](../Metal/mtlcapturemanager/defaultcapturescope.md) specifies. If the value of this property is `nil`, Xcode defines the default capture scope using drawable presentation boundaries; for example, using your calls to the methods [`present(_:)`](../Metal/mtlcommandbuffer/present%28_%29.md) or [`present()`](../Metal/mtldrawable/present%28%29.md).

To change the default scope, create an [`MTLCaptureScope`](../Metal/mtlcapturescope.md) instance and assign it to [`defaultCaptureScope`](../Metal/mtlcapturemanager/defaultcapturescope.md).

```swift
MTLCaptureManager.shared().defaultCaptureScope = myCaptureScope
```

## See Also

### Project preparation for debugging
- [Building your project with embedded shader sources](./building-your-project-with-embedded-shader-sources.md)
  Prepare to debug your project’s shaders by including source code in the build.
- [Naming resources and commands](./naming-resources-and-commands.md)
  Enhance the debugging of your Metal app using labels and grouping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/creating-and-using-custom-capture-scopes)*