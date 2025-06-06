# WKWebExtensionTab

**Framework**: Webkit  
**Kind**: protocol

A protocol with methods that represent a tab to web extensions.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
protocol WKWebExtensionTab : NSObjectProtocol
```

## Topics

### Instance Methods
- [func activate(for: WKWebExtensionContext, completionHandler: ((any Error)?) -> Void)](wkwebextensiontab/activate(for:completionhandler:).md)
  Called to activate the tab, making it frontmost.
- [func close(for: WKWebExtensionContext, completionHandler: ((any Error)?) -> Void)](wkwebextensiontab/close(for:completionhandler:).md)
  Called to close the tab.
- [func detectWebpageLocale(for: WKWebExtensionContext, completionHandler: (Locale?, (any Error)?) -> Void)](wkwebextensiontab/detectwebpagelocale(for:completionhandler:).md)
  Called to detect the locale of the webpage currently loaded in the tab.
- [func duplicate(using: WKWebExtension.TabConfiguration, for: WKWebExtensionContext, completionHandler: ((any WKWebExtensionTab)?, (any Error)?) -> Void)](wkwebextensiontab/duplicate(using:for:completionhandler:).md)
  Called to duplicate the tab.
- [func goBack(for: WKWebExtensionContext, completionHandler: ((any Error)?) -> Void)](wkwebextensiontab/goback(for:completionhandler:).md)
  Called to navigate the tab to the previous page in its history.
- [func goForward(for: WKWebExtensionContext, completionHandler: ((any Error)?) -> Void)](wkwebextensiontab/goforward(for:completionhandler:).md)
  Called to navigate the tab to the next page in its history.
- [func indexInWindow(for: WKWebExtensionContext) -> Int](wkwebextensiontab/indexinwindow(for:).md)
  Called when the index of the tab in the window is needed.
- [func isLoadingComplete(for: WKWebExtensionContext) -> Bool](wkwebextensiontab/isloadingcomplete(for:).md)
  Called to check if the tab has finished loading.
- [func isMuted(for: WKWebExtensionContext) -> Bool](wkwebextensiontab/ismuted(for:).md)
  Called to check if the tab is currently muted.
- [func isPinned(for: WKWebExtensionContext) -> Bool](wkwebextensiontab/ispinned(for:).md)
  Called when the pinned state of the tab is needed.
- [func isPlayingAudio(for: WKWebExtensionContext) -> Bool](wkwebextensiontab/isplayingaudio(for:).md)
  Called to check if the tab is currently playing audio.
- [func isReaderModeActive(for: WKWebExtensionContext) -> Bool](wkwebextensiontab/isreadermodeactive(for:).md)
  Called to check if the tab is currently showing reader mode.
- [func isReaderModeAvailable(for: WKWebExtensionContext) -> Bool](wkwebextensiontab/isreadermodeavailable(for:).md)
  Called to check if reader mode is available for the tab.
- [func isSelected(for: WKWebExtensionContext) -> Bool](wkwebextensiontab/isselected(for:).md)
  Called when the selected state of the tab is needed.
- [func loadURL(URL, for: WKWebExtensionContext, completionHandler: ((any Error)?) -> Void)](wkwebextensiontab/loadurl(_:for:completionhandler:).md)
  Called to load a URL in the tab.
- [func parentTab(for: WKWebExtensionContext) -> (any WKWebExtensionTab)?](wkwebextensiontab/parenttab(for:).md)
  Called when the parent tab for the tab is needed.
- [func pendingURL(for: WKWebExtensionContext) -> URL?](wkwebextensiontab/pendingurl(for:).md)
  Called when the pending URL of the tab is needed.
- [func reload(fromOrigin: Bool, for: WKWebExtensionContext, completionHandler: ((any Error)?) -> Void)](wkwebextensiontab/reload(fromorigin:for:completionhandler:).md)
  Called to reload the current page in the tab.
- [func setMuted(Bool, for: WKWebExtensionContext, completionHandler: ((any Error)?) -> Void)](wkwebextensiontab/setmuted(_:for:completionhandler:).md)
  Called to set the mute state of the tab.
- [func setParentTab((any WKWebExtensionTab)?, for: WKWebExtensionContext, completionHandler: ((any Error)?) -> Void)](wkwebextensiontab/setparenttab(_:for:completionhandler:).md)
  Called to set or clear the parent tab for the tab.
- [func setPinned(Bool, for: WKWebExtensionContext, completionHandler: ((any Error)?) -> Void)](wkwebextensiontab/setpinned(_:for:completionhandler:).md)
  Called to set the pinned state of the tab.
- [func setReaderModeActive(Bool, for: WKWebExtensionContext, completionHandler: ((any Error)?) -> Void)](wkwebextensiontab/setreadermodeactive(_:for:completionhandler:).md)
  Called to set the reader mode for the tab.
- [func setSelected(Bool, for: WKWebExtensionContext, completionHandler: ((any Error)?) -> Void)](wkwebextensiontab/setselected(_:for:completionhandler:).md)
  Called to set the selected state of the tab.
- [func setZoomFactor(Double, for: WKWebExtensionContext, completionHandler: ((any Error)?) -> Void)](wkwebextensiontab/setzoomfactor(_:for:completionhandler:).md)
  Called to set the zoom factor of the tab.
- [func shouldBypassPermissions(for: WKWebExtensionContext) -> Bool](wkwebextensiontab/shouldbypasspermissions(for:).md)
  Called to determine if the tab should bypass host permission checks.
- [func shouldGrantPermissionsOnUserGesture(for: WKWebExtensionContext) -> Bool](wkwebextensiontab/shouldgrantpermissionsonusergesture(for:).md)
  Called to determine if permissions should be granted for the tab on user gesture.
- [func size(for: WKWebExtensionContext) -> CGSize](wkwebextensiontab/size(for:).md)
  Called when the size of the tab is needed.
- [func takeSnapshot(using: WKSnapshotConfiguration, for: WKWebExtensionContext, completionHandler: (UIImage?, (any Error)?) -> Void)](wkwebextensiontab/takesnapshot(using:for:completionhandler:).md)
  Called to capture a snapshot of the current webpage as an image.
- [func title(for: WKWebExtensionContext) -> String?](wkwebextensiontab/title(for:).md)
  Called when the title of the tab is needed.
- [func url(for: WKWebExtensionContext) -> URL?](wkwebextensiontab/url(for:).md)
  Called when the URL of the tab is needed.
- [func webView(for: WKWebExtensionContext) -> WKWebView?](wkwebextensiontab/webview(for:).md)
  Called when the web view for the tab is needed.
- [func window(for: WKWebExtensionContext) -> (any WKWebExtensionWindow)?](wkwebextensiontab/window(for:).md)
  Called when the window containing the tab is needed.
- [func zoomFactor(for: WKWebExtensionContext) -> Double](wkwebextensiontab/zoomfactor(for:).md)
  Called when the zoom factor of the tab is needed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class WKWebExtension](wkwebextension.md)
  An object that encapsulates a web extension’s resources that the manifest file defines.
- [protocol WKWebExtensionWindow](wkwebextensionwindow.md)
  A protocol with methods that represent a window to web extensions.
- [class WKWebExtensionContext](wkwebextensioncontext.md)
  An object that represents the runtime environment for a web extension.
- [class WKWebExtensionController](wkwebextensioncontroller.md)
  An object that manages a set of loaded extension contexts.
- [protocol WKWebExtensionControllerDelegate](wkwebextensioncontrollerdelegate.md)
  A group of methods you use to customize web extension interactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab)*