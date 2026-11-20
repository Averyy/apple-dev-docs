# Stroke

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

A stroke drawn along a path, such as a border around an object.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
(Stroke.frame | Stroke.line | string("empty")) Stroke
```

## Mentions

- [Understanding Keynote Interchange Format structure](./understanding-keynote-interchange-format-structure.md)



**Allowed Types**: `Stroke.frame`, `Stroke.line`, `string("empty")`

## Discussion

The stroke is a line or a picture frame, or `empty` for no stroke or border.

This value takes one of the following forms:

- `empty`: No stroke or border.
- `frame`: A border drawn as a rectangular picture frame.
- `line`: A stroke or border drawn as a line in one of several styles.

## Topics

### Objects
- [object Stroke.Frame](./stroke.frame.md)
  A picture frame drawn around an object as its border.
- [object Stroke.Line](./stroke.line.md)
  A stroke or border that the reader draws as a line in one of several styles.
### Dictionaries
- [object Stroke.frame](./stroke/frame.md)
  A border drawn as a rectangular picture frame.
- [object Stroke.line](./stroke/line.md)
  A stroke or border drawn as a line in one of several styles.

## See Also

### Shapes
- [object Shape](./shape.md)
  A path with a fill and a stroke.
- [object Rect](./rect.md)
  An axis-aligned rectangle in whichever coordinate space the property using it defines.
- [object Path](./path.md)
  A path that traces the outline of a shape or of an image’s mask.
- [object ConnectionLine](./connectionline.md)
  A line drawn from its tail end to its head end, each of which can attach to another object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/stroke)*