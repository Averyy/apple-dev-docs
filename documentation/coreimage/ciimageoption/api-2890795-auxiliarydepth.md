# auxiliaryDepth

**Framework**: Core Image  
**Kind**: structdata

The key into the properties dictionary indicating whether to return an auxiliary depth image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static let auxiliaryDepth: CIImageOption
```

#### Discussion

The value of this key is an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) containing a Boolean [`true`](https://developer.apple.com/documentation/swift/true) or [`false`](https://developer.apple.com/documentation/swift/false).  If the value is [`true`](https://developer.apple.com/documentation/swift/true), then calls to [`imageWithContentsOfURL:options:`](ciimage/1546997-imagewithcontentsofurl.md) and [`imageWithData:options:`](ciimage/1547016-imagewithdata.md) will return the auxiliary image as a half-float monochrome image instead of the primary image, or [`nil`](https://developer.apple.com/documentation/objectivec/nil-2gl) if no auxiliary image exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageoption/2890795-auxiliarydepth)*