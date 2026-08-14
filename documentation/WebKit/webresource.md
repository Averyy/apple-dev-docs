# WebResource

**Framework**: WebKit  
**Kind**: class

A `WebResource` object represents a downloaded URL. It encapsulates the data of the download as well as other resource properties such as the URL, MIME type, and frame name.

**Availability**:
- macOS ?+

## Declaration

```swift
class WebResource
```

#### Overview

Use the [`init(data:url:mimeType:textEncodingName:frameName:)`](webresource/init(data:url:mimetype:textencodingname:framename:)-914h4.md) method to initialize a newly created `WebResource` object. Use the other methods in this class to get the properties of a `WebResource` object.

## Topics

### Initializing
- [init!(data: Data!, url: URL!, mimeType: String!, textEncodingName: String!, frameName: String!)](webresource/init(data:url:mimetype:textencodingname:framename:)-914h4.md)
  Initializes and returns a web resource instance.
### Getting attributes
- [var data: Data!](webresource/data.md)
  The receiver’s data.
- [var url: URL!](webresource/url.md)
  The receiver’s URL.
- [var mimeType: String!](webresource/mimetype.md)
  The receiver’s MIME type.
- [var textEncodingName: String!](webresource/textencodingname.md)
  The receiver’s text encoding name.
- [var frameName: String!](webresource/framename.md)
  The name of the frame. If the receiver does not represent the contents of an entire HTML frame, this is `nil`.
### Initializers
- [init?(coder: NSCoder)](webresource/init(coder:).md)
- [init!(data: Data!, URL: URL!, MIMEType: String!, textEncodingName: String!, frameName: String!)](webresource/init(data:url:mimetype:textencodingname:framename:)-6mz1.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [WebKit Objective-C Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/DisplayWebContent.html#//apple_ref/doc/uid/10000164i)
- [protocol WebResourceLoadDelegate](webresourceloaddelegate.md)
  Web view resource load delegates implement this protocol to be notified on the progress of loading individual resources. Note that there can be hundreds of resources, such as images and other media, per page. So, if you just want to get page loading status see the WebFrameLoadDelegate protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webresource)*