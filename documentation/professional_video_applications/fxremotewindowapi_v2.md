# FxRemoteWindowAPI_v2

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

A protocol that allows the plug-in to request that the host create a window with a defined minimum and maximum size.

**Availability**:
- FxPlug 4.2.3+

## Declaration

```swift
protocol FxRemoteWindowAPI_v2 : FxRemoteWindowAPI
```

```objc
@protocol FxRemoteWindowAPI_v2 <FxRemoteWindowAPI>
```

## Topics

### Creating a Window
- [func remoteWindow(withMinimumSize: CGSize, maximumSize: CGSize, reply: ((NSView?, (any Error)?) -> Void)!)](./fxremotewindowapi_v2/remotewindow%28withminimumsize,maximumsize,reply%29.md)
  Requests the host application to create a window with a minimum and maximum size that displays a custom UI.

## Relationships

### Inherits From
- [FxRemoteWindowAPI](./fxremotewindowapi.md)

## See Also

### User interface
- [Adding parameters to plug-ins](../Professional-Video-Applications/adding-parameters-to-plug-ins.md)
  Create standard and custom user-facing parameters for your plug-in that will appear in the inspector.
- [Adding onscreen controls to plug-ins](../Professional-Video-Applications/adding-onscreen-controls-to-plug-ins.md)
  Simplify user interaction by using onscreen controls for your FxPlug plug-in.
- [protocol FxPathAPI_v3](./fxpathapi_v3.md)
  An API that defines the methods to retrieve information about paths, shapes, and masks the user has drawn on an object.
- [protocol FxUndoAPI](./fxundoapi.md)
  An API that defines the methods that the host app implements to handle plug-in management of the host app’s undo queue.
- [protocol FxCommandAPI](./fxcommandapi.md)
  Commands that you can tell the host to perform.
- [protocol FxCommandAPI_v2](./fxcommandapi_v2.md)
  Adds functionality to move the playhead to a specific timeline time.
- [protocol FxRemoteWindowAPI](./fxremotewindowapi.md)
  A protocol that allows the plug-in to request that the host create a window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxremotewindowapi_v2)*