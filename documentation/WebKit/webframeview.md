# WebFrameView

**Framework**: WebKit  
**Kind**: class

`WebFrameView` objects and their subviews display the web content contained in a frame. You never create instances of `WebFrameView` directly—`WebView` objects create and manage a hierarchy of `WebFrameView` objects, one for each frame. `WebFrameView` objects use a scroll view whose document view conforms to the [`WebDocumentView`](webdocumentview.md) protocol.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
class WebFrameView
```

## Topics

### Getting the Web Frame
- [var webFrame: WebFrame!](webframeview/webframe.md)
  The web frame.
### Getting Subviews
- [var documentView: (any NSView & WebDocumentView)!](webframeview/documentview.md)
  The subview that displays the web content.
### Setting Scrolling Behavior
- [var allowsScrolling: Bool](webframeview/allowsscrolling.md)
  A Boolean that indicates whether the frame view should allow users to scroll.
### Printing Views
- [var canPrintHeadersAndFooters: Bool](webframeview/canprintheadersandfooters.md)
  A Boolean value indicating whether the receiver can print headers and footers.
- [func printOperation(with: NSPrintInfo!) -> NSPrintOperation!](webframeview/printoperation(with:).md)
  Returns a print operation object to print this frame.
- [var documentViewShouldHandlePrint: Bool](webframeview/documentviewshouldhandleprint.md)
  A Boolean value indicating whether the document view should handle a print operation.
- [func printDocumentView()](webframeview/printdocumentview.md)
  Prints the receiver.

## Relationships

### Inherits From
- [NSView](../AppKit/NSView.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class WebFrame](webframe.md)
  A `WebFrame` object encapsulates the data displayed in a `WebFrameView` object. There is one `WebFrame` object per frame displayed in a `WebView`. An entire webpage is represented by a hierarchy of `WebFrame` objects in which the root object is called the .
- [class WebDataSource](webdatasource.md)
  `WebDataSource` encapsulates the web content to be displayed in a web frame view. A `WebDataSource` object has a representation object, conforming to the `WebDocumentRepresentation` protocol, that holds the data in an appropriate format depending on the MIME type. You can extend WebKit to support new MIME types by implementing your own view and representation classes, and specifying the mapping between them using the  [`registerClass(_:representationClass:forMIMEType:)`](webview-swift.class/registerclass(_:representationclass:formimetype:).md) `WebView` class method.
- [protocol WebFrameLoadDelegate](webframeloaddelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframeview)*