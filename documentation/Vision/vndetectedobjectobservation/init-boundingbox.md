# init(boundingBox:)

**Framework**: Vision  
**Kind**: init

Creates an observation with a bounding box.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(boundingBox: CGRect)
```

## Parameters

- `boundingBox`: The observation’s bounding box, in coordinates normalized to the dimensions of the processed image, with its origin at the image’s lower-left corner.

## See Also

- [convenience init(requestRevision: Int, boundingBox: CGRect)](vndetectedobjectobservation/init(requestrevision:boundingbox:).md)
  Creates an observation with a revision number and bounding box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetectedobjectobservation/init(boundingbox:))*