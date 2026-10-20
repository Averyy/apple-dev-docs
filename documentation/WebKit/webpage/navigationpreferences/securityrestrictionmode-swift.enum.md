# WebPage.NavigationPreferences.SecurityRestrictionMode

**Framework**: WebKit  
**Kind**: enum  
**Role**: Enumeration

Security restriction modes for WebView content.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+

## Declaration

```swift
enum SecurityRestrictionMode
```

## Topics

### Enumeration Cases
- [WebPage.NavigationPreferences.SecurityRestrictionMode.lockdown](./securityrestrictionmode-swift.enum/lockdown.md)
  Maximum security restrictions including feature disablement. Applied automatically by the system in Lockdown Mode.
- [WebPage.NavigationPreferences.SecurityRestrictionMode.maximizeCompatibility](./securityrestrictionmode-swift.enum/maximizecompatibility.md)
  Enhanced security protections optimized for maintaining web compatibility. Disables JIT compilation and enables increased MTE adoption.
- [WebPage.NavigationPreferences.SecurityRestrictionMode.none](./securityrestrictionmode-swift.enum/none.md)
  No additional security restrictions beyond WebKit defaults.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Managing navigation between webpages
- [protocol NavigationDeciding](../navigationdeciding.md)
  Allows providing custom behavior to handle navigation changes and to coordinate these changes for the web page’s main page.
- [WebPage.NavigationAction](../navigationaction.md)
  An object that contains information about an action that causes navigation to occur.
- [WebPage.NavigationResponse](../navigationresponse.md)
  An object that contains the response to a navigation request, and which you use to make navigation-related policy decisions.
- [WebPage.NavigationPreferences](../navigationpreferences.md)
  A type that specifies the behaviors to use when loading and rendering page content.
- [WebPage.FrameInfo](../frameinfo.md)
  A type that contains information about a frame on a webpage.
- [WebPage.NavigationPreferences.ContentMode](./contentmode.md)
  Options to indicate how to render web view content.
- [WebPage.NavigationPreferences.UpgradeToHTTPSPolicy](./upgradetohttpspolicy.md)
  Preference for loading a webpage with HTTPS, and how failures should be handled.
- [WebPage.FormInfo](../forminfo.md)
  A type that contains information about a form submission from a webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigationpreferences/securityrestrictionmode-swift.enum)*