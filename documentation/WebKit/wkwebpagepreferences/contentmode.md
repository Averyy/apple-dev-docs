# WKWebpagePreferences.ContentMode

**Framework**: WebKit  
**Kind**: enum

Constants that indicate how to render web view content.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
enum ContentMode
```

#### Overview

Browsers often render webpages differently based on device type. For example, Safari provides a desktop-class experience when displaying webpages on Mac and iPad, but it displays a mobile experience when displaying pages on iPhone. Use content modes to specify how you want your web view to render content within your app.

## Topics

### Getting the Content Modes
- [WKWebpagePreferences.ContentMode.recommended](wkwebpagepreferences/contentmode/recommended.md)
  The content mode that is appropriate for the current device.
- [WKWebpagePreferences.ContentMode.desktop](wkwebpagepreferences/contentmode/desktop.md)
  The content mode that represents a desktop experience.
- [WKWebpagePreferences.ContentMode.mobile](wkwebpagepreferences/contentmode/mobile.md)
  The content mode that represents a mobile experience.
### Initializers
- [init?(rawValue: Int)](wkwebpagepreferences/contentmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var preferredContentMode: WKWebpagePreferences.ContentMode](wkwebpagepreferences/preferredcontentmode.md)
  The content mode for the web view to use when it loads and renders a webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebpagepreferences/contentmode)*