# isForMainFrame

**Framework**: Webkit  
**Kind**: property

A Boolean value that indicates whether the response targets the web view’s main frame.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isForMainFrame: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) if the response targets the main frame. The value is [`false`](https://developer.apple.com/documentation/swift/false) if the response targets a different frame, such as the frame in a new window.

## See Also

- [var canShowMIMEType: Bool](wknavigationresponse/canshowmimetype.md)
  A Boolean value that indicates whether WebKit is capable of displaying the response’s MIME type natively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationresponse/isformainframe)*