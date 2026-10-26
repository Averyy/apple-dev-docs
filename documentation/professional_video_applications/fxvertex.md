# FxVertex

**Framework**: Professional Video Applications  
**Kind**: struct  
**Role**: Structure

The properties of one vertex in a path.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
struct FxVertex
```

```c
typedef struct FxVertex { ... } FxVertex;
```

## Topics

### Instance Properties
- [var location: FxPoint2D](./fxvertex/location.md)
  The location of the point in the 2D image.
- [var inTangent: FxPoint2D](./fxvertex/intangent.md)
  The x and y vectors of the incoming tangent.
- [var interpStyle: FxPathStyle](./fxvertex/interpstyle.md)
  The style of interpolation at this vertex.
- [var location: FxPoint2D](./fxvertex/location.md)
  The location of the point in the 2D image.
- [var outTangent: FxPoint2D](./fxvertex/outtangent.md)
  The x and y vectors of the outgoing tangent.
- [var xSplineWeight: Double](./fxvertex/xsplineweight.md)
  The weight of the x-spline at this point.
- [var interpStyle: FxPathStyle](./fxvertex/interpstyle.md)
  The style of interpolation at this vertex.
### Initializers
- [init()](./fxvertex/init%28%29.md)
- [init(location: FxPoint2D, inTangent: FxPoint2D, outTangent: FxPoint2D, xSplineWeight: Double, interpStyle: FxPathStyle)](./fxvertex/init%28location,intangent,outtangent,xsplineweight,interpstyle%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Structuring Path Information
- [struct FxPathGeometryInfo](./fxpathgeometryinfo.md)
  A structure that defines the geometry information of the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxvertex)*