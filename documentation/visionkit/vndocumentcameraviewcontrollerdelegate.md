# VNDocumentCameraViewControllerDelegate

**Framework**: VisionKit  
**Kind**: protocol

A delegate protocol through which the document camera returns its scanned results.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
protocol VNDocumentCameraViewControllerDelegate : NSObjectProtocol
```

#### Overview

Your app is responsible for dismissing the document camera in all delegate callback methods.

## Topics

### Determining scan results
- [func documentCameraViewController(VNDocumentCameraViewController, didFinishWith: VNDocumentCameraScan)](vndocumentcameraviewcontrollerdelegate/documentcameraviewcontroller(_:didfinishwith:).md)
  Tells the delegate that the user successfully saved a scanned document from the document camera.
- [func documentCameraViewControllerDidCancel(VNDocumentCameraViewController)](vndocumentcameraviewcontrollerdelegate/documentcameraviewcontrollerdidcancel(_:).md)
  Tells the delegate that the user canceled out of the document scanner camera.
- [func documentCameraViewController(VNDocumentCameraViewController, didFailWithError: any Error)](vndocumentcameraviewcontrollerdelegate/documentcameraviewcontroller(_:didfailwitherror:).md)
  Tells the delegate that document scanning failed while the camera view controller was active.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Structuring Recognized Text on a Document](structuring_recognized_text_on_a_document.md)
  Detect, recognize, and structure text on a business card or receipt using Vision and VisionKit.
- [class VNDocumentCameraViewController](vndocumentcameraviewcontroller.md)
  An object that presents UI for a camera pass-through that helps people scan physical documents.
- [class VNDocumentCameraScan](vndocumentcamerascan.md)
  A single document scanned in the document camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/vndocumentcameraviewcontrollerdelegate)*