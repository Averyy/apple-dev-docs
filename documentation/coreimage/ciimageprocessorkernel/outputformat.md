# outputFormat

**Framework**: Core Image  
**Kind**: property

The processor’s output pixel format.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class var outputFormat: CIFormat { get }
```

#### Discussion

Override this class property if you want your processor’s output to be in a specific [`CIFormat`](ciformat.md): [`BGRA8`](ciformat/bgra8.md), [`RGBAh`](ciformat/rgbah.md), [`RGBAf`](ciformat/rgbaf.md), or [`R8`](ciformat/r8.md).  If the [`outputFormat`](ciimageprocessorkernel/outputformat.md) is 0, then the output will be a supported format that best matches the rendering context’s [`workingFormat`](cicontext/workingformat.md).

If a processor returns data in a colorspace other than the context working space, then call [`matchedToWorkingSpace(from:)`](ciimage/matchedtoworkingspace(from:).md) on the processor output.

If a processor returns data as alpha-unpremultiplied RGBA data, then call [`premultiplyingAlpha()`](ciimage/premultiplyingalpha().md) on the processor output.

## See Also

- [class var outputIsOpaque: Bool](ciimageprocessorkernel/outputisopaque.md)
  Boolean determining whether or not processor outputs an opaque image.
- [class var synchronizeInputs: Bool](ciimageprocessorkernel/synchronizeinputs.md)
  Tells whether or not processor input should be synchronized for CPU access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/outputformat)*