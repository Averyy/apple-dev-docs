# zoomFactor(for:)

**Framework**: Webkit  
**Kind**: method

Called when the zoom factor of the tab is needed.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func zoomFactor(for context: WKWebExtensionContext) -> Double
```

#### Discussion

Defaults to [`pageZoom`](wkwebview/pagezoom.md) of the tab’s web view if not implemented.

## Parameters

- `context`: The context in which the web extension is running.

## See Also

- [func setZoomFactor(Double, for: WKWebExtensionContext, completionHandler: ((any Error)?) -> Void)](wkwebextensiontab/setzoomfactor(_:for:completionhandler:).md)
  Called to set the zoom factor of the tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/zoomfactor(for:))*