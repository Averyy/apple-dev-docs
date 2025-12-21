# mesh

**Framework**: Core Image  
**Kind**: property  
**Required**: Yes

An array that describes the mesh to render.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var mesh: [Any] { get set }
```

#### Discussion

Specify the mesh as an array of line segments. Each line segment is stored as a [`CIVector`](civector.md) instance that describes the line as a start point and an end point.

## See Also

- [var color: CIColor](cimeshgenerator/color.md)
  The color of the rendered mesh.
- [var width: Float](cimeshgenerator/width.md)
  The width of the effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cimeshgenerator/mesh)*