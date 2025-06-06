# init(requestRevision:boundingBox:)

**Framework**: Vision  
**Kind**: init

Creates an observation with a revision number and bounding box.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(requestRevision: Int, boundingBox: CGRect)
```

## Parameters

- `requestRevision`: The revision of the request to use.
- `boundingBox`: The observation’s bounding box, in coordinates normalized to the dimensions of the processed image, with its origin at the image’s lower-left corner.

## See Also

- [convenience init(boundingBox: CGRect)](vndetectedobjectobservation/init(boundingbox:).md)
  Creates an observation with a bounding box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetectedobjectobservation/init(requestrevision:boundingbox:))*