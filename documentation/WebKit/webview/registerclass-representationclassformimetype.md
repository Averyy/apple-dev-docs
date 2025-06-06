# registerClass(_:representationClass:forMIMEType:)

**Framework**: Webkit  
**Kind**: method

Specifies the view and representation objects to be used for specific MIME types.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
class func registerClass(_ viewClass: AnyClass!, representationClass: AnyClass!, forMIMEType MIMEType: String!)
```

#### Discussion

After invoking this method, when `MIMEType` content is encountered, instances of `representationClass` and `viewClass` are created to handle and display it.

## Parameters

- `viewClass`: A class conforming to the   protocol that displays the specified MIME types.
- `representationClass`: The class conforming to   protocol that represents the specified MIME types.
- `MIMEType`: This may be a primary MIME type or subtype. For example, if   is “video/” the specified view and representation objects are used for all video types. More specific subtype mappings, such as “image/gif”, takes precedence over primary type matching, such as “image/”.

## See Also

- [class func registerURLScheme(asLocal: String!)](webview/registerurlscheme(aslocal:).md)
  Adds the specified URL scheme to the list of local schemes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/registerclass(_:representationclass:formimetype:))*