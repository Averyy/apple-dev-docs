# subframeArchives

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

Archives representing the receiver’s subresources or `nil` if there are none.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var subframeArchives: [Any]! { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray * subframeArchives;
```

## See Also

### Getting attributes
- [var mainResource: WebResource!](./mainresource.md)
  The receiver’s main resource.
- [var subresources: [Any]!](./subresources.md)
  The receiver’s subresources, or `nil` if there are none.
- [var data: Data!](./data.md)
  The data representation of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webarchive/subframearchives)*