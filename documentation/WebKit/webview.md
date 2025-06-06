# WebView

**Framework**: Webkit  
**Kind**: class

`WebView` is the core view class in the WebKit framework that manages interactions between the `WebFrame` and `WebFrameView` classes. To embed web content in your application, you just create a `WebView` object, attach it to a window, and send a [`load(_:)`](webframe/load(_:)-47p2s.md) message to its main frame.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
class WebView
```

#### Overview

> **Note**:  In apps that run in OS X 10.10 and later, use the [`WKWebView`](wkwebview.md) class instead of using [`WebView`](webview.md).

 In apps that run in OS X 10.10 and later, use the [`WKWebView`](wkwebview.md) class instead of using [`WebView`](webview.md).

Behind the scenes, `WebFrame` objects encapsulate the content contained in a single frame element. A hierarchy of `WebFrame` objects is used to model an entire webpage where the root is called the . There is a `WebFrameView` object per `WebFrame` object used to display the frame content. Therefore, there is a parallel hierarchy of `WebFrameView` objects used to render an entire page. The `WebView` object is also the parent view of this hierarchy. You do not need to create `WebFrame` and `WebFrameView` objects directly. These objects are automatically created when the page loads, either programmatically or by the user clicking a link.

You customize your embedded web content by implementing `WebView` delegates to handle certain aspects of the process. `WebView` objects have multiple delegates because the process of loading a webpage is asynchronous and complicated if errors occur. All the `WebView` delegates use informal protocols so you only need to implement only the delegates and methods that define the behavior you wish to change—default implementations are already provided.

For example, you might want to implement the frame load and resource load delegates to monitor the load progress and display status messages. Applications that use multiple windows may want to implement a user interface delegate. See the individual informal delegate protocols for more details: `WebFrameLoadDelegate`, `WebPolicyDelegate`, [`WebResourceLoadDelegate`](webresourceloaddelegate.md), and [`WebUIDelegate`](webuidelegate.md).

Another way to monitor load progress with less control is to observe the [`WebViewProgressEstimateChangedNotification`](webviewprogressestimatechangednotification.md), [`WebViewProgressFinishedNotification`](webviewprogressfinishednotification.md), and [`WebViewProgressStartedNotification`](webviewprogressstartednotification.md) notifications. For example, you could observe these notifications to implement a simple progress indicator in your application. You update the progress indicator by invoking the [`estimatedProgress`](webview/estimatedprogress.md) method to get an estimate of the amount of content that is currently loaded.

A `WebView` object is intended to support most features you would expect in a web browser except that it doesn’t implement the specific user interface for those features. You are responsible for implementing the user interface objects such as status bars, toolbars, buttons, and text fields. For example, a `WebView` object manages a back-forward list by default, and has [`goBack(_:)`](webview/goback(_:).md) and [`goForward(_:)`](webview/goforward(_:).md) action methods. It is your responsibility to create the buttons that would send theses action messages. Note, there is some overhead in maintaining a back-forward list and page cache, so you should disable it if your application doesn’t use it.

You use a `WebPreferences` object to encapsulate the preferences of a `WebView` object, such as the font, text encoding, and image settings. You can modify the preferences for individual `WebView` objects or specify a shared `WebPreferences` object using the [`preferencesIdentifier`](webview/preferencesidentifier.md) method. Use the [`autosaves`](webpreferences/autosaves.md)  `WebPreferences` method to specify whether the preferences should be automatically saved to the user defaults database.

You can also extend WebKit by implementing your own document view and representation classes for specific MIME types. Use the [`registerClass(_:representationClass:forMIMEType:)`](webview/registerclass(_:representationclass:formimetype:).md) class method to register your custom classes with a `WebView` object.

## Topics

### Registering Document Views and Representations
- [class func registerURLScheme(asLocal: String!)](webview/registerurlscheme(aslocal:).md)
  Adds the specified URL scheme to the list of local schemes.
- [class func registerClass(AnyClass!, representationClass: AnyClass!, forMIMEType: String!)](webview/registerclass(_:representationclass:formimetype:).md)
  Specifies the view and representation objects to be used for specific MIME types.
### Initializing Views
- [init!(frame: NSRect, frameName: String!, groupName: String!)](webview/init(frame:framename:groupname:).md)
  Initializes the receiver with a frame rectangle, frame name, and group name.
### Closing the View
- [func close()](webview/close.md)
  Closes the web view when it’s no longer needed.
- [var shouldCloseWithWindow: Bool](webview/shouldclosewithwindow.md)
  A Boolean that indicates whether the web view should close when its window or host window closes.
### Getting the Main Frame
- [var mainFrame: WebFrame!](webview/mainframe.md)
  The main frame, the root of the web frame hierarchy for this page.
### Loading Content
- [func stopLoading(Any?)](webview/stoploading(_:).md)
  An action method that stops the loading of any web frame content managed by the receiver.
- [func takeStringURLFrom(Any?)](webview/takestringurlfrom(_:).md)
  Sets the receiver’s current location by obtaining a URL string from the sender.
- [func reload(Any?)](webview/reload(_:).md)
  An action method that reloads the current page.
- [func reloadFromOrigin(Any?)](webview/reloadfromorigin(_:).md)
  Action method that performs an end-to-end revalidation using cache-validating conditionals if possible.
- [var estimatedProgress: Double](webview/estimatedprogress.md)
  An estimate, as a percentage, of the amount of content that is currently loaded.
### Drawing
- [var drawsBackground: Bool](webview/drawsbackground.md)
  A Boolean that indicates whether the web view draws a background.
- [var shouldUpdateWhileOffscreen: Bool](webview/shouldupdatewhileoffscreen.md)
  A Boolean that inidicates whether the web view should update even when it is not in a window that is currently visible.
### Moving Back and Forward
- [func setMaintainsBackForwardList(Bool)](webview/setmaintainsbackforwardlist(_:).md)
  Sets whether to use a back-forward list.
- [var backForwardList: WebBackForwardList!](webview/backforwardlist.md)
  The receiver’s back-forward list.
- [var canGoBack: Bool](webview/cangoback.md)
  A Boolean that indicates whether the previous location can be loaded.
- [func goBack() -> Bool](webview/goback.md)
  Loads the previous location in the back-forward list.
- [func goBack(Any?)](webview/goback(_:).md)
  An action method that loads the previous location in the back-forward list.
- [var canGoForward: Bool](webview/cangoforward.md)
  A Boolean that indicates whether the next location can be loaded.
- [func goForward() -> Bool](webview/goforward.md)
  Loads the next location in the back-forward list.
- [func goForward(Any?)](webview/goforward(_:).md)
  An action method that loads the next location in the back-forward list.
- [func go(toBackForwardItem: WebHistoryItem!) -> Bool](webview/go(tobackforwarditem:).md)
  Loads a specific location from the back-forward list and sets it as the current item.
### Changing the Text Size
- [var canMakeTextLarger: Bool](webview/canmaketextlarger.md)
  A Boolean that indicates whether the text can be made larger.
- [func makeTextLarger(Any?)](webview/maketextlarger(_:).md)
  Action method that increases the text size by one unit.
- [var canMakeTextSmaller: Bool](webview/canmaketextsmaller.md)
  A Boolean that indicates whether the text can be made smaller.
- [func makeTextSmaller(Any?)](webview/maketextsmaller(_:).md)
  Action method that reduces the text size by one unit.
### Getting and Setting Delegates
- [var downloadDelegate: (any WebDownloadDelegate)!](webview/downloaddelegate.md)
  The receiver’s download delegate.
- [var frameLoadDelegate: (any WebFrameLoadDelegate)!](webview/frameloaddelegate.md)
  The receiver’s frame load delegate.
- [var policyDelegate: (any WebPolicyDelegate)!](webview/policydelegate.md)
  The receiver’s policy delegate.
- [var resourceLoadDelegate: (any WebResourceLoadDelegate)!](webview/resourceloaddelegate.md)
  The receiver’s resource load delegate.
- [var uiDelegate: (any WebUIDelegate)!](webview/uidelegate.md)
  The receiver’s user interface delegate.
### Getting and Setting the Window
- [var hostWindow: NSWindow!](webview/hostwindow.md)
  The receiver’s host window.
### Getting and Setting Preferences
- [var preferences: WebPreferences!](webview/preferences.md)
  The receiver’s preferences.
- [var preferencesIdentifier: String!](webview/preferencesidentifier.md)
  The identifier of the receiver’s preferences.
### Getting and Setting Frame Contents
- [var isLoading: Bool](webview/isloading.md)
  A Boolean that indicates whether the web view is loading content.
- [var selectedFrame: WebFrame!](webview/selectedframe.md)
  The frame with the active selection.
- [var mainFrameURL: String!](webview/mainframeurl.md)
  The URL that the main frame loads.
- [var mainFrameTitle: String!](webview/mainframetitle.md)
  The HTML title of the loaded page.
- [var mainFrameIcon: NSImage!](webview/mainframeicon.md)
  The site’s favicon.
- [var mainFrameDocument: DOMDocument!](webview/mainframedocument.md)
  The DOM document for the main frame.
### Getting and Setting Content Information
- [class func canShowMIMEType(String!) -> Bool](webview/canshowmimetype(_:).md)
  Returns whether the receiver can display content of a given MIME type.
- [class func mimeTypesShownAsHTML() -> [Any]!](webview/mimetypesshownashtml.md)
  Returns a list of MIME types that WebKit renders as HTML.
- [class func setMIMETypesShownAsHTML([Any]!)](webview/setmimetypesshownashtml(_:).md)
  Sets the MIME types that WebKit attempts to render as HTML.
- [class func canShowMIMEType(asHTML: String!) -> Bool](webview/canshowmimetype(ashtml:).md)
  Returns whether the receiver interprets a MIME type as HTML.
- [var supportsTextEncoding: Bool](webview/supportstextencoding.md)
  A Boolean that indicates whether the document view supports different text encodings.
- [var customTextEncodingName: String!](webview/customtextencodingname.md)
  The custom text encoding name.
- [var textSizeMultiplier: Float](webview/textsizemultiplier.md)
  The font size multiplier for text displayed in web frame view objects managed by the receiver.
### Searching the Document
- [func search(for: String!, direction: Bool, caseSensitive: Bool, wrap: Bool) -> Bool](webview/search(for:direction:casesensitive:wrap:).md)
  Searches a document view for a string and highlights it if it is found.
### Getting and Setting the Group Name
- [var groupName: String!](webview/groupname.md)
  The receiver’s group name.
### Getting and Setting User-agent Strings
- [func userAgent(for: URL!) -> String!](webview/useragent(for:).md)
  Returns the appropriate user-agent string for a given URL.
- [var applicationNameForUserAgent: String!](webview/applicationnameforuseragent.md)
  The receiver’s application name that is used in the user-agent string.
- [var customUserAgent: String!](webview/customuseragent.md)
  The receiver’s custom user-agent string.
### Processing JavaScript
- [func stringByEvaluatingJavaScript(from: String!) -> String!](webview/stringbyevaluatingjavascript(from:).md)
  Returns the result of running a script.
### Using the Pasteboard
- [class func url(from: NSPasteboard!) -> URL!](webview/url(from:).md)
  Returns a URL from the specified pasteboard.
- [class func urlTitle(from: NSPasteboard!) -> String!](webview/urltitle(from:).md)
  Returns the title of a URL from the specified pasteboard.
- [func pasteboardTypes(forElement: [AnyHashable : Any]!) -> [Any]!](webview/pasteboardtypes(forelement:).md)
  Returns an array of pasteboard types for an element.
- [var pasteboardTypesForSelection: [Any]!](webview/pasteboardtypesforselection.md)
  An array of pasteboard types that can be used for the current selection of the receiver.
- [func writeElement([AnyHashable : Any]!, withPasteboardTypes: [Any]!, to: NSPasteboard!)](webview/writeelement(_:withpasteboardtypes:to:).md)
  Writes an element to the pasteboard using a list of types.
- [func writeSelection(withPasteboardTypes: [Any]!, to: NSPasteboard!)](webview/writeselection(withpasteboardtypes:to:).md)
  Writes the receiver’s current selection to a pasteboard using a list of types.
### Dragging
- [func element(at: NSPoint) -> [AnyHashable : Any]!](webview/element(at:).md)
  Returns a dictionary description of the element at a given point in the receiver’s coordinates.
- [func moveDragCaret(to: NSPoint)](webview/movedragcaret(to:).md)
  Moves the drag caret that indicates the destination of a drag operation to a given point.
- [func removeDragCaret()](webview/removedragcaret.md)
  Removes the drag caret that indicates the destination of a drag operation.
### Cut, Copy and Paste Action Methods
- [func copy(Any?)](webview/copy(_:).md)
  Action method that copies the selected content to the general pasteboard.
- [func copyFont(Any?)](webview/copyfont(_:).md)
  An action method that copies font information onto the font pasteboard.
- [func cut(Any?)](webview/cut(_:).md)
  An action method that deletes selected content and puts it on the general pasteboard.
- [func delete(Any?)](webview/delete(_:).md)
  An action method that deletes the selected content.
- [func paste(Any?)](webview/paste(_:).md)
  An action method that pastes content from the pasteboard at the insertion point or over the selection.
- [func pasteFont(Any?)](webview/pastefont(_:).md)
  An action method that pastes font information from the font pasteboard.
- [func pasteAsPlainText(Any?)](webview/pasteasplaintext(_:).md)
  An action method that pastes pasteboard content as plain text.
- [func pasteAsRichText(Any?)](webview/pasteasrichtext(_:).md)
  An action method that pastes pasteboard content into the receiver as rich text, maintaining its attributes.
### Content Alignment Action Methods
- [func alignCenter(Any?)](webview/aligncenter(_:).md)
  An action method that applies center alignment to selected content or all content if there’s no selection.
- [func alignJustified(Any?)](webview/alignjustified(_:).md)
  An action method that applies full justification to selected content or all content if there’s no selection.
- [func alignLeft(Any?)](webview/alignleft(_:).md)
  An action method that applies left justification to selected content or all content if there’s no selection.
- [func alignRight(Any?)](webview/alignright(_:).md)
  An action method that applies right justification to selected content or all content if there is no selection.
### Changing the Font, Color and Other Attributes When Editing
- [func changeFont(Any?)](webview/changefont(_:).md)
  An action method that changes the font of the selection, or all content if there is no selection.
- [func changeAttributes(Any?)](webview/changeattributes(_:).md)
  An action method that changes the attributes of the current selection.
- [func changeDocumentBackgroundColor(Any?)](webview/changedocumentbackgroundcolor(_:).md)
  Sets the background color of the selected content.
- [func changeColor(Any?)](webview/changecolor(_:).md)
  Sets the color of the selected content.
### Spell-checking Action Methods
- [func checkSpelling(Any?)](webview/checkspelling(_:).md)
  An action method that searches for a misspelled word in the receiver.
- [func showGuessPanel(Any?)](webview/showguesspanel(_:).md)
  An action method that shows a spelling correction panel.
### Find Panel Action Method
- [func performFindPanelAction(Any?)](webview/performfindpanelaction(_:).md)
  An action method that opens the Find menu and Find panel.
### Controlling Speakable Text
- [func startSpeaking(Any?)](webview/startspeaking(_:).md)
  An action method that starts speaking the selected text or all text if there’s no selection.
- [func stopSpeaking(Any?)](webview/stopspeaking(_:).md)
  An action method that stops speaking that is in progress.
### Getting and Setting Document Editing Attributes
- [var isEditable: Bool](webview/iseditable.md)
  A Boolean that indicates whether the user is allowed to edit the document.
- [var smartInsertDeleteEnabled: Bool](webview/smartinsertdeleteenabled.md)
  A Boolean that indicates whether smart-space insertion and deletion is enabled.
- [var isContinuousSpellCheckingEnabled: Bool](webview/iscontinuousspellcheckingenabled.md)
  A Boolean that indicates whether the web view has continuous spell-checking enabled.
- [var spellCheckerDocumentTag: Int](webview/spellcheckerdocumenttag.md)
  The spell-checker document tag for this document.
- [var undoManager: UndoManager!](webview/undomanager.md)
  The receiver’s undo manager.
- [var editingDelegate: (any WebEditingDelegate)!](webview/editingdelegate.md)
  The receiver’s editing delegate.
- [func editableDOMRange(for: NSPoint) -> DOMRange!](webview/editabledomrange(for:).md)
  Returns the editable DOM object located at a given point.
### Editing Documents
- [func replaceSelection(with: DOMNode!)](webview/replaceselection(with:)-5px9m.md)
  Replaces the receiver’s current selection with the specified DOM node.
- [func replaceSelection(withText: String!)](webview/replaceselection(withtext:).md)
  Replaces the current selection with a string of text.
- [func replaceSelection(withMarkupString: String!)](webview/replaceselection(withmarkupstring:).md)
  Replaces the current selection with mixed text and markup.
- [func replaceSelection(with: WebArchive!)](webview/replaceselection(with:)-3vj8l.md)
  Replaces the current selection with an archive’s contents.
- [func deleteSelection()](webview/deleteselection.md)
  Deletes the receiver’s current selection unless it’s collapsed.
- [func moveToBeginningOfSentence(Any?)](webview/movetobeginningofsentence(_:).md)
  Moves the insertion point to the beginning of the current sentence.
- [func moveToBeginningOfSentenceAndModifySelection(Any?)](webview/movetobeginningofsentenceandmodifyselection(_:).md)
  Moves the insertion point and extends the selection to the beginning of the current sentence.
- [func moveToEndOfSentence(Any?)](webview/movetoendofsentence(_:).md)
  Moves the insertion point to the end of the current sentence.
- [func moveToEndOfSentenceAndModifySelection(Any?)](webview/movetoendofsentenceandmodifyselection(_:).md)
  Moves the insertion point and extends the selection to the end of the current sentence.
- [func selectSentence(Any?)](webview/selectsentence(_:).md)
  Selects the entire sentence around the insertion point.
- [func toggleContinuousSpellChecking(Any?)](webview/togglecontinuousspellchecking(_:).md)
  Toggles whether continuous spell checking is available.
- [func toggleSmartInsertDelete(Any?)](webview/togglesmartinsertdelete(_:).md)
  Toggles whether spaces around selected words are inserted or deleted to preserve proper spacing and punctuation.
- [var canMakeTextStandardSize: Bool](webview/canmaketextstandardsize.md)
  A Boolean that indicates whether the current text size is a multiple of 1.
- [func makeTextStandardSize(Any?)](webview/maketextstandardsize(_:).md)
  Resets the text size to a multiple of 1.
- [var maintainsInactiveSelection: Bool](webview/maintainsinactiveselection.md)
  A Boolean that indicates whether the selection is maintained when focus is lost.
### Selecting Content in the Document
- [var selectedDOMRange: DOMRange!](webview/selecteddomrange.md)
  The range of the current selection.
- [func setSelectedDOMRange(DOMRange!, affinity: NSSelectionAffinity)](webview/setselecteddomrange(_:affinity:).md)
  Selects a range of nodes.
- [var selectionAffinity: NSSelectionAffinity](webview/selectionaffinity.md)
  The current selection affinity.
### Getting and Setting CSS Properties
- [func computedStyle(for: DOMElement!, pseudoElement: String!) -> DOMCSSStyleDeclaration!](webview/computedstyle(for:pseudoelement:).md)
  Returns the computed style of an element and its pseudo element.
- [var mediaStyle: String!](webview/mediastyle.md)
  The receiver’s CSS media property.
- [var typingStyle: DOMCSSStyleDeclaration!](webview/typingstyle.md)
  The receiver’s CSS typing style.
- [func styleDeclaration(withText: String!) -> DOMCSSStyleDeclaration!](webview/styledeclaration(withtext:).md)
  Returns the CSS style declaration for the specified text.
- [func applyStyle(DOMCSSStyleDeclaration!)](webview/applystyle(_:).md)
  Applies the CSS typing style to the current selection.
### Using WebScript
- [var windowScriptObject: WebScriptObject!](webview/windowscriptobject.md)
  The receiver’s window object from the scripting environment.
### Constants
- [Element Dictionary Keys](element-dictionary-keys.md)
  Predefined keys used to access an element dictionary.
### Notifications
- [static let WebViewDidBeginEditing: NSNotification.Name](../foundation/nsnotification/name/1408490-webviewdidbeginediting.md)
  Posted when a web view begins any operation that changes its contents in response to user editing.
- [static let WebViewDidChange: NSNotification.Name](../foundation/nsnotification/name/1408476-webviewdidchange.md)
  Posted when a web view performs any operation that changes its contents in response to user editing.
- [static let WebViewDidChangeSelection: NSNotification.Name](../foundation/nsnotification/name/1408552-webviewdidchangeselection.md)
  Posted when a web view changes its typing selection.
- [static let WebViewDidChangeTypingStyle: NSNotification.Name](../foundation/nsnotification/name/1408443-webviewdidchangetypingstyle.md)
  Posted when a web view changes its typing style.
- [static let WebViewDidEndEditing: NSNotification.Name](../foundation/nsnotification/name/1408570-webviewdidendediting.md)
  Posted when a web view ends any operation that changes its contents in response to user editing.
- [static let WebViewProgressEstimateChanged: NSNotification.Name](../foundation/nsnotification/name/1408355-webviewprogressestimatechanged.md)
  Posted by a WebView object when the estimated progress value of a load changes.
- [static let WebViewProgressFinished: NSNotification.Name](../foundation/nsnotification/name/1408430-webviewprogressfinished.md)
  Posted by a WebView object when the load has finished.
- [static let WebViewProgressStarted: NSNotification.Name](../foundation/nsnotification/name/1408460-webviewprogressstarted.md)
  Posted by a WebView object when a load begins, including a load that is initiated in a subframe.
### Instance Methods
- [func overWrite(Any?)](webview/overwrite(_:).md)

## Relationships

### Inherits From
- [NSView](../AppKit/NSView.md)
### Conforms To
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
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [NSUserInterfaceValidations](../AppKit/NSUserInterfaceValidations.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [WebKit Objective-C Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/DisplayWebContent.html#//apple_ref/doc/uid/10000164i)
- [class WebPreferences](webpreferences.md)
  WebPreferences encapsulates the preferences you can change per WebView object. These preferences include font, text encoding, and image settings. Normally a WebView object uses the standard preferences returned by the [`standard()`](webpreferences/standard().md) class method. However, you can modify the preferences for individual WebView instances too. Use the [`preferencesIdentifier`](webview/preferencesidentifier.md) WebView method to change a WebView object’s preferences, or to share preferences between WebView objects. Use the [`autosaves`](webpreferences/autosaves.md) method to specify if the preferences object should be automatically saved to the user defaults database.
- [protocol WebEditingDelegate](webeditingdelegate.md)
- [protocol WebUIDelegate](webuidelegate.md)
  Web view user interface delegates implement this protocol to control the opening of new windows, augment the behavior of default menu items displayed when the user clicks elements, and perform other user interface–related tasks. These methods can be invoked as a result of handling JavaScript or other plug-in content. Delegates that display more than one web view per window, for example, need to implement some of these methods to handle that case. The default implementation assumes one window per web view, so non-conventional user interfaces might implement a user interface delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview)*