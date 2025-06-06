# cmpSize

**Framework**: Application Services  
**Kind**: structp

The size in bits of each component for a pixel.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var cmpSize: Int16
```

#### Discussion

Color QuickDraw expects that the sizes of all components are the same, and that the value of the `cmpCount` field multiplied by the value of the `cmpSize` field is less than or equal to the value in the `pixelSize` field.For an indexed pixel value, which has only one component, the value of the `cmpSize` field is the same as the value of the `pixelSize` field; that is, 1, 2, 4, or 8. For direct pixels there are two additional possibilities. A 16-bit pixel, which has three components, has a `cmpSize` value of 5; this leaves an unused high-order bit, which Color QuickDraw sets to 0. A 32-bit pixel, which has three components (red, green, and blue), has a `cmpSize` value of 8; this leaves an unused high-order byte, which Color QuickDraw sets to 0.

If presented with a 32-bit image (for example, in the `CopyBits` procedure) Color QuickDraw passes whatever bits are there, and it does not set the high byte to 0. Generally, therefore, your application should clear the memory for the image to 0 before creating a 16-bit or 32-bit image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/pixmap/1464685-cmpsize)*