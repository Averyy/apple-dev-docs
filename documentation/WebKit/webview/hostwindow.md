# hostWindow

**Framework**: Webkit  
**Kind**: property

The receiver’s host window.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
var hostWindow: NSWindow! { get set }
```

#### Discussion

Your application should only use this if a web view is going to be removed from its window temporarily, and you want the web view to continue operating (for example, you don’t want to interrupt a load in progress). Since the receiver maintains a copy of `hostWindow`, it is your responsibility to set the host window to `nil` before closing the window to avoid consuming excess memory.

For example, you might use this property if you attach a web view to an `NSTabView` object (as in a tabbed browser implementation). The `NSTabView` object takes views out of the window when they are not in the active tab, so you need to use this before the web view is removed from its window. If you don’t invoke this property, plug-ins will stop operating when the web view is removed from its window.

> **Note**:  Plug-ins and JavaScript depend on a window to function properly even if the web view is not in an actual window.

 Plug-ins and JavaScript depend on a window to function properly even if the web view is not in an actual window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/hostwindow)*