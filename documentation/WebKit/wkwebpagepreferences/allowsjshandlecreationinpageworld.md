# allowsJSHandleCreationInPageWorld

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var allowsJSHandleCreationInPageWorld: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsJSHandleCreationInPageWorld;
```

## Discussion

A boolean indicating whether `window.webkit.createJSHandle` will be available in `[WKContentWorld pageWorld]`

The default value is false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebpagepreferences/allowsjshandlecreationinpageworld)*