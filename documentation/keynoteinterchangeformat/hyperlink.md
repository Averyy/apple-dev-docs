# Hyperlink

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

A clickable link attached to text.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
(Hyperlink.file | Hyperlink.program | Hyperlink.slide_jump | Hyperlink.url) Hyperlink
```



**Allowed Types**: `Hyperlink.file`, `Hyperlink.program`, `Hyperlink.slide_jump`, `Hyperlink.url`

## Discussion

The target is a URL, a jump to another slide in the same presentation, a file, or an opaque program action.

This value takes one of the following forms:

- `file`: A relative or absolute file path or a file URL.
- `program`: An opaque action. The recognized value is `exit_slideshow`, which exits the slideshow. Keynote preserves unrecognized values verbatim and produces a warning on import.
- `slide_jump`: A jump to another slide in the same presentation.
- `url`: An absolute URL with any scheme other than `file:`, such as `https://...`, `mailto:...`, `tel:+...`, or `keynote://...`.

## Topics

### Enumerations
- [object Hyperlink.SlideTarget](./hyperlink.slidetarget.md)
  A target slide inside the same presentation, given either by identifier or by position.
### Dictionaries
- [object Hyperlink.file](./hyperlink/file.md)
  A relative or absolute file path or a file URL.
- [object Hyperlink.program](./hyperlink/program.md)
  An opaque action.
- [object Hyperlink.slide_jump](./hyperlink/slide_jump.md)
  A jump to another slide in the same presentation.
- [object Hyperlink.url](./hyperlink/url.md)
  An absolute URL with any scheme other than `file:`, such as `https://...`, `mailto:...`, `tel:+...`, or `keynote://...`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/hyperlink)*