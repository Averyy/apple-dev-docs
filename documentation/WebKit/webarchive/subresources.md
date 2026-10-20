# subresources

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s subresources, or `nil` if there are none.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var subresources: [Any]! { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray * subresources;
```

## See Also

### Getting attributes
- [var mainResource: WebResource!](./mainresource.md)
  The receiver’s main resource.
- [var subframeArchives: [Any]!](./subframearchives.md)
  Archives representing the receiver’s subresources or `nil` if there are none.
- [var data: Data!](./data.md)
  The data representation of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webarchive/subresources)*