# bounds

**Framework**: Core Image  
**Kind**: property

A rectangle that indicates the position and extent of the QR code feature in image coordinates.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var bounds: CGRect { get }
```

#### Discussion

This property identifies the rectangular region of the image containing the detected QR code, not necessarily the shape of the QR code. A detected feature is square in space, but may appear as a four-sided polygon in the image. Use the properties listed in `CIQRCodeFeature` to find the corners of the QR code as it appears in perspective.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/bounds-swift.property)*