# defaultWebpagePreferences

**Framework**: Webkit  
**Kind**: property

The default preferences to use when loading and rendering content.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var defaultWebpagePreferences: WKWebpagePreferences! { get set }
```

#### Discussion

Use this property to specify the JavaScript settings and content mode for new webpages. When the web view navigates to a new page, it passes the default preferences to its navigation delegate, which can modify the preferences or pass them as they are.

## See Also

- [var preferences: WKPreferences](wkwebviewconfiguration/preferences.md)
  The object that manages the preference-related settings for the web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/defaultwebpagepreferences)*