# VNDocumentCameraScan

**Framework**: VisionKit  
**Kind**: class

A single document scanned in the document camera.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class VNDocumentCameraScan
```

#### Overview

When the document camera scans a document, it returns the resulting information in this format, through the delegate method [`documentCameraViewController(_:didFinishWith:)`](vndocumentcameraviewcontrollerdelegate/documentcameraviewcontroller(_:didfinishwith:).md).

## Topics

### Reading the scanned document
- [var title: String](vndocumentcamerascan/title.md)
  The title of the scanned document.
- [var pageCount: Int](vndocumentcamerascan/pagecount.md)
  The number of pages in the scanned document.
- [func imageOfPage(at: Int) -> UIImage](vndocumentcamerascan/imageofpage(at:).md)
  Requests the image of a page at a specified index.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [Structuring recognized text on a document](structuring-recognized-text-on-a-document.md)
  Detect, recognize, and structure text on a business card or receipt using Vision and VisionKit.
- [class VNDocumentCameraViewController](vndocumentcameraviewcontroller.md)
  An object that presents UI for a camera pass-through that helps people scan physical documents.
- [protocol VNDocumentCameraViewControllerDelegate](vndocumentcameraviewcontrollerdelegate.md)
  A delegate protocol through which the document camera returns its scanned results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/vndocumentcamerascan)*