# zoomFactor(for:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Called when the zoom factor of the tab is needed.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
optional func zoomFactor(for context: WKWebExtensionContext) -> Double
```

```objc
- (double) zoomFactorForWebExtensionContext:(WKWebExtensionContext *) context;
```

#### Discussion

Defaults to [`pageZoom`](../wkwebview/pagezoom.md) of the tab’s web view if not implemented.

## Parameters

- `context`: The context in which the web extension is running.

## See Also

### Related Documentation
- [func setZoomFactor(Double, for: WKWebExtensionContext, completionHandler: ((any Error)?) -> Void)](./setzoomfactor%28_,for,completionhandler%29.md)
  Called to set the zoom factor of the tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/zoomfactor(for:))*