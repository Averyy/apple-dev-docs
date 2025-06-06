# outputFormat

**Framework**: Core Image  
**Kind**: cldata

The processor's output pixel format.

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

Override this class property if you want your processor's output to be in a specific [`CIFormat`](ciformat.md): [`BGRA8`](ciformat/1438064-bgra8.md), [`RGBAh`](ciformat/1437998-rgbah.md), [`RGBAf`](ciformat/1437756-rgbaf.md), or [`R8`](ciformat/1437695-r8.md).  If the [`outputFormat`](ciimageprocessorkernel/2143065-outputformat.md) is 0, then the output will be a supported format that best matches the rendering context's [`workingFormat`](cicontext/1642215-workingformat.md).

If a processor returns data in a colorspace other than the context working space, then call [`matchedToWorkingSpace(from:)`](ciimage/1645896-matchedtoworkingspace.md) on the processor output. 

If a processor returns data as alpha-unpremultiplied RGBA data, then call [`premultiplyingAlpha()`](ciimage/1645894-premultiplyingalpha.md) on the processor output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/2143065-outputformat)*