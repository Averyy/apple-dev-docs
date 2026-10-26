# FxCommandAPI

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

Commands that you can tell the host to perform.

**Availability**:
- FxPlug 4.1+

## Declaration

```swift
protocol FxCommandAPI
```

```objc
@protocol FxCommandAPI
```

## Topics

### Instructing the Host to Perform a Command
- [func perform(FxCommand) throws](./fxcommandapi/perform%28_%29.md)
  Instructs the host application to perform a command.
### Handling and Defining Commands
- [protocol FxCommandHandler](./fxcommandhandler.md)
  Defines the methods a plug-in must implement to be notified of the application’s key binding for common commands.
- [enum FxCommand](./fxcommand.md)
  Defines the commands that can be performed by the host.
### Constants
- [var kKeyChar_UpArrow: unichar](./kkeychar_uparrow.md)
  The key character for Unicode 0x21de.
- [var kKeyChar_LeftArrow: unichar](./kkeychar_leftarrow.md)
  The key character for Unicode 0x21e0.
- [var kKeyChar_DownArrow: unichar](./kkeychar_downarrow.md)
  The key character for Unicode 0x21df.
- [var kKeyChar_RightArrow: unichar](./kkeychar_rightarrow.md)
  The key character for Unicode 0x21e2.
- [let kKey_Command: String](./kkey_command.md)
  The FxCommand that will be invoked by this keypress.
- [let kKey_Character: String](./kkey_character.md)
  The character the user must press to invoke the command.
- [let kKey_Modifiers: String](./kkey_modifiers.md)
  The modifiers the user must include in the keypress to invoke the command.

## Relationships

### Inherited By
- [FxCommandAPI_v2](./fxcommandapi_v2.md)

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
- [protocol FxCommandAPI_v2](./fxcommandapi_v2.md)
  Adds functionality to move the playhead to a specific timeline time.
- [protocol FxRemoteWindowAPI](./fxremotewindowapi.md)
  A protocol that allows the plug-in to request that the host create a window.
- [protocol FxRemoteWindowAPI_v2](./fxremotewindowapi_v2.md)
  A protocol that allows the plug-in to request that the host create a window with a defined minimum and maximum size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxcommandapi)*