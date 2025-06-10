# apply(extent:arguments:)

**Framework**: Core Image  
**Kind**: method

Creates a new image using the kernel and specified arguments.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func apply(extent: CGRect, arguments args: [Any]) -> CIImage?
```

#### Return Value

A new image object describing the result of applying the kernel.

#### Discussion

This method is analogous to the [`CIFilter`](cifilter-swift.class.md) method [`apply(_:arguments:options:)`](cifilter-swift.class/apply(_:arguments:options:).md), but it does not require construction of a [`CIFilter`](cifilter-swift.class.md) object, and it allows you to specify a callback for determining the kernel’s region of interest as a block or closure. As with the similar [`CIFilter`](cifilter-swift.class.md) method, calling this method does not execute the kernel code—filters and their kernel code are evaluated only when rendering a final output image.

## Parameters

- `extent`: The extent of the output image.
- `args`: An array of arguments to pass to the kernel routine. The type of each object in the array must be compatible with the corresponding parameter declared in the kernel routine source code. For details, see  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolorkernel/apply(extent:arguments:))*