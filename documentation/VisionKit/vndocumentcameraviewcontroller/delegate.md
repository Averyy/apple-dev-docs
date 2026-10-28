# delegate

**Framework**: VisionKit  
**Kind**: property  
**Role**: Instance Property

The delegate to be notified when the user saves or cancels the document scanner.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any VNDocumentCameraViewControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<VNDocumentCameraViewControllerDelegate> delegate;
```

## Overview

The delegate receives one of the following three calls:

- [`documentCameraViewController(_:didFinishWith:)`](../vndocumentcameraviewcontrollerdelegate/documentcameraviewcontroller%28_,didfinishwith%29.md) when the camera successfully completes a scan.
- [`documentCameraViewControllerDidCancel(_:)`](../vndocumentcameraviewcontrollerdelegate/documentcameraviewcontrollerdidcancel%28_%29.md) when the user cancels out of the document camera interface.
- [`documentCameraViewController(_:didFailWithError:)`](../vndocumentcameraviewcontrollerdelegate/documentcameraviewcontroller%28_,didfailwitherror%29.md) when the document scan fails or is unable to capture a photo.

Your app is responsible for dismissing the document camera in all delegate methods.

## See Also

### Supporting the document camera
- [class var isSupported: Bool](./issupported.md)
  A Boolean variable that indicates whether or not the current device supports document scanning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/vndocumentcameraviewcontroller/delegate)*