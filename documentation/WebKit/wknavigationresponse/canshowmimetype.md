# canShowMIMEType

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether WebKit is capable of displaying the response’s MIME type natively.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
var canShowMIMEType: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL canShowMIMEType;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) if WebKit is able to display the MIME type.

## See Also

### Getting Additional Response Information
- [var isForMainFrame: Bool](./isformainframe.md)
  A Boolean value that indicates whether the response targets the web view’s main frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationresponse/canshowmimetype)*