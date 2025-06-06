# formatForInput(at:)

**Framework**: Core Image  
**Kind**: clm

Method to override for returning the image processing kernel's input pixel format.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func formatForInput(at input: Int32) -> CIFormat
```

#### Return_value

Core Image pixel format [`CIFormat`](ciformat.md) constant revealing the processor's input pixel format.

#### Discussion

Override this method and the [`outputFormat`](ciimageprocessorkernel/2143065-outputformat.md) property getter to customize your processor's input and output pixel format.  

The format must be one of [`CIFormat`](ciformat.md): [`BGRA8`](ciformat/1438064-bgra8.md), [`RGBAh`](ciformat/1437998-rgbah.md), [`RGBAf`](ciformat/1437756-rgbaf.md), or [`R8`](ciformat/1437695-r8.md).  If the [`outputFormat`](ciimageprocessorkernel/2143065-outputformat.md) is 0, then the output will be a supported format that best matches the rendering context's [`workingFormat`](cicontext/1642215-workingformat.md).

## Parameters

- `input`: Index of this image processor in a multi-step workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/2138289-formatforinput)*