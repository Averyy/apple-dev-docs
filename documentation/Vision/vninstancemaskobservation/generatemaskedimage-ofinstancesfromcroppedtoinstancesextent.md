# generateMaskedImage(ofInstances:from:croppedToInstancesExtent:)

**Framework**: Vision  
**Kind**: method

Creates a high-resolution image where everything becomes transparent black, except for the instances you specify.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func generateMaskedImage(ofInstances instances: IndexSet, from requestHandler: VNImageRequestHandler, croppedToInstancesExtent cropResult: Bool) throws -> CVPixelBuffer
```

#### Return Value

The pixel buffer that contains the image.

## Parameters

- `instances`: The collection of instances.
- `requestHandler`: The image request callback.
- `cropResult`: A Boolean value that indicates whether to crop the image to the smallest rectangle that contains all instances.

## See Also

- [func generateMask(forInstances: IndexSet) throws -> CVPixelBuffer](vninstancemaskobservation/generatemask(forinstances:).md)
  Creates a low-resolution mask from the instances you specify.
- [func generateScaledMaskForImage(forInstances: IndexSet, from: VNImageRequestHandler) throws -> CVPixelBuffer](vninstancemaskobservation/generatescaledmaskforimage(forinstances:from:).md)
  Creates a high-resolution mask where everything becomes transparent black, except for the instances you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vninstancemaskobservation/generatemaskedimage(ofinstances:from:croppedtoinstancesextent:))*