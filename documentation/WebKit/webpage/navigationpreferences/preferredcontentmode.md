# preferredContentMode

**Framework**: WebKit  
**Kind**: property

The content mode for the web view to use when it loads and renders a webpage.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
var preferredContentMode: WebPage.NavigationPreferences.ContentMode
```

#### Discussion

The default value of this property is `recommended`. The web page ignores this preference for subframe navigation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigationpreferences/preferredcontentmode)*