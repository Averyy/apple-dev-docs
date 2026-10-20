# url

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s URL.

**Availability**:
- macOS

## Declaration

```swift
var url: URL! { get }
```

```objc
@property (nonatomic, strong, readonly) NSURL * URL;
```

## See Also

### Getting attributes
- [var data: Data!](./data.md)
  The receiver’s data.
- [var mimeType: String!](./mimetype.md)
  The receiver’s MIME type.
- [var textEncodingName: String!](./textencodingname.md)
  The receiver’s text encoding name.
- [var frameName: String!](./framename.md)
  The name of the frame. If the receiver does not represent the contents of an entire HTML frame, this is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webresource/url)*