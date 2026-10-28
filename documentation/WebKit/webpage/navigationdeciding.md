# WebPage.NavigationDeciding

**Framework**: WebKit  
**Kind**: protocol  
**Role**: Protocol

Allows providing custom behavior to handle navigation changes and to coordinate these changes for the web page’s main page.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol NavigationDeciding
```

## Overview

For example, you might use these methods to restrict navigation from specific links within your content.

## Topics

### Instance Methods
- [func decideAuthenticationChallengeDisposition(for: URLAuthenticationChallenge) async -> (URLSession.AuthChallengeDisposition, URLCredential?)](./navigationdeciding/decideauthenticationchallengedisposition%28for%29.md)
  Determines the response to an authentication challenge.
- [func decidePolicy(for: WebPage.NavigationResponse) async -> WKNavigationResponsePolicy](./navigationdeciding/decidepolicy%28for%29.md)
  Determines permission to navigate to new content after the response to the navigation request is known.
- [func decidePolicy(for: WebPage.NavigationAction, preferences: inout WebPage.NavigationPreferences) async -> WKNavigationActionPolicy](./navigationdeciding/decidepolicy%28for,preferences%29.md)
  Determines permission to navigate to new content based on the specified preferences and action information.
- [func willSubmit(formInfo: WebPage.FormInfo) async](./navigationdeciding/willsubmit%28forminfo%29.md)
  Allow the application to process form autofill information before a form submission actually takes place.

## See Also

### Managing navigation between webpages
- [WebPage.NavigationAction](./navigationaction.md)
  An object that contains information about an action that causes navigation to occur.
- [WebPage.NavigationResponse](./navigationresponse.md)
  An object that contains the response to a navigation request, and which you use to make navigation-related policy decisions.
- [WebPage.NavigationPreferences](./navigationpreferences.md)
  A type that specifies the behaviors to use when loading and rendering page content.
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

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigationdeciding)*