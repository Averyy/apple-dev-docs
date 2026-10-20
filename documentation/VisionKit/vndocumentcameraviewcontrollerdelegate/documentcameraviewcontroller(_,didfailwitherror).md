# documentCameraViewController(_:didFailWithError:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that document scanning failed while the camera view controller was active.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func documentCameraViewController(_ controller: VNDocumentCameraViewController, didFailWithError error: any Error)
```

```objc
- (void) documentCameraViewController:(VNDocumentCameraViewController *) controller didFailWithError:(NSError *) error;
```

## Parameters

- `controller`: The document camera view controller that failed.
- `error`: The error containing the reason for failure.

## See Also

### Determining scan results
- [func documentCameraViewController(VNDocumentCameraViewController, didFinishWith: VNDocumentCameraScan)](./documentcameraviewcontroller%28_,didfinishwith%29.md)
  Tells the delegate that the user successfully saved a scanned document from the document camera.
- [func documentCameraViewControllerDidCancel(VNDocumentCameraViewController)](./documentcameraviewcontrollerdidcancel%28_%29.md)
  Tells the delegate that the user canceled out of the document scanner camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/vndocumentcameraviewcontrollerdelegate/documentcameraviewcontroller(_:didfailwitherror:))*