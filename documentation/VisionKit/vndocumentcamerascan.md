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
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Structuring Recognized Text on a Document](structuring_recognized_text_on_a_document.md)
  Detect, recognize, and structure text on a business card or receipt using Vision and VisionKit.
- [class VNDocumentCameraViewController](vndocumentcameraviewcontroller.md)
  An object that presents UI for a camera pass-through that helps people scan physical documents.
- [protocol VNDocumentCameraViewControllerDelegate](vndocumentcameraviewcontrollerdelegate.md)
  A delegate protocol through which the document camera returns its scanned results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/vndocumentcamerascan)*