# USDLayer.OpenOptions

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

Options for opening a layer.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct OpenOptions
```

## Topics

### Initializers
- [init()](./openoptions/init%28%29.md)
  Creates an empty option set.
- [init(arrayLiteral: USDLayer.OpenOptions...)](./openoptions/init%28arrayliteral%29.md)
  Creates an option set from a sequence of options.
### Type Properties
- [static var createNew: USDLayer.OpenOptions](./openoptions/createnew.md)
  Creates a new layer instead of opening an existing file. Any existing file at the identifier will be overwritten.

## Relationships

### Conforms To
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Opening and finding layers
- [static func find(identifier: String) -> USDLayer?](./find%28identifier%29.md)
  Returns an already-loaded layer with this identifier, or `nil` if none is loaded. Does no I/O.
- [static func open(String, options: USDLayer.OpenOptions) throws -> USDLayer](./open%28_,options%29.md)
  Returns an already-loaded layer at the identifier, or opens it from the resolved asset path.
- [USDLayer.Permission](./permission.md)
  Access permission for a spec.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/openoptions)*