# setImage(_:dirtyRect:)

**Framework**: Core Image  
**Kind**: instm

Updates an image accumulator with a subregion of an image object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setImage(_ image: CIImage, dirtyRect: CGRect)
```

#### Discussion

For additional details on using this method, see “Imaging Dynamical Systems” in [`Core Image Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185). 

## Parameters

- `im`: The image object whose contents you want to assign to the image accumulator.
- `r`: A rectangle that defines the subregion of the image object that’s changed since the last time you updated the image accumulator. You must guarantee that the new contents differ from the old only within the region specified by the this argument.

## See Also

- [func setImage(CIImage)](ciimageaccumulator/1427702-setimage.md)
  Sets the contents of the image accumulator to the contents of the specified image object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427706-setimage)*