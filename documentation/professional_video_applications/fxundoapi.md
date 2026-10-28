# FxUndoAPI

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

An API that defines the methods that the host app implements to handle plug-in management of the host app’s undo queue.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
protocol FxUndoAPI
```

```objc
@protocol FxUndoAPI
```

## Overview

Note that not all host apps implement this protocol.

## Topics

### Creating Undo Groups
- [func startUndoGroup(String!) -> Bool](./fxundoapi/startundogroup%28_%29.md)
  Begins a new undo group.
- [func endUndoGroup() -> Bool](./fxundoapi/endundogroup%28%29.md)
  Closes the current undo group.

## See Also

### User interface
- [Adding parameters to plug-ins](../Professional-Video-Applications/adding-parameters-to-plug-ins.md)
  Create standard and custom user-facing parameters for your plug-in that will appear in the inspector.
- [Adding onscreen controls to plug-ins](../Professional-Video-Applications/adding-onscreen-controls-to-plug-ins.md)
  Simplify user interaction by using onscreen controls for your FxPlug plug-in.
- [protocol FxPathAPI_v3](./fxpathapi_v3.md)
  An API that defines the methods to retrieve information about paths, shapes, and masks the user has drawn on an object.
- [protocol FxCommandAPI](./fxcommandapi.md)
  Commands that you can tell the host to perform.
- [protocol FxCommandAPI_v2](./fxcommandapi_v2.md)
  Adds functionality to move the playhead to a specific timeline time.
- [protocol FxRemoteWindowAPI](./fxremotewindowapi.md)
  A protocol that allows the plug-in to request that the host create a window.
- [protocol FxRemoteWindowAPI_v2](./fxremotewindowapi_v2.md)
  A protocol that allows the plug-in to request that the host create a window with a defined minimum and maximum size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxundoapi)*