# mimeType

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s MIME type.

**Availability**:
- macOS

## Declaration

```swift
var mimeType: String! { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * MIMEType;
```

## See Also

### Getting attributes
- [var data: Data!](./data.md)
  The receiver’s data.
- [var url: URL!](./url.md)
  The receiver’s URL.
- [var textEncodingName: String!](./textencodingname.md)
  The receiver’s text encoding name.
- [var frameName: String!](./framename.md)
  The name of the frame. If the receiver does not represent the contents of an entire HTML frame, this is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webresource/mimetype)*