# apply(extent:roiCallback:arguments:)

**Framework**: Core Image  
**Kind**: instm

Creates a new image using the kernel and specified arguments.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func apply(extent: CGRect, roiCallback callback: @escaping CIKernelROICallback, arguments args: [Any]) -> CIImage?
```

#### Return_value

A new image object describing the result of applying the kernel.

#### Discussion

This method is analogous to the [`CIFilter`](cifilter.md) method [`apply(_:arguments:options:)`](cifilter/1438077-apply.md), but it does not require construction of a [`CIFilter`](cifilter.md) object, and it allows you to specify a callback for determining the kernel’s region of interest as a block or closure. As with the similar [`CIFilter`](cifilter.md) method, calling this method does not execute the kernel code—filters and their kernel code are evaluated only when rendering a final output image.

When applying a filter kernel, the region of interest (ROI) is the area of source image pixels that must be processed to produce a given area of destination image pixels. For a more detailed definition, see [`The Region of Interest`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_advanced_concepts/ci.advanced_concepts.html#//apple_ref/doc/uid/TP30001185-CH9-SW12). Core Image calls your `callback` block or closure to determine the ROI when rendering the filter output. Core Image automatically splits large images into smaller tiles for rendering, so your callback may be called multiple times.

## Parameters

- `extent`: The extent of the output image.
- `callback`: A block or closure that computes the region of interest for a given rectangle of destination image pixels. See  .
- `args`: An array of arguments to pass to the kernel routine. The type of each object in the array must be compatible with the corresponding parameter declared in the kernel routine source code. For details, see  .

## See Also

- [typealias CIKernelROICallback](cikernelroicallback.md)
  The signature for a block that computes the region of interest (ROI) for a given area of destination image pixels. Core Image calls this block when applying the kernel. You specify this block when using the [`apply(extent:roiCallback:arguments:)`](cikernel/1438243-apply.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cikernel/1438243-apply)*