# setURLSchemeHandler(_:forURLScheme:)

**Framework**: WebKit  
**Kind**: method

Registers an object to load resources associated with the specified URL scheme.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setURLSchemeHandler(_ urlSchemeHandler: (any WKURLSchemeHandler)?, forURLScheme urlScheme: String)
```

#### Discussion

Use this method to register any custom resource types that your web content uses. For example, you might register a custom URL scheme for resources that you provide programmatically from your app.

It is a programmer error to call this method than one once for the same scheme.

> 💡 **Tip**:  To prevent future conflicts with WebKit, include the name of your app or company in any custom scheme names.

## Parameters

- `urlSchemeHandler`: The object to handle the URL scheme. This object must adopt the   protocol.
- `urlScheme`: It is a programmer error to register a handler for a scheme WebKit already handles, such as  , and this method raises an   if you try to do so. To determine whether WebKit handles a specific scheme, call the   class method of  .

## See Also

- [func urlSchemeHandler(forURLScheme: String) -> (any WKURLSchemeHandler)?](wkwebviewconfiguration/urlschemehandler(forurlscheme:).md)
  Returns the currently registered handler object for the specified URL scheme.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/seturlschemehandler(_:forurlscheme:))*