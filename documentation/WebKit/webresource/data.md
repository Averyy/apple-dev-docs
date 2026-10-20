# data

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s data.

**Availability**:
- macOS

## Declaration

```swift
var data: Data! { get }
```

```objc
@property (nonatomic, copy, readonly) NSData * data;
```

## See Also

### Getting attributes
- [var url: URL!](./url.md)
  The receiver’s URL.
- [var mimeType: String!](./mimetype.md)
  The receiver’s MIME type.
- [var textEncodingName: String!](./textencodingname.md)
  The receiver’s text encoding name.
- [var frameName: String!](./framename.md)
  The name of the frame. If the receiver does not represent the contents of an entire HTML frame, this is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webresource/data)*