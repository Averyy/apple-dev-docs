# USDLayer.OpenOptions

**Framework**: USDKit  
**Kind**: struct

Options for opening a layer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct OpenOptions
```

## Topics

### Initializers
- [init()](usdlayer/openoptions/init.md)
  Creates an empty option set.
- [init(arrayLiteral: USDLayer.OpenOptions...)](usdlayer/openoptions/init(arrayliteral:).md)
  Creates an option set from a sequence of options.
### Type Properties
- [static var createNew: USDLayer.OpenOptions](usdlayer/openoptions/createnew.md)
  Creates a new layer instead of opening an existing file. Any existing file at the identifier will be overwritten.

## Relationships

### Conforms To
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static func find(identifier: String) -> USDLayer?](usdlayer/find(identifier:).md)
  Returns an already-loaded layer with this identifier, or `nil` if none is loaded. Does no I/O.
- [static func open(String, options: USDLayer.OpenOptions) throws -> USDLayer](usdlayer/open(_:options:).md)
  Returns an already-loaded layer at the identifier, or opens it from the resolved asset path.
- [USDLayer.Permission](usdlayer/permission.md)
  Access permission for a spec.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/openoptions)*