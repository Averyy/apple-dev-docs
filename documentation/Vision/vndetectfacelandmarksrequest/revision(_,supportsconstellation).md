# revision(_:supportsConstellation:)

**Framework**: Vision  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (BOOL) revision:(NSUInteger) requestRevision supportsConstellation:(VNRequestFaceLandmarksConstellation) constellation;
```

#### Return Value

[`true`](../../Swift/true.md) if the revision supports the constellation, otherwise [`false`](../../Swift/false.md).

## Parameters

- `requestRevision`: The revision of the request.
- `constellation`: The contellation for which to determine support.

## See Also

### Identifying Request Revisions
- [var VNDetectFaceLandmarksRequestRevision3: Int](../vndetectfacelandmarksrequestrevision3.md)
  A constant for specifying revision 3 of the face landmarks detection request.
- [var VNDetectFaceLandmarksRequestRevision2: Int](../vndetectfacelandmarksrequestrevision2.md)
  A constant for specifying revision 2 of the face landmarks detection request.
- [var VNDetectFaceLandmarksRequestRevision1: Int](../vndetectfacelandmarksrequestrevision1.md)
  A constant for specifying revision 1 of the face landmarks detection request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetectfacelandmarksrequest/revision(_:supportsconstellation:))*