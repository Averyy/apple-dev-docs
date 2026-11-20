# Paragraph.Constituent

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

An element of a paragraph’s contents.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
(Paragraph.Constituent.hyperlink | Paragraph.Constituent.inline_object | Paragraph.Constituent.run) Paragraph.Constituent
```



**Allowed Types**: `Paragraph.Constituent.hyperlink`, `Paragraph.Constituent.inline_object`, `Paragraph.Constituent.run`

## Discussion

Each element is a run of text, an inline object, or a link.

This value takes one of the following forms:

- `hyperlink`: A link.
- `inline_object`: An inline object. An object that can’t be imported (for example, a movie the device can’t play) isn’t dropped on its own. In the text of a text box or shape, the whole text box or shape is removed, including all of its text; in a slide’s presenter notes, such an object stops the document from loading.
- `run`: A run of text in the same style.

## Topics

### Dictionaries
- [object Paragraph.Constituent.hyperlink](./paragraph.constituent/hyperlink.md)
  A link.
- [object Paragraph.Constituent.inline_object](./paragraph.constituent/inline_object.md)
  An inline object.
- [object Paragraph.Constituent.run](./paragraph.constituent/run.md)
  A run of text in the same style.

## See Also

### Enumerations
- [type Paragraph.BreakType](./paragraph.breaktype.md)
  The break that ends a paragraph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/paragraph.constituent)*