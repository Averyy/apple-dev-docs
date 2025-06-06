# WKWebView

**Framework**: Webkit  
**Kind**: class

An object that displays interactive web content, such as for an in-app browser.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class WKWebView
```

## Mentions

- [Replacing UIWebView in your app](replacing-uiwebview-in-your-app.md)

#### Overview

A [`WKWebView`](wkwebview.md) object is a platform-native view that you use to incorporate web content seamlessly into your app’s UI. A web view supports a full web-browsing experience, and presents HTML, CSS, and JavaScript content alongside your app’s native views. Use it when web technologies satisfy your app’s layout and styling requirements more readily than native views. For example, you might use it when your app’s content changes frequently.

A web view offers control over the navigation and user experience through delegate objects. Use the navigation delegate to react when the user clicks links in your web content, or interacts with the content in a way that affects navigation. For example, you might prevent the user from navigating to new content unless specific conditions are met. Use the UI delegate to present native UI elements, such as alerts or contextual menus, in response to interactions with your web content.

> **Note**:  [`WKWebView`](wkwebview.md) replaces the [`UIWebView`](https://developer.apple.com/documentation/UIKit/UIWebView) class in iOS 8 and later, and it replaces the [`WebView`](webview.md) class in macOS 10.10 and later.

Embed a [`WKWebView`](wkwebview.md) object programmatically into your view hierarchy, or add it using Interface Builder. Interface Builder supports many customizations, such as configuring data detectors, media playback, and interaction behaviors. For more extensive customizations, create your web view programmatically using a [`WKWebViewConfiguration`](wkwebviewconfiguration.md) object. For example, use a web view configuration object to specify handlers for custom URL schemes, manage cookies, and customize preferences for your web content.

Before your web view appears onscreen, load content from a web server using a [`URLRequest`](https://developer.apple.com/documentation/Foundation/URLRequest) structure or load content directly from a local file or HTML string. The web view automatically loads embedded resources such as images or videos as part of the initial load request. It then renders your content and displays the results inside the view’s bounds rectangle. The following code example shows a view controller that replaces its default view with a custom [`WKWebView`](wkwebview.md) object.

```swift
import UIKit
import WebKit

class ViewController: UIViewController, WKUIDelegate {
    
    var webView: WKWebView!
    
    override func loadView() {
        let webConfiguration = WKWebViewConfiguration()
        webView = WKWebView(frame: .zero, configuration: webConfiguration)
        webView.uiDelegate = self
        view = webView
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        
        let myURL = URL(string:"https://www.apple.com")
        let myRequest = URLRequest(url: myURL!)
        webView.load(myRequest)
    }
}
```

A web view automatically converts telephone numbers that appear in web content to Phone links. When the user taps a Phone link, the Phone app launches and dials the number. Use the [`WKWebViewConfiguration`](wkwebviewconfiguration.md) object to change the default data detector behavior.

You can also use [`setMagnification(_:centeredAt:)`](wkwebview/setmagnification(_:centeredat:).md) to programmatically set the scale of web content the first time it appears in a web view. Thereafter, the user can change the scale using gestures.

##### Manage the Navigation Through Your Web Content

[`WKWebView`](wkwebview.md) provides a complete browsing experience, including the ability to navigate between different webpages using links, forward and back buttons, and more. When the user clicks a link in your content, the web view acts like a browser and displays the content at that link. To disallow navigation, or to customize your web view’s navigation behavior, provide your web view with a navigation delegate — an object that conforms to the [`WKNavigationDelegate`](wknavigationdelegate.md) protocol. Use your navigation delegate to modify the web view’s navigation behavior, or to track the loading progress of new content.

You can also use the methods of [`WKWebView`](wkwebview.md) to navigate programmatically through your content, or to trigger navigation from other parts of your app’s interface. For example, if your UI includes forward and back buttons, connect those buttons to the [`goBack(_:)`](wkwebview/goback(_:).md) and [`goForward(_:)`](wkwebview/goforward(_:).md) methods of your web view to trigger the corresponding web navigation. Use the [`canGoBack`](wkwebview/cangoback.md) and [`canGoForward`](wkwebview/cangoforward.md) properties to determine when to enable or disable your buttons.

##### Provide Sharing Options

People may want to share the contents of your web view with an app or other people. Use a [`UIActivityViewController`](https://developer.apple.com/documentation/UIKit/UIActivityViewController) to present a share sheet offering all the ways people can share the web content.

If your app has the [`com.apple.developer.web-browser`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.web-browser) entitlement, the iOS share sheet can offer Add to Home Screen for an `http` or `https` webpage, creating a convenient link to a web app or bookmark. To allow someone to add the current webpage to the Home Screen, include the [`WKWebView`](wkwebview.md) instance in the `activityItems` array when you call [`init(activityItems:applicationActivities:)`](https://developer.apple.com/documentation/UIKit/UIActivityViewController/init(activityItems:applicationActivities:)) to create the [`UIActivityViewController`](https://developer.apple.com/documentation/UIKit/UIActivityViewController). For more information about building a browser app, see [`Preparing your app to be the default web browser`](https://developer.apple.com/documentation/Xcode/preparing-your-app-to-be-the-default-browser).

## Topics

### Creating a web view
- [init(frame: CGRect, configuration: WKWebViewConfiguration)](wkwebview/init(frame:configuration:).md)
  Creates a web view and initializes it with the specified frame and configuration data.
- [init?(coder: NSCoder)](wkwebview/init(coder:).md)
  Returns an object initialized from data in the specified coder object.
- [var configuration: WKWebViewConfiguration](wkwebview/configuration.md)
  The object that contains the configuration details for the web view.
### Determining whether WebKit can load content
- [class func handlesURLScheme(String) -> Bool](wkwebview/handlesurlscheme(_:).md)
  Returns a Boolean value that indicates whether WebKit natively supports resources with the specified URL scheme.
### Displaying native user interface elements
- [var uiDelegate: (any WKUIDelegate)?](wkwebview/uidelegate.md)
  The object you use to integrate custom user interface elements, such as contextual menus or panels, into web view interactions.
- [protocol WKUIDelegate](wkuidelegate.md)
  The methods for presenting native user interface elements on behalf of a webpage.
### Managing navigation between webpages
- [var navigationDelegate: (any WKNavigationDelegate)?](wkwebview/navigationdelegate.md)
  The object you use to manage navigation behavior for the web view.
- [protocol WKNavigationDelegate](wknavigationdelegate.md)
  Methods for accepting or rejecting navigation changes, and for tracking the progress of navigation requests.
### Loading web content
- [func load(URLRequest) -> WKNavigation?](wkwebview/load(_:).md)
  Loads the web content that the specified URL request object references and navigates to that content.
- [func load(Data, mimeType: String, characterEncodingName: String, baseURL: URL) -> WKNavigation?](wkwebview/load(_:mimetype:characterencodingname:baseurl:).md)
  Loads the content of the specified data object and navigates to it.
- [func loadHTMLString(String, baseURL: URL?) -> WKNavigation?](wkwebview/loadhtmlstring(_:baseurl:).md)
  Loads the contents of the specified HTML string and navigates to it.
- [func loadFileRequest(URLRequest, allowingReadAccessTo: URL) -> WKNavigation](wkwebview/loadfilerequest(_:allowingreadaccessto:).md)
  Loads the web content from the file the URL request object specifies and navigates to that content.
- [func loadFileURL(URL, allowingReadAccessTo: URL) -> WKNavigation?](wkwebview/loadfileurl(_:allowingreadaccessto:).md)
  Loads the web content from the specified file and navigates to it.
- [func loadSimulatedRequest(URLRequest, response: URLResponse, responseData: Data) -> WKNavigation](wkwebview/loadsimulatedrequest(_:response:responsedata:).md)
  Loads the web content from the data you provide as if the data were the response to the request.
- [func loadSimulatedRequest(URLRequest, responseHTML: String) -> WKNavigation](wkwebview/loadsimulatedrequest(_:responsehtml:).md)
  Loads the web content from the HTML you provide as if the HTML were the response to the request.
- [var isLoading: Bool](wkwebview/isloading.md)
  A Boolean value that indicates whether the view is currently loading content.
- [var estimatedProgress: Double](wkwebview/estimatedprogress.md)
  An estimate of what fraction of the current navigation has been loaded.
### Managing the loading process
- [func reload() -> WKNavigation?](wkwebview/reload.md)
  Reloads the current webpage.
- [func reload(Any?)](wkwebview/reload(_:).md)
  Reloads the current webpage.
- [func reloadFromOrigin() -> WKNavigation?](wkwebview/reloadfromorigin.md)
  Reloads the current webpage, and performs end-to-end revalidation of the content using cache-validating conditionals, if possible.
- [func reloadFromOrigin(Any?)](wkwebview/reloadfromorigin(_:).md)
  Reloads the current webpage, and performs end-to-end revalidation of the content using cache-validating conditionals, if possible.
- [func stopLoading()](wkwebview/stoploading.md)
  Stops loading all resources on the current page.
- [func stopLoading(Any?)](wkwebview/stoploading(_:).md)
  Stops loading all resources on the current page.
### Managing downloads
- [func startDownload(using: URLRequest, completionHandler: (WKDownload) -> Void)](wkwebview/startdownload(using:completionhandler:).md)
  Starts to download the resource at the URL in the request.
- [func resumeDownload(fromResumeData: Data, completionHandler: (WKDownload) -> Void)](wkwebview/resumedownload(fromresumedata:completionhandler:).md)
  Resumes a failed or canceled download.
### Making web content inspectable
- [var isInspectable: Bool](wkwebview/isinspectable.md)
  A Boolean value that indicates whether you can inspect the view with Safari Web Inspector.
### Inspecting the view information
- [var scrollView: UIScrollView](wkwebview/scrollview.md)
  The scroll view associated with the web view.
- [var title: String?](wkwebview/title.md)
  The page title.
- [var url: URL?](wkwebview/url.md)
  The URL for the current webpage.
- [var mediaType: String?](wkwebview/mediatype.md)
  The media type for the contents of the web view.
- [var customUserAgent: String?](wkwebview/customuseragent.md)
  The custom user agent string.
- [var serverTrust: SecTrust?](wkwebview/servertrust.md)
  The trust management object you use to evaluate trust for the current webpage.
- [var hasOnlySecureContent: Bool](wkwebview/hasonlysecurecontent.md)
  A Boolean value that indicates whether the web view loaded all resources on the page through securely encrypted connections.
- [var themeColor: UIColor?](wkwebview/themecolor.md)
  The theme color that the system gets from the first valid meta tag in the webpage.
- [var underPageBackgroundColor: UIColor!](wkwebview/underpagebackgroundcolor.md)
  The color the web view displays behind the active page, visible when the user scrolls beyond the bounds of the page.
### Scaling content
- [var pageZoom: CGFloat](wkwebview/pagezoom.md)
  The scale factor by which the web view scales content relative to its bounds.
- [var allowsMagnification: Bool](wkwebview/allowsmagnification.md)
  A Boolean value that indicates whether magnify gestures change the web view’s magnification.
- [var magnification: CGFloat](wkwebview/magnification.md)
  The factor by which the page content is currently scaled.
- [func setMagnification(CGFloat, centeredAt: CGPoint)](wkwebview/setmagnification(_:centeredat:).md)
  Scales the page content and centers the result on the specified point.
### Interacting with media
- [func pauseAllMediaPlayback(completionHandler: (() -> Void)?)](wkwebview/pauseallmediaplayback(completionhandler:).md)
  Pauses playback of all media in the web view.
- [func requestMediaPlaybackState(completionHandler: (WKMediaPlaybackState) -> Void)](wkwebview/requestmediaplaybackstate(completionhandler:).md)
  Requests the playback status of media in the web view.
- [func setAllMediaPlaybackSuspended(Bool, completionHandler: (() -> Void)?)](wkwebview/setallmediaplaybacksuspended(_:completionhandler:).md)
  Changes whether the webpage is suspending playback of all media in the page.
- [func closeAllMediaPresentations(completionHandler: (() -> Void)?)](wkwebview/closeallmediapresentations(completionhandler:).md)
  Closes all media the web view is presenting, including picture-in-picture video and fullscreen video.
- [enum WKMediaPlaybackState](wkmediaplaybackstate.md)
  An enumeration that describes whether an audio or video presentation is playing, paused, or suspended.
### Managing the microphone and camera
- [var cameraCaptureState: WKMediaCaptureState](wkwebview/cameracapturestate.md)
  An enumeration case that indicates whether the webpage is using the camera to capture images or video.
- [var microphoneCaptureState: WKMediaCaptureState](wkwebview/microphonecapturestate.md)
  An enumeration case that indicates whether the webpage is using the microphone to capture audio.
- [func setCameraCaptureState(WKMediaCaptureState, completionHandler: (() -> Void)?)](wkwebview/setcameracapturestate(_:completionhandler:).md)
  Changes whether the webpage is using the camera to capture images or video.
- [func setMicrophoneCaptureState(WKMediaCaptureState, completionHandler: (() -> Void)?)](wkwebview/setmicrophonecapturestate(_:completionhandler:).md)
  Changes whether the webpage is using the microphone to capture audio.
- [enum WKMediaCaptureState](wkmediacapturestate.md)
  An enumeration that describes whether a media device, like a camera or microphone, is currently capturing audio or video.
### Searching the current page’s content
- [func find(String, configuration: WKFindConfiguration, completionHandler: (WKFindResult) -> Void)](wkwebview/find(_:configuration:completionhandler:).md)
  Searches for the specified string in the web view’s content.
- [func find(String, configuration: WKFindConfiguration) async throws -> WKFindResult](wkwebview/find(_:configuration:).md)
  Searches for the specified string in the web view’s content.
- [class WKFindConfiguration](wkfindconfiguration.md)
  The configuration parameters to use when searching the contents of the web view.
- [class WKFindResult](wkfindresult.md)
  An object that contains the results of searching the web view’s contents.
### Navigating between webpages
- [var allowsBackForwardNavigationGestures: Bool](wkwebview/allowsbackforwardnavigationgestures.md)
  A Boolean value that indicates whether horizontal swipe gestures trigger backward and forward page navigation.
- [var backForwardList: WKBackForwardList](wkwebview/backforwardlist.md)
  The web view’s back-forward list.
- [func goBack(Any?)](wkwebview/goback(_:).md)
  Navigates to the back item in the back-forward list.
- [func goBack() -> WKNavigation?](wkwebview/goback.md)
  Navigates to the back item in the back-forward list.
- [func goForward(Any?)](wkwebview/goforward(_:).md)
  Navigates to the forward item in the back-forward list.
- [func goForward() -> WKNavigation?](wkwebview/goforward.md)
  Navigates to the forward item in the back-forward list.
- [func go(to: WKBackForwardListItem) -> WKNavigation?](wkwebview/go(to:).md)
  Navigates to an item from the back-forward list and sets it as the current item.
- [var canGoBack: Bool](wkwebview/cangoback.md)
  A Boolean value that indicates whether there is a valid back item in the back-forward list.
- [var canGoForward: Bool](wkwebview/cangoforward.md)
  A Boolean value that indicates whether there is a valid forward item in the back-forward list.
- [var allowsLinkPreview: Bool](wkwebview/allowslinkpreview.md)
  A Boolean value that determines whether pressing a link displays a preview of the destination for the link.
- [var interactionState: Any?](wkwebview/interactionstate.md)
  An object you use to capture the current state of interaction in a web view so that you can restore that state later to another web view.
### Executing JavaScript
- [func evaluateJavaScript(String, completionHandler: ((Any?, (any Error)?) -> Void)?)](wkwebview/evaluatejavascript(_:completionhandler:).md)
  Evaluates the specified JavaScript string.
- [func evaluateJavaScript(String, in: WKFrameInfo?, in: WKContentWorld, completionHandler: ((Result<Any, any Error>) -> Void)?)](wkwebview/evaluatejavascript(_:in:in:completionhandler:).md)
  Evaluates a JavaScript string in the context of the specified frame and content world.
- [func evaluateJavaScript(String, in: WKFrameInfo?, contentWorld: WKContentWorld) async throws -> Any?](wkwebview/evaluatejavascript(_:in:contentworld:).md)
  Evaluates a JavaScript string in the context of the specified frame and content world.
- [func callAsyncJavaScript(String, arguments: [String : Any], in: WKFrameInfo?, in: WKContentWorld, completionHandler: ((Result<Any, any Error>) -> Void)?)](wkwebview/callasyncjavascript(_:arguments:in:in:completionhandler:).md)
  Executes the specified string as an asynchronous JavaScript function.
- [func callAsyncJavaScript(String, arguments: [String : Any], in: WKFrameInfo?, contentWorld: WKContentWorld) async throws -> Any?](wkwebview/callasyncjavascript(_:arguments:in:contentworld:).md)
  Executes the specified string as an asynchronous JavaScript function.
### Capturing the web view’s content
- [func takeSnapshot(with: WKSnapshotConfiguration?, completionHandler: (UIImage?, (any Error)?) -> Void)](wkwebview/takesnapshot(with:completionhandler:).md)
  Generates a platform-native image from the web view’s contents asynchronously.
- [func createPDF(configuration: WKPDFConfiguration, completionHandler: (Result<Data, any Error>) -> Void)](wkwebview/createpdf(configuration:completionhandler:).md)
  Generates PDF data from the web view’s contents asynchronously.
- [func pdf(configuration: WKPDFConfiguration) async throws -> Data](wkwebview/pdf(configuration:).md)
  Generates PDF data from the web view’s contents asynchronously.
- [func createWebArchiveData(completionHandler: (Result<Data, any Error>) -> Void)](wkwebview/createwebarchivedata(completionhandler:).md)
  Creates a web archive of the web view’s current contents asynchronously.
- [func printOperation(with: NSPrintInfo) -> NSPrintOperation](wkwebview/printoperation(with:).md)
  Returns the print operation object to use when printing the contents of the web view.
- [class WKSnapshotConfiguration](wksnapshotconfiguration.md)
  The configuration data to use when generating an image from a web view’s contents.
- [class WKPDFConfiguration](wkpdfconfiguration.md)
  The configuration data to use when generating a PDF representation of a web view’s contents.
### Supporting Find and Replace
- [var isFindInteractionEnabled: Bool](wkwebview/isfindinteractionenabled.md)
- [var findInteraction: UIFindInteraction?](wkwebview/findinteraction.md)
### Handling full-screen transitions
- [var fullscreenState: WKWebView.FullscreenState](wkwebview/fullscreenstate-swift.property.md)
- [WKWebView.FullscreenState](wkwebview/fullscreenstate-swift.enum.md)
### Configuring viewport insets
- [func setMinimumViewportInset(UIEdgeInsets, maximumViewportInset: UIEdgeInsets)](wkwebview/setminimumviewportinset(_:maximumviewportinset:).md)
- [var minimumViewportInset: UIEdgeInsets](wkwebview/minimumviewportinset.md)
- [var maximumViewportInset: UIEdgeInsets](wkwebview/maximumviewportinset.md)
### Deprecated
- [Deprecated symbols](wkwebview-deprecated-symbols.md)
  Review unsupported symbols and their replacements.
### Instance Properties
- [var isWritingToolsActive: Bool](wkwebview/iswritingtoolsactive.md)

## Relationships

### Inherits From
- [NSView](../AppKit/NSView.md)
- [UIView](../UIKit/UIView.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/NSAccessibilityElementProtocol.md)
- [NSAccessibilityProtocol](../AppKit/NSAccessibilityProtocol.md)
- [NSAnimatablePropertyContainer](../AppKit/NSAnimatablePropertyContainer.md)
- [NSAppearanceCustomization](../AppKit/NSAppearanceCustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](../AppKit/NSDraggingDestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTextFinderClient](../AppKit/NSTextFinderClient.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [NSUserInterfaceValidations](../AppKit/NSUserInterfaceValidations.md)
- [UIAccessibilityIdentification](../UIKit/UIAccessibilityIdentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearance](../UIKit/UIAppearance.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIDynamicItem](../UIKit/UIDynamicItem.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UILargeContentViewerItem](../UIKit/UILargeContentViewerItem.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/UIPopoverPresentationControllerSourceItem.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [Replacing UIWebView in your app](replacing-uiwebview-in-your-app.md)
  Find a suitable alternative to handle your app’s web content.
- [Viewing Desktop or Mobile Web Content Using a Web View](viewing-desktop-or-mobile-web-content-using-a-web-view.md)
  Implement a simple iPad web browser that can view either the desktop or mobile version of a website.
- [protocol WKUIDelegate](wkuidelegate.md)
  The methods for presenting native user interface elements on behalf of a webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/WebKit/wkwebview)*