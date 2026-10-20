# VNDocumentCameraViewControllerDelegate

**Framework**: VisionKit  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol VNDocumentCameraViewControllerDelegate <NSObject>
```

#### Overview

Your app is responsible for dismissing the document camera in all delegate callback methods.

## Topics

### Determining scan results
- [func documentCameraViewController(VNDocumentCameraViewController, didFinishWith: VNDocumentCameraScan)](./vndocumentcameraviewcontrollerdelegate/documentcameraviewcontroller%28_,didfinishwith%29.md)
  Tells the delegate that the user successfully saved a scanned document from the document camera.
- [func documentCameraViewControllerDidCancel(VNDocumentCameraViewController)](./vndocumentcameraviewcontrollerdelegate/documentcameraviewcontrollerdidcancel%28_%29.md)
  Tells the delegate that the user canceled out of the document scanner camera.
- [func documentCameraViewController(VNDocumentCameraViewController, didFailWithError: any Error)](./vndocumentcameraviewcontrollerdelegate/documentcameraviewcontroller%28_,didfailwitherror%29.md)
  Tells the delegate that document scanning failed while the camera view controller was active.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Document scanning through the camera
- [Structuring recognized text on a document](./structuring-recognized-text-on-a-document.md)
  Detect, recognize, and structure text on a business card or receipt using Vision and VisionKit.
- [class VNDocumentCameraViewController](./vndocumentcameraviewcontroller.md)
  An object that presents UI for a camera pass-through that helps people scan physical documents.
- [class VNDocumentCameraScan](./vndocumentcamerascan.md)
  A single document scanned in the document camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/vndocumentcameraviewcontrollerdelegate)*