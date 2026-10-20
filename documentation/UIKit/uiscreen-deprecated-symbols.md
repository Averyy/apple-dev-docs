# Deprecated symbols

**Framework**: UIKit  
**Role**: API Collection

Review symbols that are no longer in active development, and their recommended replacements.

#### Overview

Although these symbols are available for use, Apple is no longer actively developing them, and may remove them in a future release. Apple recommends moving away from these symbols and using their indicated replacements instead. Check the individual symbol pages for the recommended replacements.

## Topics

### Deprecated properties
- [class var main: UIScreen](./uiscreen/main.md)
  Returns the screen object representing the device’s screen.
- [class var screens: [UIScreen]](./uiscreen/screens.md)
  Returns an array containing all of the screens attached to the device.
- [var applicationFrame: CGRect](./uiscreen/applicationframe.md)
  The frame rectangle for the app window, measured in points.
- [var focusedItem: (any UIFocusItem)?](./uiscreen/focuseditem.md)
  The item that is currently focused.
- [var focusedView: UIView?](./uiscreen/focusedview.md)
  The view that is currently focused.
- [var supportsFocus: Bool](./uiscreen/supportsfocus.md)
  A Boolean value that indicates whether the screen supports focus-based inputs.
- [var isCaptured: Bool](./uiscreen/iscaptured.md)
  A Boolean value that indicates whether the system is actively cloning the screen to another destination.
### Deprecated notifications
- [class let didConnectNotification: NSNotification.Name](./uiscreen/didconnectnotification.md)
  A notification the system posts when a new screen connects to the device.
- [class let didDisconnectNotification: NSNotification.Name](./uiscreen/diddisconnectnotification.md)
  A notification the system posts when a screen disconnects from the device.
### Deprecated methods
- [func displayLink(withTarget: Any, selector: Selector) -> CADisplayLink?](./uiscreen/displaylink%28withtarget,selector%29.md)
  Returns a display link object for the current screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen-deprecated-symbols)*