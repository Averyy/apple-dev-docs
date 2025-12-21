# WebPage.NavigationPreferences.ContentMode

**Framework**: WebKit  
**Kind**: enum

Options to indicate how to render web view content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum ContentMode
```

#### Overview

Browsers often render webpages differently based on device type. For example, Safari provides a desktop-class experience when displaying webpages on Mac and iPad, but it displays a mobile experience when displaying pages on iPhone. Use content modes to specify how you want your web page to render content within your app.

## Topics

### Enumeration Cases
- [WebPage.NavigationPreferences.ContentMode.desktop](webpage/navigationpreferences/contentmode/desktop.md)
  The content mode that represents a desktop experience.
- [WebPage.NavigationPreferences.ContentMode.mobile](webpage/navigationpreferences/contentmode/mobile.md)
  The content mode that represents a mobile experience.
- [WebPage.NavigationPreferences.ContentMode.recommended](webpage/navigationpreferences/contentmode/recommended.md)
  The content mode that is appropriate for the current device.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigationpreferences/contentmode)*