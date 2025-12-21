# defaultNavigationPreferences

**Framework**: WebKit  
**Kind**: property

The default preferences to use when loading and rendering content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
var defaultNavigationPreferences: WebPage.NavigationPreferences
```

#### Discussion

Use this property to specify the JavaScript settings and content mode for new navigations. When the webpage navigates to a new resource, it passes the default preferences to its navigation decider, which can modify the preferences if desired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/configuration/defaultnavigationpreferences)*