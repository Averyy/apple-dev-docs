# nearestSampling

**Framework**: Core Image  
**Kind**: structdata

The key into the properties dictionary to indicate whether to use nearest-neighbor sampling.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static let nearestSampling: CIImageOption
```

#### Discussion

The value for this key is an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) containing a Boolean value specifying whether the image should be sampled using nearest neighbor behavior.  An unspecified value defaults to linear sampling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageoption/2867426-nearestsampling)*