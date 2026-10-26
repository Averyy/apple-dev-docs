# FxPathGeometryInfo

**Framework**: Professional Video Applications  
**Kind**: struct  
**Role**: Structure

A structure that defines the geometry information of the path.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
struct FxPathGeometryInfo
```

```c
typedef struct FxPathGeometryInfo { ... } FxPathGeometryInfo;
```

## Topics

### Instance Properties
- [var curvature: Double](./fxpathgeometryinfo/curvature.md)
  The curvature of the ellipse, if applicable.
- [var radius: FxPoint2D](./fxpathgeometryinfo/radius.md)
  The radius of the ellipse, if applicable.
- [var size: FxPoint2D](./fxpathgeometryinfo/size.md)
  The size of the rectangle, if applicable.
- [var transform: Unmanaged<FxMatrix44>!](./fxpathgeometryinfo/transform.md)
  The shape’s transformation matrix.
### Initializers
- [init()](./fxpathgeometryinfo/init%28%29.md)
- [init(curvature: Double, radius: FxPoint2D, size: FxPoint2D, transform: Unmanaged<FxMatrix44>!)](./fxpathgeometryinfo/init%28curvature,radius,size,transform%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### Structuring Path Information
- [struct FxVertex](./fxvertex.md)
  The properties of one vertex in a path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxpathgeometryinfo)*