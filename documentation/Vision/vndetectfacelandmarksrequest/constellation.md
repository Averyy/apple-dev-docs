# constellation

**Framework**: Vision  
**Kind**: property

A variable that describes how a face landmarks request orders or enumerates the resulting features.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var constellation: VNRequestFaceLandmarksConstellation { get set }
```

#### Discussion

Set this variable to one of the supported constellation types detailed in [`VNRequestFaceLandmarksConstellation`](vnrequestfacelandmarksconstellation.md). The default value is [`VNRequestFaceLandmarksConstellation.constellationNotDefined`](vnrequestfacelandmarksconstellation/constellationnotdefined.md).

## See Also

- [enum VNRequestFaceLandmarksConstellation](vnrequestfacelandmarksconstellation.md)
  An enumeration of face landmarks in a constellation object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetectfacelandmarksrequest/constellation)*