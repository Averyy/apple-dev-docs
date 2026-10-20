# frameName

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The name of the frame. If the receiver does not represent the contents of an entire HTML frame, this is `nil`.

**Availability**:
- macOS

## Declaration

```swift
var frameName: String! { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * frameName;
```

## See Also

### Getting attributes
- [var data: Data!](./data.md)
  The receiver’s data.
- [var url: URL!](./url.md)
  The receiver’s URL.
- [var mimeType: String!](./mimetype.md)
  The receiver’s MIME type.
- [var textEncodingName: String!](./textencodingname.md)
  The receiver’s text encoding name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webresource/framename)*