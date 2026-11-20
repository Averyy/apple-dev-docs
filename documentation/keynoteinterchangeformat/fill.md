# Fill

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

A style that fills an area with exactly one of a solid color, a gradient, or an image.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
(Fill.color | Fill.gradient | Fill.image) Fill
```

## Mentions

- [Understanding Keynote Interchange Format structure](./understanding-keynote-interchange-format-structure.md)



**Allowed Types**: `Fill.color`, `Fill.gradient`, `Fill.image`

## Discussion

This value takes one of the following forms:

- `color`: A solid color fill.
- `gradient`: A gradient fill, either linear or radial.
- `image`: An image fill, with optional scale and tint.

## Topics

### Objects
- [object Fill.Gradient](./fill.gradient.md)
  A fill with a continuous gradient between two or more colors.
- [object Fill.ImageFill](./fill.imagefill.md)
  An image that the reader uses to fill an area.
### Dictionaries
- [object Fill.color](./fill/color.md)
  A solid color fill.
- [object Fill.gradient](./fill/gradient.md)
  A gradient fill, either linear or radial.
- [object Fill.image](./fill/image.md)
  An image fill, with optional scale and tint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/fill)*