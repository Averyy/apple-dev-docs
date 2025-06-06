# init(data:url:mimeType:textEncodingName:frameName:)

**Framework**: Webkit  
**Kind**: init

Initializes and returns a web resource instance.

**Availability**:
- macOS ?+

## Declaration

```swift
init!(data: Data!, url URL: URL!, mimeType MIMEType: String!, textEncodingName: String!, frameName: String!)
```

#### Return Value

An initialized web resource.

## Parameters

- `data`: The download data.
- `URL`: The download URL.
- `MIMEType`: The MIME type of the data.
- `textEncodingName`: The IANA encoding name (for example, “utf-8” or “utf-16”). This parameter may be  .
- `frameName`: The name of the frame. Use this parameter if the resource represents the contents of an entire HTML frame; otherwise pass  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webresource/init(data:url:mimetype:textencodingname:framename:))*