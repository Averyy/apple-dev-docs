# WebKit for SwiftUI

**Framework**: WebKit

Integrate web content into your SwiftUI apps with new standard views you connect to webpages.

#### Overview

Present web content in your SwiftUI app with WebKit for SwiftUI. Use WebKit features to observe content and customize the web browsing and display experience.

Create a [`WebView`](webview-swift.struct.md) with a [`URL`](https://developer.apple.com/documentation/foundation/url) to display your web content. Apply view modifiers for various customizations, like displaying a find navigator, customizing scrolling behavior, configuring gesture behavior, and more.

Connect [`WebView`](webview-swift.struct.md) to a [`WebPage`](webpage.md) to interact with and react to changes in web content, such as observing navigation progress and calling JavaScript. You can use [`WebPage`](webpage.md) by itself when you don’t need to display the content directly.

> **Note**: For more information about using WebKit in your app using SwiftUI, see [`Meet WebKit for SwiftUI`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2025/231) from WWDC25.

## Topics

### Essentials
- [Building a cross-platform web browser](building-a-cross-platform-web-browser.md)
  Implement a browser on multiple platforms that loads content, manages navigation history, and saves favorite websites, using WebKit for SwiftUI.
- [struct WebView](webview-swift.struct.md)
  A view that displays some web content.
- [class WebPage](webpage.md)
  An object that controls and manages the behavior of interactive web content.
### Managing navigation between webpages
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
- [WebPage.NavigationPreferences.UpgradeToHTTPSPolicy](webpage/navigationpreferences/upgradetohttpspolicy.md)
  Preference for loading a webpage with HTTPS, and how failures should be handled.
- [WebPage.NavigationPreferences.SecurityRestrictionMode](webpage/navigationpreferences/securityrestrictionmode-swift.enum.md)
  Security restriction modes for WebView content.
- [WebPage.FormInfo](webpage/forminfo.md)
  A type that contains information about a form submission from a webpage.
### Observing navigation between webpages
- [WebPage.BackForwardList](webpage/backforwardlist-swift.struct.md)
  An observable representation of a webpage’s previously loaded resources.
- [WebPage.NavigationEvent](webpage/navigationevent.md)
  A particular state that occurs during the progression of a navigation.
- [WebPage.BackForwardList.Item](webpage/backforwardlist-swift.struct/item.md)
  A representation of a resource that a webpage previously visited.
- [WebPage.BackForwardList.Item.ID](webpage/backforwardlist-swift.struct/item/id-swift.struct.md)
  An opaque type representing the identifier for an item.
### Configuring a WebPage
- [WebPage.Configuration](webpage/configuration.md)
  A configuration type that specifies the preferences and behaviors of a webpage.
- [WebPage.DeviceSensorAuthorization](webpage/devicesensorauthorization.md)
  A type that describes the authorization permissions policy for the device’s sensors a web resource may access.
- [struct URLScheme](urlscheme.md)
  A type representing a valid URL scheme.
- [protocol URLSchemeHandler](urlschemehandler.md)
  A protocol for loading resources with URL schemes that WebKit doesn’t handle.
- [enum URLSchemeTaskResult](urlschemetaskresult.md)
  A value used as part of a sequence of results from a [`URLSchemeHandler`](urlschemehandler.md), which can either be a `Data` or a `URLResponse`.
- [WebPage.Configuration.MediaPlaybackBehavior](webpage/configuration/mediaplaybackbehavior-swift.enum.md)
  The behavior used when playing HTML video within a page.
- [WebPage.DeviceSensorAuthorization.Permission](webpage/devicesensorauthorization/permission.md)
  The kind of sensor permission a web resource may request to access.
### Immersive environments
- [WebPage.ImmersiveEnvironment](webpage/immersiveenvironment.md)
  An object representing a website-provided immersive environment that is ready for presentation.
- [struct WebViewImmersiveEnvironmentView](webviewimmersiveenvironmentview.md)
  A SwiftUI view that renders a specific website-provided immersive environment.
- [var allowsImmersiveEnvironments: Bool](webpage/configuration/allowsimmersiveenvironments.md)
  Indicates whether website immersive environments are allowed.

## See Also

- [WebKit for AppKit and UIKit](webkit-for-appkit-and-uikit.md)
  Display web content in AppKit or UIKit apps, or apps built with Objective-C.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webkit-for-swiftui)*