# workingFormat

**Framework**: Core Image  
**Kind**: structdata

An option for the color format to use for intermediate results when rendering with the context.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let workingFormat: CIContextOption
```

#### Discussion

The value for this key is an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object containing a [`CIFormat`](ciformat.md) value. The default working format is [`RGBA8`](ciformat/1438063-rgba8.md) for CPU rendering and [`RGBAf`](ciformat/1437756-rgbaf.md) for GPU rendering. For greater color precision, GPU rendering also supports the [`RGBAh`](ciformat/1437998-rgbah.md) format, but this format requires twice as much memory and can be used only with color management enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontextoption/1437788-workingformat)*