# Table.VisualProperties.StrokePreset.Edge

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

An edge of the stroked range that a stroke preset can turn on.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
string Table.VisualProperties.StrokePreset.Edge
```

## Discussion

The four outer edges are stroked with `exterior_stroke`; the two interior cases are stroked with `horizontal_stroke` and `vertical_stroke`.

This value takes one of the following forms:

- `bottom`: Outer bottom edge.
- `horizontal`: Interior horizontal gridlines (between rows).
- `left`: Outer left edge.
- `right`: Outer right edge.
- `top`: Outer top edge.
- `vertical`: Interior vertical gridlines (between columns). Shown in Keynote as “Center borders.”


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.visualproperties.strokepreset.edge)*