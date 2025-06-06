# setZoomFactor(_:for:completionHandler:)

**Framework**: Webkit  
**Kind**: method

Called to set the zoom factor of the tab.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func setZoomFactor(_ zoomFactor: Double, for context: WKWebExtensionContext) async throws
```

#### Discussion

Sets [`pageZoom`](wkwebview/pagezoom.md) of the tab’s web view if not implemented.

## Parameters

- `zoomFactor`: The desired zoom factor for the tab.
- `context`: The context in which the web extension is running.
- `completionHandler`: A block that must be called upon completion. It takes a single error argument, which should be provided if any errors occurred.

## See Also

- [func zoomFactor(for: WKWebExtensionContext) -> Double](wkwebextensiontab/zoomfactor(for:).md)
  Called when the zoom factor of the tab is needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/setzoomfactor(_:for:completionhandler:))*