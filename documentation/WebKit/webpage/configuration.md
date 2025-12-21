# WebPage.Configuration

**Framework**: WebKit  
**Kind**: struct

A configuration type that specifies the preferences and behaviors of a webpage.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
struct Configuration
```

## Topics

### Initializers
- [init()](webpage/configuration/init.md)
  Creates a new configuration value.
### Instance Properties
- [var allowsAirPlayForMediaPlayback: Bool](webpage/configuration/allowsairplayformediaplayback.md)
  Indicates whether the webpage allows media playback over AirPlay.
- [var allowsInlinePredictions: Bool](webpage/configuration/allowsinlinepredictions.md)
  Indicates whether inline predictions are allowed.
- [var applicationNameForUserAgent: String?](webpage/configuration/applicationnameforuseragent.md)
  The app name that appears in the user agent string.
- [var dataDetectorTypes: WKDataDetectorTypes](webpage/configuration/datadetectortypes.md)
  The types of data detectors to apply to the webpage’s content.
- [var defaultNavigationPreferences: WebPage.NavigationPreferences](webpage/configuration/defaultnavigationpreferences.md)
  The default preferences to use when loading and rendering content.
- [var deviceSensorAuthorization: WebPage.DeviceSensorAuthorization](webpage/configuration/devicesensorauthorization.md)
  Allows specifying how web resources may access device sensors.
- [var ignoresViewportScaleLimits: Bool](webpage/configuration/ignoresviewportscalelimits.md)
  Determines whether a webpage allows scaling of the webpage.
- [var limitsNavigationsToAppBoundDomains: Bool](webpage/configuration/limitsnavigationstoappbounddomains.md)
  Indicates whether the web view limits navigation to pages within the app’s domain.
- [var loadsSubresources: Bool](webpage/configuration/loadssubresources.md)
  Indicates whether the webpage loads all of its subresources in addition to the main resource.
- [var mediaPlaybackBehavior: WebPage.Configuration.MediaPlaybackBehavior](webpage/configuration/mediaplaybackbehavior-swift.property.md)
  Indicates whether HTML5 videos play inline or use the native full-screen controller.
- [var showsSystemScreenTimeBlockingView: Bool](webpage/configuration/showssystemscreentimeblockingview.md)
  Indicates whether the webpage should use the system Screen Time blocking view.
- [var supportsAdaptiveImageGlyph: Bool](webpage/configuration/supportsadaptiveimageglyph.md)
  Indicates whether insertion of adaptive image glyphs is allowed.
- [var suppressesIncrementalRendering: Bool](webpage/configuration/suppressesincrementalrendering.md)
  Indicates whether the web view suppresses content rendering until the content is fully loaded into memory.
- [var upgradeKnownHostsToHTTPS: Bool](webpage/configuration/upgradeknownhoststohttps.md)
  Indicates whether the web view should automatically upgrade supported HTTP requests to HTTPS.
- [var urlSchemeHandlers: [URLScheme : any URLSchemeHandler]](webpage/configuration/urlschemehandlers.md)
  Allows registering an object to load resources associated with a specified URL scheme.
- [var userContentController: WKUserContentController](webpage/configuration/usercontentcontroller.md)
  The object that coordinates interactions between your app’s native code and the webpage’s scripts and other content.
- [var userInterfaceDirectionPolicy: WKUserInterfaceDirectionPolicy](webpage/configuration/userinterfacedirectionpolicy.md)
  The directionality of user interface elements.
- [var webExtensionController: WKWebExtensionController?](webpage/configuration/webextensioncontroller.md)
  The web extension controller to associate with the webpage.
- [var websiteDataStore: WKWebsiteDataStore](webpage/configuration/websitedatastore.md)
  The object you use to get and set the site’s cookies and to track the cached data objects.
### Enumerations
- [WebPage.Configuration.MediaPlaybackBehavior](webpage/configuration/mediaplaybackbehavior-swift.enum.md)
  The behavior used when playing HTML video within a page.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [WebPage.DeviceSensorAuthorization](webpage/devicesensorauthorization.md)
  A type that describes the authorization permissions policy for the device’s sensors a web resource may access.
- [struct URLScheme](urlscheme.md)
  A type representing a valid URL scheme.
- [protocol URLSchemeHandler](urlschemehandler.md)
  A protocol for loading resources with URL schemes that WebKit doesn’t handle.
- [enum URLSchemeTaskResult](urlschemetaskresult.md)
  A value used as part of a sequence of results from a [`URLSchemeHandler`](urlschemehandler.md), which can either be a `Data` or a `URLResponse`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/configuration)*