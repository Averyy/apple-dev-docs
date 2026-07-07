# WebPage.NavigationPreferences.UpgradeToHTTPSPolicy

**Framework**: WebKit  
**Kind**: enum

Preference for loading a webpage with HTTPS, and how failures should be handled.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum UpgradeToHTTPSPolicy
```

## Topics

### Enumeration Cases
- [WebPage.NavigationPreferences.UpgradeToHTTPSPolicy.automaticFallbackToHTTP](webpage/navigationpreferences/upgradetohttpspolicy/automaticfallbacktohttp.md)
- [WebPage.NavigationPreferences.UpgradeToHTTPSPolicy.errorOnFailure](webpage/navigationpreferences/upgradetohttpspolicy/erroronfailure.md)
- [WebPage.NavigationPreferences.UpgradeToHTTPSPolicy.keepAsRequested](webpage/navigationpreferences/upgradetohttpspolicy/keepasrequested.md)
- [WebPage.NavigationPreferences.UpgradeToHTTPSPolicy.userMediatedFallbackToHTTP](webpage/navigationpreferences/upgradetohttpspolicy/usermediatedfallbacktohttp.md)

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
- [WebPage.NavigationPreferences.ContentMode](webpage/navigationpreferences/contentmode.md)
  Options to indicate how to render web view content.
- [WebPage.NavigationPreferences.SecurityRestrictionMode](webpage/navigationpreferences/securityrestrictionmode-swift.enum.md)
  Security restriction modes for WebView content.
- [WebPage.FormInfo](webpage/forminfo.md)
  A type that contains information about a form submission from a webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigationpreferences/upgradetohttpspolicy)*