# documentCameraViewController(_:didFinishWith:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) documentCameraViewController:(VNDocumentCameraViewController *) controller didFinishWithScan:(VNDocumentCameraScan *) scan;
```

## Parameters

- `controller`: The document camera view controller that captured the scan.
- `scan`: The scanned document that the camera detected.

## See Also

### Determining scan results
- [func documentCameraViewControllerDidCancel(VNDocumentCameraViewController)](./documentcameraviewcontrollerdidcancel%28_%29.md)
  Tells the delegate that the user canceled out of the document scanner camera.
- [func documentCameraViewController(VNDocumentCameraViewController, didFailWithError: any Error)](./documentcameraviewcontroller%28_,didfailwitherror%29.md)
  Tells the delegate that document scanning failed while the camera view controller was active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/vndocumentcameraviewcontrollerdelegate/documentcameraviewcontroller(_:didfinishwith:))*