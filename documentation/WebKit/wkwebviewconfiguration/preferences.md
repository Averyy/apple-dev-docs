# preferences

**Framework**: WebKit  
**Kind**: property

The object that manages the preference-related settings for the web view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var preferences: WKPreferences { get set }
```

#### Discussion

Use the preferences object in this property to customize the rendering, JavaScript, and other preferences related to your web view. You can also change the preferences by assigning a new WKPreferences object to this property.

## See Also

- [var defaultWebpagePreferences: WKWebpagePreferences!](wkwebviewconfiguration/defaultwebpagepreferences.md)
  The default preferences to use when loading and rendering content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/preferences)*