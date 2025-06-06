# allowDraftMode

**Framework**: Core Image  
**Kind**: structdata

A key for allowing draft mode. The associated value is a Boolean value packaged as an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object.  It’s best not to use draft mode if the image needs to be drawn without draft mode at a later time, because changing the value from [`true`](https://developer.apple.com/documentation/swift/true) to [`false`](https://developer.apple.com/documentation/swift/false) is an expensive operation. If the optional scale factor is smaller than a certain value, additionally setting draft mode can improve image decoding speed without any perceivable loss of quality. However, turning on draft mode does not have any effect if the scale factor is not below this threshold.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.5+ - Deprecated in 12.0
- tvOS 10.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
static let allowDraftMode: CIRAWFilterOption
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1438010-allowdraftmode)*