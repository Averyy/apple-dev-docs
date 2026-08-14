# WKOpenPanelParameters

**Framework**: WebKit  
**Kind**: class

The configuration details of a file upload control in your web content.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 10.12+
- visionOS 2.4+

## Declaration

```swift
@MainActor
class WKOpenPanelParameters
```

#### Overview

Use a [`WKOpenPanelParameters`](wkopenpanelparameters.md) to determine the configuration of a file upload control. You don’t create this object directly. Instead, a web view creates one and passes it to the [`webView(_:runOpenPanelWith:initiatedByFrame:completionHandler:)`](wkuidelegate/webview(_:runopenpanelwith:initiatedbyframe:completionhandler:).md) method of its UI delegate object when it displays a file upload control.

## Topics

### Configuring the panel parameters
- [var allowsMultipleSelection: Bool](wkopenpanelparameters/allowsmultipleselection.md)
  A Boolean value that indicates whether the file upload control supports multiple files.
- [var allowsDirectories: Bool](wkopenpanelparameters/allowsdirectories.md)
  A Boolean value that indicates whether the file upload control supports the selection of directories.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)

## See Also

- [func webView(WKWebView, runOpenPanelWith: WKOpenPanelParameters, initiatedByFrame: WKFrameInfo, completionHandler: ([URL]?) -> Void)](wkuidelegate/webview(_:runopenpanelwith:initiatedbyframe:completionhandler:).md)
  Displays a file upload panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkopenpanelparameters)*