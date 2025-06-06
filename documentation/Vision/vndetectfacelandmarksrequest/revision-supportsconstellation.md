# revision(_:supportsConstellation:)

**Framework**: Vision  
**Kind**: method

Returns a Boolean value that indicates whether a revision supports a constellation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class func revision(_ requestRevision: Int, supportsConstellation constellation: VNRequestFaceLandmarksConstellation) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the revision supports the constellation, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `requestRevision`: The revision of the request.
- `constellation`: The contellation for which to determine support.

## See Also

- [let VNDetectFaceLandmarksRequestRevision3: Int](vndetectfacelandmarksrequestrevision3.md)
  A constant for specifying revision 3 of the face landmarks detection request.
- [let VNDetectFaceLandmarksRequestRevision2: Int](vndetectfacelandmarksrequestrevision2.md)
  A constant for specifying revision 2 of the face landmarks detection request.
- [let VNDetectFaceLandmarksRequestRevision1: Int](vndetectfacelandmarksrequestrevision1.md)
  A constant for specifying revision 1 of the face landmarks detection request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetectfacelandmarksrequest/revision(_:supportsconstellation:))*