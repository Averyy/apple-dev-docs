# ListLabelType

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The kind of label shown at a list level.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
(ListLabelType.image | ListLabelType.number | ListLabelType.string | string("none" | "null_image")) ListLabelType
```



**Allowed Types**: `ListLabelType.image`, `ListLabelType.number`, `ListLabelType.string`, `string("none" | "null_image")`

## Discussion

The `string` and `image` cases carry the label’s content, size, and offset; `number` carries a numbering format and size; and `none` and `null_image` carry no value.

This value takes one of the following forms:

- `image`: An image label.
- `none`: No bullet or label for this level.
- `null_image`: An image label whose image is missing. Nothing is drawn for the level, which still counts as labeled rather than as `none`.
- `number`: A number label.
- `string`: A text bullet.

## Topics

### Objects
- [object ListLabelType.ListImageLabel](./listlabeltype.listimagelabel.md)
  An image bullet.
- [object ListLabelType.ListNumberLabel](./listlabeltype.listnumberlabel.md)
  A numbered list label.
- [object ListLabelType.ListStringLabel](./listlabeltype.liststringlabel.md)
  A text list label, such as a bullet character or a short string.
### Dictionaries
- [object ListLabelType.image](./listlabeltype/image.md)
  An image label.
- [object ListLabelType.number](./listlabeltype/number.md)
  A number label.
- [object ListLabelType.string](./listlabeltype/string.md)
  A text bullet.

## See Also

### Lists
- [object ListLevelType](./listleveltype.md)
  One nesting level of a list style.
- [object ListProperties](./listproperties.md)
  The properties of a list style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/listlabeltype)*