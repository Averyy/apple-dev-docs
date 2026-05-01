# documentCameraViewController(_:didFinishWith:)

**Framework**: VisionKit  
**Kind**: method

Tells the delegate that the user successfully saved a scanned document from the document camera.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func documentCameraViewController(_ controller: VNDocumentCameraViewController, didFinishWith scan: VNDocumentCameraScan)
```

## Parameters

- `controller`: The document camera view controller that captured the scan.
- `scan`: The scanned document that the camera detected.

## See Also

- [func documentCameraViewControllerDidCancel(VNDocumentCameraViewController)](vndocumentcameraviewcontrollerdelegate/documentcameraviewcontrollerdidcancel(_:).md)
  Tells the delegate that the user canceled out of the document scanner camera.
- [func documentCameraViewController(VNDocumentCameraViewController, didFailWithError: any Error)](vndocumentcameraviewcontrollerdelegate/documentcameraviewcontroller(_:didfailwitherror:).md)
  Tells the delegate that document scanning failed while the camera view controller was active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/vndocumentcameraviewcontrollerdelegate/documentcameraviewcontroller(_:didfinishwith:))*