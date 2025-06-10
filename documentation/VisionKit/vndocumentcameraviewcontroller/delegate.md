# delegate

**Framework**: VisionKit  
**Kind**: property

The delegate to be notified when the user saves or cancels the document scanner.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any VNDocumentCameraViewControllerDelegate)? { get set }
```

#### Overview

The delegate receives one of the following three calls:

- [`documentCameraViewController(_:didFinishWith:)`](vndocumentcameraviewcontrollerdelegate/documentcameraviewcontroller(_:didfinishwith:).md) when the camera successfully completes a scan.
- [`documentCameraViewControllerDidCancel(_:)`](vndocumentcameraviewcontrollerdelegate/documentcameraviewcontrollerdidcancel(_:).md) when the user cancels out of the document camera interface.
- [`documentCameraViewController(_:didFailWithError:)`](vndocumentcameraviewcontrollerdelegate/documentcameraviewcontroller(_:didfailwitherror:).md) when the document scan fails or is unable to capture a photo.

Your app is responsible for dismissing the document camera in all delegate methods.

## See Also

- [class var isSupported: Bool](vndocumentcameraviewcontroller/issupported.md)
  A Boolean variable that indicates whether or not the current device supports document scanning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/vndocumentcameraviewcontroller/delegate)*