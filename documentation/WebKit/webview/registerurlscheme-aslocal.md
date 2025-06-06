# registerURLScheme(asLocal:)

**Framework**: Webkit  
**Kind**: method

Adds the specified URL scheme to the list of local schemes.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
class func registerURLScheme(asLocal scheme: String!)
```

#### Discussion

You need to register a scheme as local to access resources with file URLs and to have the same security checks as a local file.

## Parameters

- `scheme`: The scheme to add to the list.

## See Also

- [class func registerClass(AnyClass!, representationClass: AnyClass!, forMIMEType: String!)](webview/registerclass(_:representationclass:formimetype:).md)
  Specifies the view and representation objects to be used for specific MIME types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/registerurlscheme(aslocal:))*