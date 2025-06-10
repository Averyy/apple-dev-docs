# isub_image

**Framework**: Kernel  
**Kind**: structp

The subimage in which the symbol is defined. It is an index into the list of images that make up the umbrella image. If this field is 0, the symbol is in the umbrella image itself. If the image is not an umbrella framework or library, this field is 0.

**Availability**:
- macOS 10.6+

## Declaration

```swift
uint32_t isub_image:8;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/twolevel_hint/1525623-isub_image)*