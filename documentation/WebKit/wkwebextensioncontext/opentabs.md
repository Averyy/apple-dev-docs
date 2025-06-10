# openTabs

**Framework**: WebKit  
**Kind**: property

A set of open tabs in all open windows that are exposed to this extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var openTabs: Set<AnyHashable> { get }
```

#### Discussion

Provides a set of tabs in all open windows that are visible to the extension, as updated by the [`didOpenTab(_:)`](wkwebextensioncontext/didopentab(_:).md) and [`didCloseTab:windowIsClosing:`](wkwebextensioncontext/didclosetab:windowisclosing:.md) methods.

Initially populated by the tabs in the windows returned by the extension controller delegate method [`webExtensionController(_:openWindowsFor:)`](wkwebextensioncontrollerdelegate/webextensioncontroller(_:openwindowsfor:).md).

## See Also

- [func didOpenTab(any WKWebExtensionTab)](wkwebextensioncontext/didopentab(_:).md)
  Called by the app when a new tab is opened to fire appropriate events with only this extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/opentabs)*