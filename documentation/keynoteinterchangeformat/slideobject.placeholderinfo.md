# SlideObject.PlaceholderInfo

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The placeholder an object acts as on its slide.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
(SlideObject.PlaceholderInfo.defined | SlideObject.PlaceholderInfo.tagged) SlideObject.PlaceholderInfo
```



**Allowed Types**: `SlideObject.PlaceholderInfo.defined`, `SlideObject.PlaceholderInfo.tagged`

## Discussion

It’s either one of the predefined placeholders that a layout can turn on and off, or a placeholder identified by a custom tag.

This value takes one of the following forms:

- `defined`: One of the predefined placeholders that someone can turn on and off on any slide.
- `tagged`: A placeholder that has a tag associated with it. It can be an image, a movie, a shape, or a text box.

## Topics

### Objects
- [object SlideObject.PlaceholderInfo.PlaceholderDefinition](./slideobject.placeholderinfo.placeholderdefinition.md)
  The predefined placeholder an object fills.
### Dictionaries
- [object SlideObject.PlaceholderInfo.defined](./slideobject.placeholderinfo/defined.md)
  One of the predefined placeholders that someone can turn on and off on any slide.
- [object SlideObject.PlaceholderInfo.tagged](./slideobject.placeholderinfo/tagged.md)
  A placeholder that has a tag associated with it. It can be an image, a movie, a shape, or a text box.

## See Also

### Enumerations
- [type SlideObject.SourceKind](./slideobject.sourcekind.md)
  The source of an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/slideobject.placeholderinfo)*