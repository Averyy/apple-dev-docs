# WKWebViewConfiguration

**Framework**: WebKit  
**Kind**: class

A collection of properties that you use to initialize a web view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class WKWebViewConfiguration
```

#### Overview

A [`WKWebViewConfiguration`](wkwebviewconfiguration.md) object provides information about how to configure a [`WKWebView`](wkwebview.md) object. Use your configuration object to specify:

- The initial cookies to make available to your web content
- Handlers for any custom URL schemes your web content uses
- Settings for how to handle media content
- Information about how to manage selections within the web view
- Custom scripts to inject into the webpage
- Custom rules that determine how to render content

You create a [`WKWebViewConfiguration`](wkwebviewconfiguration.md) object in your code, configure its properties, and pass it to the initializer of your [`WKWebView`](wkwebview.md) object. The web view incorporates your configuration settings only at creation time; you cannot change those settings dynamically later.

## Topics

### Configuring the web view’s behavior
- [var websiteDataStore: WKWebsiteDataStore](wkwebviewconfiguration/websitedatastore.md)
  The object you use to get and set the site’s cookies and to track the cached data objects.
- [var userContentController: WKUserContentController](wkwebviewconfiguration/usercontentcontroller.md)
  The object that coordinates interactions between your app’s native code and the webpage’s scripts and other content.
- [var processPool: WKProcessPool](wkwebviewconfiguration/processpool.md)
  The object that coordinates the processes the web view uses to render its web content and execute scripts.
- [var applicationNameForUserAgent: String?](wkwebviewconfiguration/applicationnameforuseragent.md)
  The app name that appears in the user agent string.
- [var limitsNavigationsToAppBoundDomains: Bool](wkwebviewconfiguration/limitsnavigationstoappbounddomains.md)
  A Boolean value that indicates whether the web view limits navigation to pages within the app’s domain.
- [var upgradeKnownHostsToHTTPS: Bool](wkwebviewconfiguration/upgradeknownhoststohttps.md)
  A Boolean value that indicates whether the web view should automatically upgrade supported HTTP requests to HTTPS.
### Configuring the web view’s preferences
- [var preferences: WKPreferences](wkwebviewconfiguration/preferences.md)
  The object that manages the preference-related settings for the web view.
- [var defaultWebpagePreferences: WKWebpagePreferences!](wkwebviewconfiguration/defaultwebpagepreferences.md)
  The default preferences to use when loading and rendering content.
### Adding handlers for custom URL schemes
- [func setURLSchemeHandler((any WKURLSchemeHandler)?, forURLScheme: String)](wkwebviewconfiguration/seturlschemehandler(_:forurlscheme:).md)
  Registers an object to load resources associated with the specified URL scheme.
- [func urlSchemeHandler(forURLScheme: String) -> (any WKURLSchemeHandler)?](wkwebviewconfiguration/urlschemehandler(forurlscheme:).md)
  Returns the currently registered handler object for the specified URL scheme.
### Configuring the rendering behavior
- [var ignoresViewportScaleLimits: Bool](wkwebviewconfiguration/ignoresviewportscalelimits.md)
  A Boolean value that determines whether a web view allows scaling of the webpage.
- [var suppressesIncrementalRendering: Bool](wkwebviewconfiguration/suppressesincrementalrendering.md)
  A Boolean value that indicates whether the web view suppresses content rendering until the content is fully loaded into memory.
### Setting media playback preferences
- [var allowsInlineMediaPlayback: Bool](wkwebviewconfiguration/allowsinlinemediaplayback.md)
  A Boolean value that indicates whether HTML5 videos play inline or use the native full-screen controller.
- [var allowsAirPlayForMediaPlayback: Bool](wkwebviewconfiguration/allowsairplayformediaplayback.md)
  A Boolean value that indicates whether the web view allows media playback over AirPlay.
- [var allowsPictureInPictureMediaPlayback: Bool](wkwebviewconfiguration/allowspictureinpicturemediaplayback.md)
  A Boolean value that indicates whether HTML5 videos can play Picture in Picture.
- [var mediaTypesRequiringUserActionForPlayback: WKAudiovisualMediaTypes](wkwebviewconfiguration/mediatypesrequiringuseractionforplayback.md)
  The media types that require a user gesture to begin playing.
- [struct WKAudiovisualMediaTypes](wkaudiovisualmediatypes.md)
  The media types that require a user gesture to begin playing.
### Identifying data types
- [var dataDetectorTypes: WKDataDetectorTypes](wkwebviewconfiguration/datadetectortypes.md)
  The types of data detectors to apply to the web view’s content.
- [struct WKDataDetectorTypes](wkdatadetectortypes.md)
  The data detector types.
### Setting selection granularity
- [var selectionGranularity: WKSelectionGranularity](wkwebviewconfiguration/selectiongranularity.md)
  The level of granularity with which the user can interactively select web view content.
- [enum WKSelectionGranularity](wkselectiongranularity.md)
  The granularity with which the user can select and modify web view content.
### Selecting user interface directionality
- [var userInterfaceDirectionPolicy: WKUserInterfaceDirectionPolicy](wkwebviewconfiguration/userinterfacedirectionpolicy.md)
  The directionality of user interface elements.
- [enum WKUserInterfaceDirectionPolicy](wkuserinterfacedirectionpolicy.md)
  The policy that determines the directionality of user interface elements in a web view.
### Deprecated
- [var mediaPlaybackAllowsAirPlay: Bool](wkwebviewconfiguration/mediaplaybackallowsairplay.md)
  Deprecated property.
- [var requiresUserActionForMediaPlayback: Bool](wkwebviewconfiguration/requiresuseractionformediaplayback.md)
  A Boolean value that indicates whether HTML5 videos require the user to start playing them (`true`) or whether the videos play automatically (`false`).
- [var mediaPlaybackRequiresUserAction: Bool](wkwebviewconfiguration/mediaplaybackrequiresuseraction.md)
  Deprecated property.
### Instance Properties
- [var allowsInlinePredictions: Bool](wkwebviewconfiguration/allowsinlinepredictions.md)
- [var showsSystemScreenTimeBlockingView: Bool](wkwebviewconfiguration/showssystemscreentimeblockingview.md)
- [var supportsAdaptiveImageGlyph: Bool](wkwebviewconfiguration/supportsadaptiveimageglyph.md)
- [var webExtensionController: WKWebExtensionController?](wkwebviewconfiguration/webextensioncontroller.md)
- [var writingToolsBehavior: UIWritingToolsBehavior](wkwebviewconfiguration/writingtoolsbehavior.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class WKWindowFeatures](wkwindowfeatures.md)
  Display-related attributes that a webpage requests for its window.
- [class WKProcessPool](wkprocesspool.md)
  An opaque token that you use to run multiple web views in a single process.
- [class WKPreferences](wkpreferences.md)
  An object that encapsulates the standard behaviors to apply to websites.
- [class WKWebpagePreferences](wkwebpagepreferences.md)
  An object that specifies the behaviors to use when loading and rendering page content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration)*