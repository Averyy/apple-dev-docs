# WebKit Constants

**Framework**: Webkit

WebKit constants affecting multiple classes.

## Topics

### WKPreview Constants
- [let WKPreviewActionItemIdentifierAddToReadingList: String](wkpreviewactionitemidentifieraddtoreadinglist.md)
  Adds the item to the Reading List.
- [let WKPreviewActionItemIdentifierCopy: String](wkpreviewactionitemidentifiercopy.md)
  Copies the item to the clipboard.
- [let WKPreviewActionItemIdentifierOpen: String](wkpreviewactionitemidentifieropen.md)
  Opens the item.
- [let WKPreviewActionItemIdentifierShare: String](wkpreviewactionitemidentifiershare.md)
  Displays the Share panel options available for the item.
### WKWebsiteDataType Constants
- [let WKWebsiteDataTypeCookies: String](wkwebsitedatatypecookies.md)
  Cookies.
- [let WKWebsiteDataTypeDiskCache: String](wkwebsitedatatypediskcache.md)
  On-disk caches.
- [let WKWebsiteDataTypeIndexedDBDatabases: String](wkwebsitedatatypeindexeddbdatabases.md)
  IndexedDB databases.
- [let WKWebsiteDataTypeLocalStorage: String](wkwebsitedatatypelocalstorage.md)
  HTML local storage.
- [let WKWebsiteDataTypeMemoryCache: String](wkwebsitedatatypememorycache.md)
  In-memory caches.
- [let WKWebsiteDataTypeOfflineWebApplicationCache: String](wkwebsitedatatypeofflinewebapplicationcache.md)
  HTML offline web app caches.
- [let WKWebsiteDataTypeSessionStorage: String](wkwebsitedatatypesessionstorage.md)
  HTML session storage.
- [let WKWebsiteDataTypeWebSQLDatabases: String](wkwebsitedatatypewebsqldatabases.md)
  WebSQL databases.
### DOM Constants
- [let DOMEventException: String](domeventexception.md)
- [let DOMException: String](domexception.md)
- [let DOMRangeException: String](domrangeexception.md)
- [let DOMXPathException: String](domxpathexception.md)
- [var DOM_BAD_BOUNDARYPOINTS_ERR: DOMRangeExceptionCode](dom_bad_boundarypoints_err.md)
- [var DOM_DOMSTRING_SIZE_ERR: DOMExceptionCode](dom_domstring_size_err.md)
- [var DOM_HIERARCHY_REQUEST_ERR: DOMExceptionCode](dom_hierarchy_request_err.md)
- [var DOM_INDEX_SIZE_ERR: DOMExceptionCode](dom_index_size_err.md)
- [var DOM_INUSE_ATTRIBUTE_ERR: DOMExceptionCode](dom_inuse_attribute_err.md)
- [var DOM_INVALID_ACCESS_ERR: DOMExceptionCode](dom_invalid_access_err.md)
- [var DOM_INVALID_CHARACTER_ERR: DOMExceptionCode](dom_invalid_character_err.md)
- [var DOM_INVALID_EXPRESSION_ERR: DOMXPathExceptionCode](dom_invalid_expression_err.md)
- [var DOM_INVALID_MODIFICATION_ERR: DOMExceptionCode](dom_invalid_modification_err.md)
- [var DOM_INVALID_NODE_TYPE_ERR: DOMRangeExceptionCode](dom_invalid_node_type_err.md)
- [var DOM_INVALID_STATE_ERR: DOMExceptionCode](dom_invalid_state_err.md)
- [var DOM_NAMESPACE_ERR: DOMExceptionCode](dom_namespace_err.md)
- [var DOM_NOT_FOUND_ERR: DOMExceptionCode](dom_not_found_err.md)
- [var DOM_NOT_SUPPORTED_ERR: DOMExceptionCode](dom_not_supported_err.md)
- [var DOM_NO_DATA_ALLOWED_ERR: DOMExceptionCode](dom_no_data_allowed_err.md)
- [var DOM_NO_MODIFICATION_ALLOWED_ERR: DOMExceptionCode](dom_no_modification_allowed_err.md)
- [var DOM_SYNTAX_ERR: DOMExceptionCode](dom_syntax_err.md)
- [var DOM_TYPE_ERR: DOMXPathExceptionCode](dom_type_err.md)
- [var DOM_UNSPECIFIED_EVENT_TYPE_ERR: DOMEventExceptionCode](dom_unspecified_event_type_err.md)
- [var DOM_WRONG_DOCUMENT_ERR: DOMExceptionCode](dom_wrong_document_err.md)
### WebKit Constants (Legacy)
- [let WebActionButtonKey: String](webactionbuttonkey.md)
  An NSNumber object where `0` indicates the left button, `1` indicates the middle button, and `2` indicates the right button.
- [let WebActionElementKey: String](webactionelementkey.md)
  A dictionary containing element information. See [`WebView`](webview.md) for a description of the key-value pairs in this dictionary.
- [let WebActionModifierFlagsKey: String](webactionmodifierflagskey.md)
  An unsigned number that indicates the modifier flag.
- [let WebActionNavigationTypeKey: String](webactionnavigationtypekey.md)
  The navigation type of the action. Can be any of the values defined in [`WebNavigationType`](webnavigationtype.md) below.
- [let WebActionOriginalURLKey: String](webactionoriginalurlkey.md)
  The URL that initiated the action.
- [let WebArchivePboardType: String](webarchivepboardtype.md)
  The pasteboard type constant used when adding or accessing a WebArchive on the pasteboard.
- [let WebElementDOMNodeKey: String](webelementdomnodekey.md)
  The DOMNode for this element.
- [let WebElementFrameKey: String](webelementframekey.md)
  The WebFrame object associated with this element.
- [let WebElementImageAltStringKey: String](webelementimagealtstringkey.md)
  An NSString of the ALT attribute of an image element.
- [let WebElementImageKey: String](webelementimagekey.md)
  An NSImage representing an image element.
- [let WebElementImageRectKey: String](webelementimagerectkey.md)
  An NSValue containing an NSRect, the size of an image element.
- [let WebElementImageURLKey: String](webelementimageurlkey.md)
  An NSURL containing the location of an image element.
- [let WebElementIsSelectedKey: String](webelementisselectedkey.md)
  An NSNumber used as a BOOL value to indicate whether a text element is selected or not. Zero value indicates false, true otherwise.
- [let WebElementLinkLabelKey: String](webelementlinklabelkey.md)
  An NSString containing the text within an anchor.
- [let WebElementLinkTargetFrameKey: String](webelementlinktargetframekey.md)
  The WebFrame object associated with the target of the anchor.
- [let WebElementLinkTitleKey: String](webelementlinktitlekey.md)
  An NSString containing the title of an anchor.
- [let WebElementLinkURLKey: String](webelementlinkurlkey.md)
  An NSURL containing the location of a link if the element is within an anchor.
- [static let WebHistoryAllItemsRemoved: NSNotification.Name](../foundation/nsnotification/name/1521391-webhistoryallitemsremoved.md)
  Posted when all history items have been removed from the web history.
- [static let WebHistoryItemChanged: NSNotification.Name](../foundation/nsnotification/name/1525160-webhistoryitemchanged.md)
  Posted by a WebHistoryItem object when the value of the history item’s title, alternate title, URL strings, or last visited interval changes.
- [static let WebHistoryItemsAdded: NSNotification.Name](../foundation/nsnotification/name/1521408-webhistoryitemsadded.md)
  Posted when history items have been added to a web history.
- [let WebHistoryItemsKey: String](webhistoryitemskey.md)
  The key to access an array containing the added or removed web history items.
- [static let WebHistoryItemsRemoved: NSNotification.Name](../foundation/nsnotification/name/1521392-webhistoryitemsremoved.md)
  Posted when items have been removed from the web history.
- [static let WebHistoryLoaded: NSNotification.Name](../foundation/nsnotification/name/1521395-webhistoryloaded.md)
  Posted when web history items have been loaded from a URL.
- [static let WebHistorySaved: NSNotification.Name](../foundation/nsnotification/name/1521397-webhistorysaved.md)
  Posted when web history items have been saved to a URL.
- [let WebKitErrorDomain: String](webkiterrordomain.md)
- [let WebKitErrorMIMETypeKey: String](webkiterrormimetypekey.md)
- [let WebKitErrorPlugInNameKey: String](webkiterrorpluginnamekey.md)
- [let WebKitErrorPlugInPageURLStringKey: String](webkiterrorpluginpageurlstringkey.md)
- [let WebPlugInAttributesKey: String](webpluginattributeskey.md)
  The `NSDictionary` object containing all names and values of all attributes of the plug-in’s associated HTML element, as well as all names and values of the parameters to be passed to the plug-in. For example, this dictionary will contain all `PARAM` elements within an `APPLET` element. If attribute and parameter names conflict, the attributes of an element take precedence over any of its parameters. All keys and values in this dictionary must be of type `NSString`. .
- [let WebPlugInBaseURLKey: String](webpluginbaseurlkey.md)
  The base URL of the document containing the plug-in’s view. .
- [let WebPlugInContainerKey: String](webplugincontainerkey.md)
  An object that conforms to the `WebPlugInContainer` informal protocol. This object is used for callbacks from the plug-in to the enclosing application. If `WebPlugInContainerKey` is `nil`, no callbacks will occur.
- [let WebPlugInContainingElementKey: String](webplugincontainingelementkey.md)
  If an element of the page’s Document Object Model was used to specify the plug-in, this will contain that element. Otherwise, it will be `nil`.
- [let WebPlugInShouldLoadMainResourceKey: String](webpluginshouldloadmainresourcekey.md)
  A Boolean value indicating whether the plug-in should load its own main resource (the `src` URL, in most cases).
- [static let WebPreferencesChanged: NSNotification.Name](../foundation/nsnotification/name/1536311-webpreferenceschanged.md)
  Posted when the web preference settings are changed. 
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
### Constants
- [let WKErrorDomain: String](wkerrordomain.md)
  String that identifies the WebKit error domain.
- [let WKWebsiteDataTypeFetchCache: String](wkwebsitedatatypefetchcache.md)
- [let WKWebsiteDataTypeFileSystem: String](wkwebsitedatatypefilesystem.md)
- [let WKWebsiteDataTypeHashSalt: String](wkwebsitedatatypehashsalt.md)
- [let WKWebsiteDataTypeMediaKeys: String](wkwebsitedatatypemediakeys.md)
- [let WKWebsiteDataTypeSearchFieldRecentSearches: String](wkwebsitedatatypesearchfieldrecentsearches.md)
- [let WKWebsiteDataTypeServiceWorkerRegistrations: String](wkwebsitedatatypeserviceworkerregistrations.md)

## See Also

- [class DOMAbstractView](domabstractview.md)
- [class DOMAttr](domattr.md)
- [class DOMBlob](domblob.md)
- [class DOMCDATASection](domcdatasection.md)
- [class DOMCharacterData](domcharacterdata.md)
- [class DOMComment](domcomment.md)
- [class DOMCounter](domcounter.md)
- [class DOMCSSCharsetRule](domcsscharsetrule.md)
- [class DOMCSSFontFaceRule](domcssfontfacerule.md)
- [class DOMCSSImportRule](domcssimportrule.md)
- [class DOMCSSMediaRule](domcssmediarule.md)
- [class DOMCSSPageRule](domcsspagerule.md)
- [class DOMCSSPrimitiveValue](domcssprimitivevalue.md)
- [class DOMCSSRule](domcssrule.md)
- [class DOMCSSRuleList](domcssrulelist.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webkit-constants)*