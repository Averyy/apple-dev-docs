# pointsInImageOfSize:

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

A buffer in memory containing landmark points in the coordinate space of the specified image size.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```objc
- (const CGPoint *) pointsInImageOfSize:(CGSize) imageSize;
```

#### Return Value

A pointer to a buffer containing a [`CGPoint`](../../CoreFoundation/cgpoint.md) for each landmark detected in the image, expressed in the coordinate space of the specified image size.

## Parameters

- `imageSize`: The pixel dimensions of the image in which to present landmark points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnfacelandmarkregion2d/pointsinimageofsize:)*