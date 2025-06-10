# UIWebView

**Framework**: UIKit  
**Kind**: class

A view that embeds web content in your app.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+

## Declaration

```swift
@MainActor
class UIWebView
```

#### Overview

> **Note**:  In apps that run in iOS 8 and later, use the [`WKWebView`](https://developer.apple.com/documentation/WebKit/WKWebView) class instead of using [`UIWebView`](uiwebview.md). Additionally, consider setting the [`WKPreferences`](https://developer.apple.com/documentation/WebKit/WKPreferences) property [`javaScriptEnabled`](https://developer.apple.com/documentation/WebKit/WKPreferences/javaScriptEnabled) to [`false`](https://developer.apple.com/documentation/swift/false) if you render files that aren’t supposed to run JavaScript.

> ❗ **Important**:  An iOS app linked on or after iOS 10.0 must include in its `Info.plist` file the usage description keys for the types of data it needs to access or it will crash. To access a user’s photo data specifically, it must include [`NSPhotoLibraryUsageDescription`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW17) and [`NSCameraUsageDescription`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW24).

Use the [`loadHTMLString(_:baseURL:)`](uiwebview/loadhtmlstring(_:baseurl:).md) method to begin loading local HTML files or the [`loadRequest(_:)`](uiwebview/loadrequest(_:).md) method to begin loading web content. Use the [`stopLoading()`](uiwebview/stoploading().md) method to stop loading, and the [`isLoading`](uiwebview/isloading.md) property to find out if a web view is in the process of loading.

If you allow the user to move back and forward through the webpage history, then you can use the [`goBack()`](uiwebview/goback().md) and [`goForward()`](uiwebview/goforward().md) methods as actions for buttons. Use the [`canGoBack`](uiwebview/cangoback.md) and [`canGoForward`](uiwebview/cangoforward.md) properties to disable the buttons when the user can’t move in a direction.

By default, a web view automatically converts telephone numbers that appear in web content to Phone links. When a Phone link is tapped, the Phone app launches and dials the number. To turn off this default behavior, set the [`dataDetectorTypes`](uiwebview/datadetectortypes.md) property with a [`UIDataDetectorTypes`](uidatadetectortypes.md) bitfield that doesn’t contain the [`phoneNumber`](uidatadetectortypes/phonenumber.md) flag.

You can also use the [`scalesPageToFit`](uiwebview/scalespagetofit.md) property to programmatically set the scale of web content the first time it’s displayed in a web view. Thereafter, the user can change the scale using gestures.

Set the [`delegate`](uiwebview/delegate.md) property to an object conforming to the [`UIWebViewDelegate`](uiwebviewdelegate.md) protocol if you want to track the loading of web content.

> ❗ **Important**:  You shouldn’t embed [`UIWebView`](uiwebview.md) or [`UITableView`](uitableview.md) objects in [`UIScrollView`](uiscrollview.md) objects. If you do so, unexpected behavior can result because touch events for the two objects can be mixed up and wrongly handled.

You can debug the HTML, CSS, and JavaScript contained inside a [`UIWebView`](uiwebview.md) with Web Inspector. Read Debugging Web Content on iOS to learn how to configure Web Inspector for iOS. Read the rest of [`Safari Web Content Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/Introduction/Introduction.html#//apple_ref/doc/uid/TP40002051) to learn how to create web content that’s optimized for Safari on iPhone and iPad.

For information about basic view behaviors, see [`View Programming Guide for iOS`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/ViewPG_iPhoneOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009503).

##### Supported File Formats

In addition to HTML content, [`UIWebView`](uiwebview.md) objects can be used to display other content types, such as Keynote, PDF, and Pages documents. For the best rendering of plain and rich text in your app, however, you should use [`UITextView`](uitextview.md) instead.

##### State Preservation

In iOS 6 and later, if you assign a value to this view’s [`restorationIdentifier`](uiviewcontroller/restorationidentifier.md) property, it attempts to preserve its URL history, the scaling and scrolling positions for each page, and information about which page is currently being viewed. During restoration, the view restores these values so that the web content appears just as it did before. For more information about how state preservation and restoration works, see [`App Programming Guide for iOS`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007072).

##### Subclassing Notes

The [`UIWebView`](uiwebview.md) class shouldn’t be subclassed.

## Topics

### Essentials
- [Replacing UIWebView in your app](../WebKit/replacing-uiwebview-in-your-app.md)
  Find a suitable alternative to handle your app’s web content.
### Responding to web view changes
- [var delegate: (any UIWebViewDelegate)?](uiwebview/delegate.md)
  The receiver’s delegate.
- [protocol UIWebViewDelegate](uiwebviewdelegate.md)
  The `UIWebViewDelegate` protocol defines methods that a delegate of a [`UIWebView`](uiwebview.md) object can optionally implement to intervene when web content is loaded.
### Loading content
- [func load(Data, mimeType: String, textEncodingName: String, baseURL: URL)](uiwebview/load(_:mimetype:textencodingname:baseurl:).md)
  Sets the main page contents, MIME type, content encoding, and base URL.
- [func loadHTMLString(String, baseURL: URL?)](uiwebview/loadhtmlstring(_:baseurl:).md)
  Sets the main page content and base URL.
- [func loadRequest(URLRequest)](uiwebview/loadrequest(_:).md)
  Connects to a given URL by initiating an asynchronous client request.
- [var request: URLRequest?](uiwebview/request.md)
  The URL request identifying the location of the content to load.
- [var isLoading: Bool](uiwebview/isloading.md)
  A Boolean value indicating whether the receiver is done loading content.
- [func stopLoading()](uiwebview/stoploading.md)
  Stops the loading of any web content managed by the receiver.
- [func reload()](uiwebview/reload.md)
  Reloads the current page.
### Moving back and forward
- [var canGoBack: Bool](uiwebview/cangoback.md)
  A Boolean value indicating whether the receiver can move backward.
- [var canGoForward: Bool](uiwebview/cangoforward.md)
  A Boolean value indicating whether the receiver can move forward.
- [func goBack()](uiwebview/goback.md)
  Loads the previous location in the back-forward list.
- [func goForward()](uiwebview/goforward.md)
  Loads the next location in the back-forward list.
### Setting web content properties
- [var allowsLinkPreview: Bool](uiwebview/allowslinkpreview.md)
  A Boolean value that determines whether pressing on a link displays a preview of the destination for the link.
- [var scalesPageToFit: Bool](uiwebview/scalespagetofit.md)
  A Boolean value determining whether the webpage scales to fit the view and the user can change the scale.
- [var scrollView: UIScrollView](uiwebview/scrollview.md)
  The scroll view associated with the web view.
- [var suppressesIncrementalRendering: Bool](uiwebview/suppressesincrementalrendering.md)
  A Boolean value indicating whether the web view suppresses content rendering until it is fully loaded into memory.
- [var keyboardDisplayRequiresUserAction: Bool](uiwebview/keyboarddisplayrequiresuseraction.md)
  A Boolean value indicating whether web content can programmatically display the keyboard.
- [var dataDetectorTypes: UIDataDetectorTypes](uiwebview/datadetectortypes.md)
  The types of data converted to clickable URLs in the web view’s content.
### Running JavaScript
- [func stringByEvaluatingJavaScript(from: String) -> String?](uiwebview/stringbyevaluatingjavascript(from:).md)
  Returns the result of running a JavaScript script.
### Managing media playback
- [var allowsInlineMediaPlayback: Bool](uiwebview/allowsinlinemediaplayback.md)
  A Boolean value that determines whether HTML5 videos play inline or use the native full-screen controller.
- [var mediaPlaybackRequiresUserAction: Bool](uiwebview/mediaplaybackrequiresuseraction.md)
  A Boolean value that determines whether HTML5 videos can play automatically or require the user to start playing them.
- [var mediaPlaybackAllowsAirPlay: Bool](uiwebview/mediaplaybackallowsairplay.md)
  A Boolean value that determines whether Air Play is allowed from this view.
- [var allowsPictureInPictureMediaPlayback: Bool](uiwebview/allowspictureinpicturemediaplayback.md)
  A Boolean value that determines whether Picture in Picture playback is allowed from this view.
### Managing pages
- [var gapBetweenPages: CGFloat](uiwebview/gapbetweenpages.md)
  The size of the gap, in points, between pages.
- [var pageCount: Int](uiwebview/pagecount.md)
  The number of pages produced by the layout of the web view.
- [var pageLength: CGFloat](uiwebview/pagelength.md)
  The size of each page, in points, in the direction that the pages flow.
- [var paginationBreakingMode: UIWebView.PaginationBreakingMode](uiwebview/paginationbreakingmode-swift.property.md)
  The manner in which column- or page-breaking occurs.
- [var paginationMode: UIWebView.PaginationMode](uiwebview/paginationmode-swift.property.md)
  The layout of content in the web view.
### Constants
- [UIWebView.NavigationType](uiwebview/navigationtype.md)
  Constant indicating the user’s action.
- [UIWebView.PaginationBreakingMode](uiwebview/paginationbreakingmode-swift.enum.md)
  The manner in which column- or page-breaking occurs.
- [UIWebView.PaginationMode](uiwebview/paginationmode-swift.enum.md)
  The layout of content in the web view, which determines the direction that the pages flow.
- [struct UIDataDetectorTypes](uidatadetectortypes.md)
  Constants that define the types of information to detect in text-based content.

## Relationships

### Inherits From
- [UIView](uiview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearance](uiappearance.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UICoordinateSpace](uicoordinatespace.md)
- [UIDynamicItem](uidynamicitem.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIFocusItem](uifocusitem.md)
- [UIFocusItemContainer](uifocusitemcontainer.md)
- [UILargeContentViewerItem](uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UIScrollViewDelegate](uiscrollviewdelegate.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [class UIActivityIndicatorView](uiactivityindicatorview.md)
  A view that shows that a task is in progress.
- [class UICalendarView](uicalendarview.md)
  A view that displays a calendar with date-specific decorations, and provides for user selection of a single date or multiple dates.
- [class UIContentUnavailableView](uicontentunavailableview.md)
  A view that indicates there’s no content to display.
- [class UIImageView](uiimageview.md)
  A view that displays a single image or a sequence of animated images in your interface.
- [class UIPickerView](uipickerview.md)
  A view that uses a spinning-wheel or slot-machine metaphor to show one or more sets of values.
- [class UIProgressView](uiprogressview.md)
  A view that depicts the progress of a task over time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview)*