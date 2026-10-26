# FxCommandAPI_v2

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

Adds functionality to move the playhead to a specific timeline time.

**Availability**:
- FxPlug 4.2+

## Declaration

```swift
protocol FxCommandAPI_v2 : FxCommandAPI
```

```objc
@protocol FxCommandAPI_v2 <FxCommandAPI>
```

## Topics

### Moving the Playhead
- [func movePlayhead(to: CMTime) throws](./fxcommandapi_v2/moveplayhead%28to%29.md)
  Moves the playhead to the desired time.

## Relationships

### Inherits From
- [FxCommandAPI](./fxcommandapi.md)

## See Also

### User interface
- [Adding parameters to plug-ins](https://developer.apple.com/documentation/professional-video-applications/adding-parameters-to-plug-ins)
  Create standard and custom user-facing parameters for your plug-in that will appear in the inspector.
- [Adding onscreen controls to plug-ins](https://developer.apple.com/documentation/professional-video-applications/adding-onscreen-controls-to-plug-ins)
  Simplify user interaction by using onscreen controls for your FxPlug plug-in.
- [protocol FxPathAPI_v3](./fxpathapi_v3.md)
  An API that defines the methods to retrieve information about paths, shapes, and masks the user has drawn on an object.
- [protocol FxUndoAPI](./fxundoapi.md)
  An API that defines the methods that the host app implements to handle plug-in management of the host app’s undo queue.
- [protocol FxCommandAPI](./fxcommandapi.md)
  Commands that you can tell the host to perform.
- [protocol FxRemoteWindowAPI](./fxremotewindowapi.md)
  A protocol that allows the plug-in to request that the host create a window.
- [protocol FxRemoteWindowAPI_v2](./fxremotewindowapi_v2.md)
  A protocol that allows the plug-in to request that the host create a window with a defined minimum and maximum size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxcommandapi_v2)*