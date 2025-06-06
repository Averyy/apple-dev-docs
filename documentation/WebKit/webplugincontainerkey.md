# WebPlugInContainerKey

**Framework**: Webkit  
**Kind**: var

An object that conforms to the `WebPlugInContainer` informal protocol. This object is used for callbacks from the plug-in to the enclosing application. If `WebPlugInContainerKey` is `nil`, no callbacks will occur.

**Availability**:
- macOS 10.3+

## Declaration

```swift
let WebPlugInContainerKey: String
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webplugincontainerkey)*