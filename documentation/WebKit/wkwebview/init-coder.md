# init(coder:)

**Framework**: WebKit  
**Kind**: init

Returns an object initialized from data in the specified coder object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init?(coder: NSCoder)
```

## Parameters

- `coder`: The coder object that contains the object’s data.

## See Also

- [init(frame: CGRect, configuration: WKWebViewConfiguration)](wkwebview/init(frame:configuration:).md)
  Creates a web view and initializes it with the specified frame and configuration data.
- [var configuration: WKWebViewConfiguration](wkwebview/configuration.md)
  The object that contains the configuration details for the web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/init(coder:))*