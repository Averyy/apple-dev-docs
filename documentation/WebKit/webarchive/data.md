# data

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The data representation of the receiver.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var data: Data! { get }
```

```objc
@property (nonatomic, copy, readonly) NSData * data;
```

#### Discussion

Can be used to save the web archive to a file, to put it on the pasteboard using the [`WebArchivePboardType`](../webarchivepboardtype.md) type, or used to initialize another web archive using the [`init(data:)`](./init%28data%29.md) method.

## See Also

### Getting attributes
- [var mainResource: WebResource!](./mainresource.md)
  The receiver’s main resource.
- [var subresources: [Any]!](./subresources.md)
  The receiver’s subresources, or `nil` if there are none.
- [var subframeArchives: [Any]!](./subframearchives.md)
  Archives representing the receiver’s subresources or `nil` if there are none.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webarchive/data)*