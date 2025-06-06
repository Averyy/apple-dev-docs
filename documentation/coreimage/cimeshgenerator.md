# CIMeshGenerator

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a mesh generator filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIMeshGenerator
```

## Topics

### Instance Properties
- [var color: CIColor](cimeshgenerator/3228559-color.md)
  The color of the rendered mesh.
- [var mesh: [Any]](cimeshgenerator/3228560-mesh.md)
  An array that describes the mesh to render.
- [var width: Float](cimeshgenerator/3228561-width.md)
  The width of the effect.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func meshGenerator() -> any CIFilter & CIMeshGenerator](cifilter/3228359-meshgenerator.md)
  Generates a pattern made from an array of line segments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cimeshgenerator)*