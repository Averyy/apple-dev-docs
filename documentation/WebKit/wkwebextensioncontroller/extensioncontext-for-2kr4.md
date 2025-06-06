# extensionContext(for:)

**Framework**: Webkit  
**Kind**: method

Returns a loaded extension context matching the specified URL.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func extensionContext(for URL: URL) -> WKWebExtensionContext?
```

#### Return Value

An extension context or `nil` if no match was found.

#### Discussion

This method is useful for determining the extension context to use when about to navigate to an extension URL. For example, you could use this method to retrieve the appropriate extension context and then use its [`webViewConfiguration`](wkwebextensioncontext/webviewconfiguration.md) property to configure a web view for loading that URL.

## Parameters

- `URL`: The URL to lookup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller/extensioncontext(for:)-2kr4)*