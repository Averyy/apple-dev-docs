# generateMask(forInstances:)

**Framework**: Vision  
**Kind**: method

Creates a low-resolution mask from the instances you specify.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func generateMask(forInstances instances: IndexSet) throws -> CVPixelBuffer
```

#### Return Value

The pixel buffer that contains the image.

## Parameters

- `instances`: The collection of instances.

## See Also

- [func generateMaskedImage(ofInstances: IndexSet, from: VNImageRequestHandler, croppedToInstancesExtent: Bool) throws -> CVPixelBuffer](vninstancemaskobservation/generatemaskedimage(ofinstances:from:croppedtoinstancesextent:).md)
  Creates a high-resolution image where everything becomes transparent black, except for the instances you specify.
- [func generateScaledMaskForImage(forInstances: IndexSet, from: VNImageRequestHandler) throws -> CVPixelBuffer](vninstancemaskobservation/generatescaledmaskforimage(forinstances:from:).md)
  Creates a high-resolution mask where everything becomes transparent black, except for the instances you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vninstancemaskobservation/generatemask(forinstances:))*