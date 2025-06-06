# registerCustomURLScheme(_:)

**Framework**: Webkit  
**Kind**: method

Registers a custom URL scheme that can be used in match patterns.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
class func registerCustomURLScheme(_ urlScheme: String)
```

#### Discussion

This method should be used to register any custom URL schemes used by the app for the extension base URLs, other than `webkit-extension`, or if extensions should have access to other supported URL schemes when using `<all_urls>`.

## Parameters

- `urlScheme`: The custom URL scheme to register.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/matchpattern/registercustomurlscheme(_:))*