# urlSchemeHandler(forURLScheme:)

**Framework**: WebKit  
**Kind**: method

Returns the currently registered handler object for the specified URL scheme.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func urlSchemeHandler(forURLScheme urlScheme: String) -> (any WKURLSchemeHandler)?
```

#### Return Value

The handler object for the specified scheme, or `nil` if the scheme has no handler.

## Parameters

- `urlScheme`: The scheme to look up. Scheme names are case sensitive, must start with an ASCII letter, and may contain only ASCII letters, numbers, the “ ” character, the “ ” character, and the “ ” character. If this parameter contains an empty string or the scheme name includes invalid characters, this method returns  .

## See Also

- [func setURLSchemeHandler((any WKURLSchemeHandler)?, forURLScheme: String)](wkwebviewconfiguration/seturlschemehandler(_:forurlscheme:).md)
  Registers an object to load resources associated with the specified URL scheme.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/urlschemehandler(forurlscheme:))*