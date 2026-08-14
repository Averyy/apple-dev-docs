# WebKit for AppKit and UIKit

**Framework**: WebKit

Display web content in AppKit or UIKit apps, or apps built with Objective-C.

#### Overview

Present a [`WKWebView`](wkwebview.md) object from your custom view hierarchies and load the content you want to display. Use supporting objects to manage cookies, evaluate scripts, control navigation, generate snapshots, and perform text-based searches.

> ❗ **Important**:  Always call WebKit functions and methods from your app’s main thread or main dispatch queue.

## Topics

### Web views
- [Replacing UIWebView in your app](replacing-uiwebview-in-your-app.md)
  Find a suitable alternative to handle your app’s web content.
- [Viewing Desktop or Mobile Web Content Using a Web View](viewing-desktop-or-mobile-web-content-using-a-web-view.md)
  Implement a simple iPad web browser that can view either the desktop or mobile version of a website.
- [class WKWebView](wkwebview.md)
  An object that displays interactive web content, such as for an in-app browser.
- [protocol WKUIDelegate](wkuidelegate.md)
  The methods for presenting native user interface elements on behalf of a webpage.
### Web view configuration
- [class WKWebViewConfiguration](wkwebviewconfiguration.md)
  A collection of properties that you use to initialize a web view.
- [class WKWindowFeatures](wkwindowfeatures.md)
  Display-related attributes that a webpage requests for its window.
- [class WKProcessPool](wkprocesspool.md)
  An opaque token that you use to run multiple web views in a single process.
- [class WKPreferences](wkpreferences.md)
  An object that encapsulates the standard behaviors to apply to websites.
- [class WKWebpagePreferences](wkwebpagepreferences.md)
  An object that specifies the behaviors to use when loading and rendering page content.
- [WKWebpagePreferences.ContentMode](wkwebpagepreferences/contentmode.md)
  Constants that indicate how to render web view content.
- [WKWebpagePreferences.UpgradeToHTTPSPolicy](wkwebpagepreferences/upgradetohttpspolicy.md)
- [enum WKSecurityRestrictionMode](wksecurityrestrictionmode.md)
- [WKPreferences.InactiveSchedulingPolicy](wkpreferences/inactiveschedulingpolicy-swift.enum.md)
  An enumeration that lists policies for how a web view that’s not in a window handles tasks.
- [WKWebView.FullscreenState](wkwebview/fullscreenstate-swift.enum.md)
### Web data management
- [class WKWebsiteDataStore](wkwebsitedatastore.md)
  An object that manages cookies, disk and memory caches, and other types of data for a web view.
- [class WKWebsiteDataRecord](wkwebsitedatarecord.md)
  A record of the data that a particular website stores persistently.
- [class WKHTTPCookieStore](wkhttpcookiestore.md)
  An object that manages the HTTP cookies associated with a particular web view.
- [protocol WKURLSchemeHandler](wkurlschemehandler.md)
  A protocol for loading resources with URL schemes that WebKit doesn’t handle.
- [protocol WKURLSchemeTask](wkurlschemetask.md)
  An interface that WebKit uses to request custom resources from your app.
- [static let readAccessURL: NSAttributedString.DocumentReadingOptionKey](../foundation/nsattributedstring/documentreadingoptionkey/readaccessurl.md)
  The local files WebKit can access when loading content.
### Navigation
- [protocol WKNavigationDelegate](wknavigationdelegate.md)
  Methods for accepting or rejecting navigation changes, and for tracking the progress of navigation requests.
- [class WKBackForwardList](wkbackforwardlist.md)
  An object that manages the list of previously loaded webpages, which the web view uses for forward and backward navigation.
- [class WKBackForwardListItem](wkbackforwardlistitem.md)
  A representation of a webpage that the web view previously visited.
- [class WKNavigation](wknavigation.md)
  An object that tracks the loading progress of a webpage.
- [class WKNavigationAction](wknavigationaction.md)
  An object that contains information about an action that causes navigation to occur.
- [class WKNavigationResponse](wknavigationresponse.md)
  An object that contains the response to a navigation request, and which you use to make navigation-related policy decisions.
- [class WKFormInfo](wkforminfo.md)
### Downloads
- [class WKDownload](wkdownload.md)
  An object that represents the download of a web resource.
- [protocol WKDownloadDelegate](wkdownloaddelegate.md)
  A protocol you implement to track download progress and handle redirects, authentication challenges, and failures.
- [WKDownload.PlaceholderPolicy](wkdownload/placeholderpolicy.md)
### Page content
- [class WKUserContentController](wkusercontentcontroller.md)
  An object for managing interactions between JavaScript code and your web view, and for filtering content in your web view.
- [class WKContentRuleListStore](wkcontentruleliststore.md)
  An object that contains the rules for how to load and filter content in the web view.
- [class WKContentWorld](wkcontentworld.md)
  An object that defines a scope of execution for JavaScript code, and which you use to prevent conflicts between different scripts.
- [class WKFrameInfo](wkframeinfo.md)
  An object that contains information about a frame on a webpage.
- [class WKSecurityOrigin](wksecurityorigin.md)
  An object that identifies the origin of a particular resource.
- [class WKUserScript](wkuserscript.md)
  A script that the web view injects into a webpage.
- [WKContentWorld.Configuration](wkcontentworld/configuration.md)
- [class WKJSHandle](wkjshandle.md)
  A WKJSHandle object contains a reference to a JavaScript object.
### Page-level search
- [class WKFindConfiguration](wkfindconfiguration.md)
  The configuration parameters to use when searching the contents of the web view.
- [class WKFindResult](wkfindresult.md)
  An object that contains the results of searching the web view’s contents.
### Contextual menus
- [class WKContextMenuElementInfo](wkcontextmenuelementinfo.md)
  An object that contains information about a link the user clicked in a webpage, and which you use to configure a context menu for that link.
### Snapshots
- [class WKSnapshotConfiguration](wksnapshotconfiguration.md)
  The configuration data to use when generating an image from a web view’s contents.
- [class WKPDFConfiguration](wkpdfconfiguration.md)
  The configuration data to use when generating a PDF representation of a web view’s contents.
### Web extensions
- [class WKWebExtension](wkwebextension.md)
  An object that encapsulates a web extension’s resources that the manifest file defines.
- [protocol WKWebExtensionTab](wkwebextensiontab.md)
  A protocol with methods that represent a tab to web extensions.
- [protocol WKWebExtensionWindow](wkwebextensionwindow.md)
  A protocol with methods that represent a window to web extensions.
- [class WKWebExtensionContext](wkwebextensioncontext.md)
  An object that represents the runtime environment for a web extension.
- [class WKWebExtensionController](wkwebextensioncontroller.md)
  An object that manages a set of loaded extension contexts.
- [protocol WKWebExtensionControllerDelegate](wkwebextensioncontrollerdelegate.md)
  A group of methods you use to customize web extension interactions.
- [WKWebExtension.Action](wkwebextension/action.md)
  An object that encapsulates the properties for an individual web extension action.
- [WKWebExtension.Command](wkwebextension/command.md)
  An object that encapsulates the properties for an individual web extension command.
- [WKWebExtension.MatchPattern](wkwebextension/matchpattern.md)
  An object that represents a way to specify groups of URLs.
- [WKWebExtension.MessagePort](wkwebextension/messageport.md)
  An object that manages message-based communication with a web extension.
- [WKWebExtension.DataRecord](wkwebextension/datarecord.md)
  An object that represents a record of stored data for a specific web extension context.
- [WKWebExtension.TabConfiguration](wkwebextension/tabconfiguration.md)
  An object that encapsulates configuration options for a tab in an extension.
- [WKWebExtension.WindowConfiguration](wkwebextension/windowconfiguration.md)
  An object that encapsulates configuration options for a window in an extension.
- [WKWebExtensionController.Configuration](wkwebextensioncontroller/configuration-swift.class.md)
  A [`WKWebExtensionController.Configuration`](wkwebextensioncontroller/configuration-swift.class.md) object with which to initialize a web extension controller.
### Errors
- [WKError.Code](wkerror/code.md)
  Possible error values that WebKit APIs can return.
- [struct WKError](wkerror.md)
  Possible error values that WebKit APIs can return.
### Immersive environments
- [class WKImmersiveEnvironment](wkimmersiveenvironment.md)
- [protocol WKImmersiveEnvironmentDelegate](wkimmersiveenvironmentdelegate.md)
- [var allowsImmersiveEnvironments: Bool](wkwebviewconfiguration/allowsimmersiveenvironments.md)
- [var immersiveEnvironmentDelegate: (any WKImmersiveEnvironmentDelegate)?](wkwebview/immersiveenvironmentdelegate.md)
- [func dismissImmersiveEnvironment(completionHandler: () -> Void)](wkwebview/dismissimmersiveenvironment(completionhandler:).md)
### Deprecated
- [Deprecated Symbols](deprecated-symbols.md)
  Review unsupported symbols and their replacements.
### Web extension errors
- [WKWebExtension.Error.Code](wkwebextension/error/code.md)
  Constants that indicate errors in the [`WKWebExtension`](wkwebextension.md) domain.
- [WKWebExtensionContext.Error.Code](wkwebextensioncontext/error/code.md)
  Constants that indicate errors in the [`WKWebExtensionContext`](wkwebextensioncontext.md) domain.
- [WKWebExtension.DataRecord.Error.Code](wkwebextension/datarecord/error/code.md)
  Constants that indicate errors in the [`WKWebExtension.DataRecord`](wkwebextension/datarecord.md) domain.
- [WKWebExtension.DataRecord.Error](wkwebextension/datarecord/error.md)
  Constants that indicate errors in the [`WKWebExtension.DataRecord`](wkwebextension/datarecord.md) domain.
- [WKWebExtension.MatchPattern.Error.Code](wkwebextension/matchpattern/error/code.md)
  Constants that indicate errors in the [`WKWebExtension.MatchPattern`](wkwebextension/matchpattern.md) domain.
- [WKWebExtension.MessagePort.Error.Code](wkwebextension/messageport/error/code.md)
  Constants that indicate errors in the [`WKWebExtension.MessagePort`](wkwebextension/messageport.md) domain.
- [WKWebExtension.MessagePort.Error](wkwebextension/messageport/error.md)
  Constants that indicate errors in the [`WKWebExtension.MessagePort`](wkwebextension/messageport.md) domain.

## See Also

- [WebKit for SwiftUI](webkit-for-swiftui.md)
  Integrate web content into your SwiftUI apps with new standard views you connect to webpages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webkit-for-appkit-and-uikit)*