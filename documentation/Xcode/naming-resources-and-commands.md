# Naming resources and commands

**Framework**: Xcode  
**Role**: Article

Enhance the debugging of your Metal app using labels and grouping.

## Overview

Resource labels and command debug groups are useful when debugging and profiling your app using Metal tools. Assigning meaningful resource labels helps you find your specific resources more quickly. Logically grouping commands lets you easily navigate the workload after capturing it.

> **Note**: The properties and methods described here don’t affect the graphics-rendering or compute-processing behavior of your app.

### Annotate resources

Many Metal objects provide a [`label`](../Metal/mtlresource/label.md) property where you can assign a meaningful string. These labels appear in each Metal tool, allowing you to easily identify specific objects.

In addition, for [`MTLBuffer`](../Metal/mtlbuffer.md), the [`addDebugMarker(_:range:)`](../Metal/mtlbuffer/adddebugmarker%28_,range%29.md) method allows you to mark and identify specific data ranges. You can call the [`removeAllDebugMarkers()`](../Metal/mtlbuffer/removealldebugmarkers%28%29.md) method to clear the existing markers.

### Annotate commands

Command buffers and command encoders provide the following methods for you to easily identify specific groups of Metal commands in your app:

- On an [`MTLCommandBuffer`](../Metal/mtlcommandbuffer.md) object, call [`pushDebugGroup(_:)`](../Metal/mtlcommandbuffer/pushdebuggroup%28_%29.md) and [`popDebugGroup()`](../Metal/mtlcommandbuffer/popdebuggroup%28%29.md) to group commands within that buffer.
- On an [`MTLCommandEncoder`](../Metal/mtlcommandencoder.md) object, call [`pushDebugGroup(_:)`](../Metal/mtlcommandencoder/pushdebuggroup%28_%29.md) and [`popDebugGroup()`](../Metal/mtlcommandencoder/popdebuggroup%28%29.md) to group commands within that encoder. In addition, call [`insertDebugSignpost(_:)`](../Metal/mtlcommandencoder/insertdebugsignpost%28_%29.md) to mark interesting locations in the encoder.

Xcode pushes and pops debug groups using unique stacks that exist only within the lifetime of their associated [`MTLCommandBuffer`](../Metal/mtlcommandbuffer.md) or [`MTLCommandEncoder`](../Metal/mtlcommandencoder.md). You can nest debug groups by pushing multiple groups onto the stack before popping previous groups.

Use these methods to simplify your app development process, particularly for tasks that involve many Metal commands per buffer or encoder.

The following example demonstrates pushing and popping multiple debug groups:

```swift
func encodeRenderPass(commandBuffer: MTLCommandBuffer, descriptor: MTLRenderPassDescriptor) { 
    guard let renderEncoder = commandBuffer.makeRenderCommandEncoder(descriptor: descriptor) else { return }
    renderEncoder.label = "My Render Encoder"
    renderEncoder.pushDebugGroup("My Render Pass")

        renderEncoder.pushDebugGroup("Pipeline Setup")
        // Render pipeline commands.
        renderEncoder.popDebugGroup() // Pops "Pipeline Setup".

        renderEncoder.pushDebugGroup("Vertex Setup")
        // Vertex function commands.
        renderEncoder.popDebugGroup() // Pops "Vertex Setup".

        renderEncoder.pushDebugGroup("Fragment Setup")
        // Fragment function commands.
        renderEncoder.popDebugGroup() // Pops "Fragment Setup".

        renderEncoder.pushDebugGroup("Draw Calls")
        // Drawing commands.
        renderEncoder.popDebugGroup() // Pops "Draw Calls".

    renderEncoder.popDebugGroup() // Pops "My Render Pass".
    renderEncoder.endEncoding()
}
```

The following screenshot shows how the debug groups appear in Xcode’s Debug navigator after you capture a frame:

![A screenshot of Xcode’s Debug navigator showing nested debug groups inside a render pass.](https://developer.apple.com/tutorials/images/com.apple.Xcode/gputools-metal-debugger-debug-navigator-labels@2x.png)

## See Also

### Project preparation for debugging
- [Building your project with embedded shader sources](./building-your-project-with-embedded-shader-sources.md)
  Prepare to debug your project’s shaders by including source code in the build.
- [Creating and using custom capture scopes](./creating-and-using-custom-capture-scopes.md)
  Capture specific GPU commands by using custom capture scopes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/naming-resources-and-commands)*