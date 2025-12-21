# Setting Up a Web View (Legacy)

**Framework**: WebKit

## Topics

### Setting Up a Web View (Legacy)
- [class WebView](webview-swift.class.md)
  `WebView` is the core view class in the WebKit framework that manages interactions between the `WebFrame` and `WebFrameView` classes. To embed web content in your application, you just create a `WebView` object, attach it to a window, and send a [`load(_:)`](webframe/load(_:)-47p2s.md) message to its main frame.
- [class WebPreferences](webpreferences.md)
  WebPreferences encapsulates the preferences you can change per WebView object. These preferences include font, text encoding, and image settings. Normally a WebView object uses the standard preferences returned by the [`standard()`](webpreferences/standard().md) class method. However, you can modify the preferences for individual WebView instances too. Use the [`preferencesIdentifier`](webview-swift.class/preferencesidentifier.md) WebView method to change a WebView object’s preferences, or to share preferences between WebView objects. Use the [`autosaves`](webpreferences/autosaves.md) method to specify if the preferences object should be automatically saved to the user defaults database.
- [protocol WebEditingDelegate](webeditingdelegate.md)
- [protocol WebUIDelegate](webuidelegate.md)
  Web view user interface delegates implement this protocol to control the opening of new windows, augment the behavior of default menu items displayed when the user clicks elements, and perform other user interface–related tasks. These methods can be invoked as a result of handling JavaScript or other plug-in content. Delegates that display more than one web view per window, for example, need to implement some of these methods to handle that case. The default implementation assumes one window per web view, so non-conventional user interfaces might implement a user interface delegate.

## See Also

- [Document Object Models API (Legacy)](document-object-models-api-legacy.md)
- [Accessing Previous Webpages (Legacy)](accessing-previous-webpages-legacy.md)
- [Archiving Webpages (Legacy)](archiving-webpages-legacy.md)
- [Loading Resources (Legacy)](loading-resources-legacy.md)
- [Working with Frames (legacy)](working-with-frames-legacy.md)
- [Downloading Information (Legacy)](downloading-information-legacy.md)
- [Opening a File (Legacy)](opening-a-file-legacy.md)
- [Setting Policies (Legacy)](setting-policies-legacy.md)
- [Implementing Plugins (Legacy)](implementing-plugins-legacy.md)
- [Incorporating Scripts (Legacy)](incorporating-scripts-legacy.md)
- [Working With Document Web Views (Legacy)](working-with-document-web-views-legacy.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/setting-up-a-web-view-legacy)*