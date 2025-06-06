# salientObjects

**Framework**: Vision  
**Kind**: property

A collection of objects describing the distinct areas of the saliency heat map.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var salientObjects: [VNRectangleObservation]? { get }
```

#### Discussion

The objects in this array don’t follow any specific ordering. It’s up to your app to iterate across the observations and apply desired ordering.

Requesting this array lazily computes the bounds of salient objects within the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnsaliencyimageobservation/salientobjects)*