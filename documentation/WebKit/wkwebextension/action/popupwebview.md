# popupWebView

**Framework**: Webkit  
**Kind**: property

A web view loaded with the pop-up page for this action, or `nil` if no pop-up is specified.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var popupWebView: WKWebView? { get }
```

#### Discussion

The web view will be preloaded with the pop-up page upon first access or after it has been unloaded. Use the [`presentsPopup`](wkwebextension/action/presentspopup.md) property to determine whether a pop-up should be displayed before using this property.

## See Also

- [var presentsPopup: Bool](wkwebextension/action/presentspopup.md)
  A Boolean value indicating whether the action has a pop-up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/action/popupwebview)*