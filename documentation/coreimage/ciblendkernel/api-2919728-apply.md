# apply(foreground:background:)

**Framework**: Core Image  
**Kind**: instm

Creates a new image using the blend kernel and specified foreground and background images.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func apply(foreground: CIImage, background: CIImage) -> CIImage?
```

#### Return_value

A [`CIImage`](ciimage.md) blending the foreground and background images.  Its extent will be the union of the foreground and background image extents.

#### Discussion

The foreground and background images are not treated differently in the blending.  You can think of them as equivalents A and B; the foreground is not given any precedence over the background.

## Parameters

- `foreground`: The first input image to be blended
- `background`: The second input image to be blended


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciblendkernel/2919728-apply)*