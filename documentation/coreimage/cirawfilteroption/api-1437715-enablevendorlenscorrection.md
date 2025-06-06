# enableVendorLensCorrection

**Framework**: Core Image  
**Kind**: structdata

A key for whether to automatically correct for image distortion from known lenses.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.10+ - Deprecated in 12.0
- tvOS 10.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
static let enableVendorLensCorrection: CIRAWFilterOption
```

#### Discussion

The value for this key is a [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object containing a Boolean value. If this value is [`true`](https://developer.apple.com/documentation/swift/true), or if this option is not specified but the image contains metadata for lens distortion parameters, Core Image corrects for lens distortion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1437715-enablevendorlenscorrection)*