# WebPage

**Framework**: WebKit  
**Kind**: class

An object that controls and manages the behavior of interactive web content.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
final class WebPage
```

#### Overview

A [`WebPage`](webpage.md) is an [`Observable`](https://developer.apple.com/documentation/Observation/Observable) type, which you use to access various properties of web content and track changes to them. Use [`WebPage`](webpage.md) to interact with web content, like evaluating JavaScript or converting the page to PDF data. The following example shows how you can combine these capabilities to get specific metadata from an ephemeral page with a custom user agent:

```swift
func fetchMetadata(for url: URL) async throws -> Metadata {
    let botAgent = """
    Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.4 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.4 facebookexternalhit/1.1 Facebot Twitterbot/1.0
    """

    var configuration = WebPage.Configuration()
    configuration.loadsSubresources = false
    configuration.defaultNavigationPreferences.allowsContentJavaScript = false
    configuration.websiteDataStore = .nonPersistent()

    let page = WebPage(configuration: configuration)
    page.customUserAgent = botAgent

    let request = URLRequest(url: url)
    let navigationID = page.load(request)

    // Wait for the navigation to fully load by tracking changes to `currentNavigationEvent`.

    let fetchOpenGraphProperty = """
    const propertyValues = document.querySelectorAll(`meta[property="${property}"]`);
    return propertyValues[0];
    """

    let arguments = [
        "property": "og:description"
    ]

    guard let description = try await page.callJavaScript(fetchOpenGraphProperty, arguments: arguments) as? String else {
        throw FetchError.javaScriptInvalidResponseType
    }

    guard let title = page.title else {
        throw FetchError.noTitle
    }

    return Metadata(title: title, description: description)
}
```

Use [`WebPage`](webpage.md) to programmatically navigate to various types of resources like URL requests, HTML strings, and data. Optionally, you can observe these navigations by tracking changes to the [`currentNavigationEvent`](webpage/currentnavigationevent.md) property, and you can customize them by using a type that conforms to the [`WebPage.NavigationDeciding`](webpage/navigationdeciding.md) protocol. Use the [`backForwardList`](webpage/backforwardlist-swift.property.md) property to observe when people navigate in their history, and programmatically navigate to a specific back-forward list item.

## Topics

### Creating a WebPage
- [WebPage.Configuration](webpage/configuration.md)
- [convenience init(configuration: WebPage.Configuration)](webpage/init(configuration:).md)
- [convenience init(configuration: WebPage.Configuration, dialogPresenter: some WebPage.DialogPresenting)](webpage/init(configuration:dialogpresenter:).md)
- [convenience init(configuration: WebPage.Configuration, navigationDecider: some WebPage.NavigationDeciding)](webpage/init(configuration:navigationdecider:).md)
- [convenience init(configuration: WebPage.Configuration, navigationDecider: some WebPage.NavigationDeciding, dialogPresenter: some WebPage.DialogPresenting)](webpage/init(configuration:navigationdecider:dialogpresenter:).md)
### Managing navigation between webpages
- [protocol NavigationDeciding](webpage/navigationdeciding.md)
  Allows providing custom behavior to handle navigation changes and to coordinate these changes for the web page’s main page.
- [WebPage.NavigationAction](webpage/navigationaction.md)
  An object that contains information about an action that causes navigation to occur.
- [WebPage.NavigationResponse](webpage/navigationresponse.md)
  An object that contains the response to a navigation request, and which you use to make navigation-related policy decisions.
- [WebPage.NavigationPreferences](webpage/navigationpreferences.md)
  A type that specifies the behaviors to use when loading and rendering page content.
- [var backForwardList: WebPage.BackForwardList](webpage/backforwardlist-swift.property.md)
  The webpage’s back-forward list.
- [WebPage.FrameInfo](webpage/frameinfo.md)
  A type that contains information about a frame on a webpage.
### Observing navigation between webpages
- [WebPage.BackForwardList](webpage/backforwardlist-swift.struct.md)
  An observable representation of a webpage’s navigations.
- [WebPage.NavigationID](webpage/navigationid.md)
  An opaque identifier which can be used to uniquely identify a load request for a web page.
- [WebPage.NavigationEvent](webpage/navigationevent.md)
  A particular state that occurs during the progression of a navigation.
- [var currentNavigationEvent: WebPage.NavigationEvent?](webpage/currentnavigationevent.md)
  The current navigation event, or `nil` if there have been no navigations so far.
### Configuring a WebPage
- [WebPage.Configuration](webpage/configuration.md)
- [WebPage.DeviceSensorAuthorization](webpage/devicesensorauthorization.md)
  A type that describes the authorization permissions policy for the device’s sensors a web resource may access.
- [struct URLScheme](urlscheme.md)
  A type representing a valid URL scheme.
- [protocol URLSchemeHandler](urlschemehandler.md)
  A protocol for loading resources with URL schemes that WebKit doesn’t handle.
- [enum URLSchemeTaskResult](urlschemetaskresult.md)
### Loading web content
- [func load(WebPage.BackForwardList.Item) -> WebPage.NavigationID?](webpage/load(_:)-78prx.md)
  Navigates to an item from the back-forward list and sets it as the current item.
- [func load(URLRequest) -> WebPage.NavigationID?](webpage/load(_:)-75gd5.md)
  Loads the web content that the specified URL request object references and navigates to that content.
- [func load(Data, mimeType: String, characterEncoding: String.Encoding, baseURL: URL) -> WebPage.NavigationID?](webpage/load(_:mimetype:characterencoding:baseurl:).md)
  Loads the content of the specified data object and navigates to it.
- [func load(html: String, baseURL: URL) -> WebPage.NavigationID?](webpage/load(html:baseurl:).md)
  Loads the contents of the specified HTML string and navigates to it.
- [func load(simulatedRequest: URLRequest, responseHTML: String) -> WebPage.NavigationID?](webpage/load(simulatedrequest:responsehtml:).md)
  Loads the web content from the HTML you provide as if the HTML were the response to the request.
- [func load(simulatedRequest: URLRequest, response: URLResponse, responseData: Data) -> WebPage.NavigationID?](webpage/load(simulatedrequest:response:responsedata:).md)
  Loads the web content from the data you provide as if the data were the response to the request.
- [var isLoading: Bool](webpage/isloading.md)
  Indicates whether the webpage is currently loading content.
- [var estimatedProgress: Double](webpage/estimatedprogress.md)
  An estimate of completion percentage of the current navigation.
### Managing the loading process
- [func reload(fromOrigin: Bool) -> WebPage.NavigationID?](webpage/reload(fromorigin:).md)
  Reloads the current webpage.
- [func stopLoading()](webpage/stoploading.md)
  Stops loading all resources on the current page.
### Inspecting page information
- [WebPage.CSSMediaType](webpage/cssmediatype.md)
  A CSS media type as defined by the [`CSS specification`](https://developer.apple.comhttps://www.w3.org/TR/mediaqueries-4/#media-types), or an arbitrary media type value.
- [var title: String](webpage/title.md)
  The page title.
- [var url: URL?](webpage/url.md)
  The URL for the current webpage.
- [var mediaType: WebPage.CSSMediaType?](webpage/mediatype.md)
  The media type for the contents of the web view.
- [var customUserAgent: String?](webpage/customuseragent.md)
  The custom user agent string.
- [var serverTrust: SecTrust?](webpage/servertrust.md)
  The trust management object you use to evaluate trust for the current webpage.
- [var hasOnlySecureContent: Bool](webpage/hasonlysecurecontent.md)
  Indicates whether the webpage loaded all resources on the page through securely encrypted connections.
- [var themeColor: Color?](webpage/themecolor.md)
  The theme color that the system gets from the first valid meta tag in the webpage.
- [var isBlockedByScreenTime: Bool](webpage/isblockedbyscreentime.md)
  Indicates whether Screen Time blocking has occurred.
- [var isInspectable: Bool](webpage/isinspectable.md)
  Indicates whether you can inspect the view with Safari Web Inspector.
- [var isWritingToolsActive: Bool](webpage/iswritingtoolsactive.md)
  Indicates whether Writing Tools is active for the view.
### Interacting with media
- [WebPage.FullscreenState](webpage/fullscreenstate-swift.enum.md)
  The set of possible fullscreen states a webpage may be in.
- [func pauseAllMediaPlayback() async](webpage/pauseallmediaplayback.md)
  Pauses playback of all media in the web view.
- [func mediaPlaybackState() async -> WKMediaPlaybackState](webpage/mediaplaybackstate.md)
  Determine the playback status of media in the page.
- [func setAllMediaPlaybackSuspended(Bool) async](webpage/setallmediaplaybacksuspended(_:).md)
  Changes whether the webpage is suspending playback of all media in the page.
- [func closeAllMediaPresentations() async](webpage/closeallmediapresentations.md)
  Closes all media the webpage is presenting, including picture-in-picture video and fullscreen video.
- [var fullscreenState: WebPage.FullscreenState](webpage/fullscreenstate-swift.property.md)
  The fullscreen state the page is currently in.
### Managing the microphone and camera
- [var cameraCaptureState: WKMediaCaptureState](webpage/cameracapturestate.md)
  Indicates whether the webpage is using the camera to capture images or video.
- [var microphoneCaptureState: WKMediaCaptureState](webpage/microphonecapturestate.md)
  Indicates whether the webpage is using the microphone to capture audio.
- [func setCameraCaptureState(WKMediaCaptureState) async](webpage/setcameracapturestate(_:).md)
  Changes whether the webpage is using the camera to capture images or video.
- [func setMicrophoneCaptureState(WKMediaCaptureState) async](webpage/setmicrophonecapturestate(_:).md)
  Changes whether the webpage is using the microphone to capture audio.
### Executing JavaScript
- [func callJavaScript(String, arguments: [String : Any], in: WebPage.FrameInfo?, contentWorld: WKContentWorld?) async throws -> sending Any?](webpage/calljavascript(_:arguments:in:contentworld:).md)
  Executes the specified string as an async JavaScript function.
### Customizing JavaScript dialogs
- [protocol DialogPresenting](webpage/dialogpresenting.md)
  Allows providing custom behavior to handle JavaScript actions and provide a response.
- [WebPage.FileInputPromptResult](webpage/fileinputpromptresult.md)
  The result of handling a JavaScript open invocation.
- [WebPage.JavaScriptConfirmResult](webpage/javascriptconfirmresult.md)
  The result of handling a JavaScript confirm invocation.
- [WebPage.JavaScriptPromptResult](webpage/javascriptpromptresult.md)
  The result of handling a JavaScript confirm invocation.
### Capturing webpage content
- [func snapshot(WKSnapshotConfiguration) async throws -> Image?](webpage/snapshot(_:).md)
  Generates an image from the web view’s contents.
- [func pdf(configuration: WKPDFConfiguration) async throws -> Data](webpage/pdf(configuration:).md)
  Generates PDF data from the webpage’s contents
- [func webArchiveData() async throws -> Data](webpage/webarchivedata.md)
  Creates a web archive of the webpage’s current contents.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct WebView](webview-swift.struct.md)
  A view that displays some web content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage)*