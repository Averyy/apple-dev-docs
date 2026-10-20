# mainResource

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s main resource.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var mainResource: WebResource! { get }
```

```objc
@property (nonatomic, strong, readonly) WebResource * mainResource;
```

## See Also

### Getting attributes
- [var subresources: [Any]!](./subresources.md)
  The receiver’s subresources, or `nil` if there are none.
- [var subframeArchives: [Any]!](./subframearchives.md)
  Archives representing the receiver’s subresources or `nil` if there are none.
- [var data: Data!](./data.md)
  The data representation of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webarchive/mainresource)*