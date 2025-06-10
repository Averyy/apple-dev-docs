# canShowMIMEType

**Framework**: WebKit  
**Kind**: property

A Boolean value that indicates whether WebKit is capable of displaying the response’s MIME type natively.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var canShowMIMEType: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) if WebKit is able to display the MIME type.

## See Also

- [var isForMainFrame: Bool](wknavigationresponse/isformainframe.md)
  A Boolean value that indicates whether the response targets the web view’s main frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationresponse/canshowmimetype)*