# WebPage.NavigationPreferences.ContentMode

**Framework**: WebKit  
**Kind**: enum

Options to indicate how to render web view content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
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
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol NavigationDeciding](webpage/navigationdeciding.md)
  Allows providing custom behavior to handle navigation changes and to coordinate these changes for the web page’s main page.
- [WebPage.NavigationAction](webpage/navigationaction.md)
  An object that contains information about an action that causes navigation to occur.
- [WebPage.NavigationResponse](webpage/navigationresponse.md)
  An object that contains the response to a navigation request, and which you use to make navigation-related policy decisions.
- [WebPage.NavigationPreferences](webpage/navigationpreferences.md)
  A type that specifies the behaviors to use when loading and rendering page content.
- [WebPage.FrameInfo](webpage/frameinfo.md)
  A type that contains information about a frame on a webpage.
- [WebPage.NavigationPreferences.UpgradeToHTTPSPolicy](webpage/navigationpreferences/upgradetohttpspolicy.md)
  Preference for loading a webpage with HTTPS, and how failures should be handled.
- [WebPage.NavigationPreferences.SecurityRestrictionMode](webpage/navigationpreferences/securityrestrictionmode-swift.enum.md)
  Security restriction modes for WebView content.
- [WebPage.FormInfo](webpage/forminfo.md)
  A type that contains information about a form submission from a webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigationpreferences/contentmode)*