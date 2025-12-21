# WebPage.NavigationPreferences

**Framework**: WebKit  
**Kind**: struct

A type that specifies the behaviors to use when loading and rendering page content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct NavigationPreferences
```

#### Overview

Create a `NavigationPreferences` value when you want to change the default rendering behavior of your web page. Typically, iOS devices render web content for a mobile experience, and Mac devices render content for a desktop experience.

## Topics

### Initializers
- [init()](webpage/navigationpreferences/init.md)
  Creates a new NavigationPreferences value.
### Instance Properties
- [var allowsContentJavaScript: Bool](webpage/navigationpreferences/allowscontentjavascript.md)
  Indicates whether JavaScript from web content is allowed to run.
- [var isLockdownModeEnabled: Bool](webpage/navigationpreferences/islockdownmodeenabled.md)
  A Boolean value that indicates whether to use Lockdown Mode in the web page.
- [var preferredContentMode: WebPage.NavigationPreferences.ContentMode](webpage/navigationpreferences/preferredcontentmode.md)
  The content mode for the web view to use when it loads and renders a webpage.
- [var preferredHTTPSNavigationPolicy: WebPage.NavigationPreferences.UpgradeToHTTPSPolicy](webpage/navigationpreferences/preferredhttpsnavigationpolicy.md)
  Used when performing a top-level navigation to a webpage.
### Enumerations
- [WebPage.NavigationPreferences.ContentMode](webpage/navigationpreferences/contentmode.md)
  Options to indicate how to render web view content.
- [WebPage.NavigationPreferences.UpgradeToHTTPSPolicy](webpage/navigationpreferences/upgradetohttpspolicy.md)
  Preference for loading a webpage with HTTPS, and how failures should be handled.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol NavigationDeciding](webpage/navigationdeciding.md)
  Allows providing custom behavior to handle navigation changes and to coordinate these changes for the web page’s main page.
- [WebPage.NavigationAction](webpage/navigationaction.md)
  An object that contains information about an action that causes navigation to occur.
- [WebPage.NavigationResponse](webpage/navigationresponse.md)
  An object that contains the response to a navigation request, and which you use to make navigation-related policy decisions.
- [WebPage.FrameInfo](webpage/frameinfo.md)
  A type that contains information about a frame on a webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigationpreferences)*