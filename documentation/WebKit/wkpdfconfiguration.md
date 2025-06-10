# WKPDFConfiguration

**Framework**: WebKit  
**Kind**: class

The configuration data to use when generating a PDF representation of a web view’s contents.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class WKPDFConfiguration
```

#### Overview

Create a [`WKPDFConfiguration`](wkpdfconfiguration.md) object when you want to generate a PDF version of your web view’s content. Use this object to specify the portion of the web view to capture. To generate the PDF content, pass the configuration object to the [`createPDF(configuration:completionHandler:)`](wkwebview/createpdf(configuration:completionhandler:).md) method of [`WKWebView`](wkwebview.md), which returns the PDF data for you to use.

## Topics

### Specifying the snapshot dimensions
- [var rect: CGRect?](wkpdfconfiguration/rect-2a0vp.md)
  The portion of your web view to capture, specified as a rectangle in the view’s coordinate system.
### Specifying snapshot properties
- [var allowTransparentBackground: Bool](wkpdfconfiguration/allowtransparentbackground.md)
  A Boolean value that indicates whether the PDF may have a transparent background.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class WKSnapshotConfiguration](wksnapshotconfiguration.md)
  The configuration data to use when generating an image from a web view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkpdfconfiguration)*