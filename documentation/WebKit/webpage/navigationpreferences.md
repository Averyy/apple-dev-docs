# WebPage.NavigationPreferences

**Framework**: WebKit  
**Kind**: struct  
**Role**: Structure

A type that specifies the behaviors to use when loading and rendering page content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct NavigationPreferences
```

## Overview

Create a `NavigationPreferences` value when you want to change the default rendering behavior of your web page. Typically, iOS devices render web content for a mobile experience, and Mac devices render content for a desktop experience.

## Topics

### Initializers
- [init()](./navigationpreferences/init%28%29.md)
  Creates a new NavigationPreferences value.
### Instance Properties
- [var allowsContentJavaScript: Bool](./navigationpreferences/allowscontentjavascript.md)
  Indicates whether JavaScript from web content is allowed to run.
- [var allowsJSHandleCreationInPageWorld: Bool](./navigationpreferences/allowsjshandlecreationinpageworld.md)
  Indicates whether `window.webkit.createJSHandle` will be available in `WKContentWorld.page` The default value of this property is `false`.
- [var alternateRequest: URLRequest?](./navigationpreferences/alternaterequest.md)
  Used to make changes to the network request that will be used for this navigation’s main resource load.
- [var isGlobalPrivacyControlEnabled: Bool](./navigationpreferences/isglobalprivacycontrolenabled.md)
  Whether the Global Privacy Control (GPC) signal is enabled for the navigation.
- [var isLockdownModeEnabled: Bool](./navigationpreferences/islockdownmodeenabled.md)
  A Boolean value that indicates whether to use Lockdown Mode in the web page.
- [var overrideReferrer: String?](./navigationpreferences/overridereferrer.md)
  Used to apply a custom `referer` header to all resource loads in the frame of this navigation.
- [var preferredContentMode: WebPage.NavigationPreferences.ContentMode](./navigationpreferences/preferredcontentmode.md)
  The content mode for the web view to use when it loads and renders a webpage.
- [var preferredHTTPSNavigationPolicy: WebPage.NavigationPreferences.UpgradeToHTTPSPolicy](./navigationpreferences/preferredhttpsnavigationpolicy.md)
  Used when performing a top-level navigation to a webpage.
- [var securityRestrictionMode: WebPage.NavigationPreferences.SecurityRestrictionMode](./navigationpreferences/securityrestrictionmode-swift.property.md)
  Security restriction mode for this navigation.
### Enumerations
- [WebPage.NavigationPreferences.ContentMode](./navigationpreferences/contentmode.md)
  Options to indicate how to render web view content.
- [WebPage.NavigationPreferences.SecurityRestrictionMode](./navigationpreferences/securityrestrictionmode-swift.enum.md)
  Security restriction modes for WebView content.
- [WebPage.NavigationPreferences.UpgradeToHTTPSPolicy](./navigationpreferences/upgradetohttpspolicy.md)
  Preference for loading a webpage with HTTPS, and how failures should be handled.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing navigation between webpages
- [protocol NavigationDeciding](./navigationdeciding.md)
  Allows providing custom behavior to handle navigation changes and to coordinate these changes for the web page’s main page.
- [WebPage.NavigationAction](./navigationaction.md)
  An object that contains information about an action that causes navigation to occur.
- [WebPage.NavigationResponse](./navigationresponse.md)
  An object that contains the response to a navigation request, and which you use to make navigation-related policy decisions.
- [WebPage.FrameInfo](./frameinfo.md)
  A type that contains information about a frame on a webpage.
- [WebPage.NavigationPreferences.ContentMode](./navigationpreferences/contentmode.md)
  Options to indicate how to render web view content.
- [WebPage.NavigationPreferences.UpgradeToHTTPSPolicy](./navigationpreferences/upgradetohttpspolicy.md)
  Preference for loading a webpage with HTTPS, and how failures should be handled.
- [WebPage.NavigationPreferences.SecurityRestrictionMode](./navigationpreferences/securityrestrictionmode-swift.enum.md)
  Security restriction modes for WebView content.
- [WebPage.FormInfo](./forminfo.md)
  A type that contains information about a form submission from a webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigationpreferences)*