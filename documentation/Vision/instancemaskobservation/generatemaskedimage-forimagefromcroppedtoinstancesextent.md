# generateMaskedImage(for:imageFrom:croppedToInstancesExtent:)

**Framework**: Vision  
**Kind**: method

Creates a high-resolution image with everything except for the instances you specify masked out.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func generateMaskedImage(for instances: IndexSet, imageFrom requestHandler: ImageRequestHandler, croppedToInstancesExtent: Bool = false) throws -> CVPixelBuffer
```

#### Return Value

The pixel buffer that contains the image.

#### Discussion

## Parameters

- `instances`: An indexed set of selected instances, where   is the background.
- `requestHandler`: A request handler containing an image to be masked.
- `croppedToInstancesExtent`: Crops the image to the smallest rectangle containing all instances. Default is  .

## See Also

- [func generateMask(for: IndexSet) throws -> CVPixelBuffer](instancemaskobservation/generatemask(for:).md)
  Creates a low-resolution mask from the instances you specify.
- [func generateScaledMask(for: IndexSet, scaledToImageFrom: ImageRequestHandler) throws -> CVPixelBuffer](instancemaskobservation/generatescaledmask(for:scaledtoimagefrom:).md)
  Creates a high-resolution mask representing a combination of the instances you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/instancemaskobservation/generatemaskedimage(for:imagefrom:croppedtoinstancesextent:))*