# isForMainFrame

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the response targets the web view’s main frame.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
var isForMainFrame: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isForMainFrame) BOOL forMainFrame;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) if the response targets the main frame. The value is [`false`](../../Swift/false.md) if the response targets a different frame, such as the frame in a new window.

## See Also

### Getting Additional Response Information
- [var canShowMIMEType: Bool](./canshowmimetype.md)
  A Boolean value that indicates whether WebKit is capable of displaying the response’s MIME type natively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationresponse/isformainframe)*