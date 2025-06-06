# isSupported

**Framework**: Visionkit  
**Kind**: property

A Boolean variable that indicates whether or not the current device supports document scanning.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class var isSupported: Bool { get }
```

#### Discussion

This class method returns `false` for unsupported hardware.

## See Also

- [var delegate: (any VNDocumentCameraViewControllerDelegate)?](vndocumentcameraviewcontroller/delegate.md)
  The delegate to be notified when the user saves or cancels the document scanner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/vndocumentcameraviewcontroller/issupported)*