# documentCameraViewControllerDidCancel(_:)

**Framework**: VisionKit  
**Kind**: method

Tells the delegate that the user canceled out of the document scanner camera.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func documentCameraViewControllerDidCancel(_ controller: VNDocumentCameraViewController)
```

## Parameters

- `controller`: The document camera view controller in which the user canceled.

## See Also

- [func documentCameraViewController(VNDocumentCameraViewController, didFinishWith: VNDocumentCameraScan)](vndocumentcameraviewcontrollerdelegate/documentcameraviewcontroller(_:didfinishwith:).md)
  Tells the delegate that the user successfully saved a scanned document from the document camera.
- [func documentCameraViewController(VNDocumentCameraViewController, didFailWithError: any Error)](vndocumentcameraviewcontrollerdelegate/documentcameraviewcontroller(_:didfailwitherror:).md)
  Tells the delegate that document scanning failed while the camera view controller was active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/vndocumentcameraviewcontrollerdelegate/documentcameraviewcontrollerdidcancel(_:))*