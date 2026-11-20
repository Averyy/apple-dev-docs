# Slide

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A slide in a presentation.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Slide
```

## Mentions

- [Understanding Keynote Interchange Format structure](./understanding-keynote-interchange-format-structure.md)

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.slide`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `identifier` (string): The slide’s identifier, which a link can use to point at the slide. Keynote writes a UUID string to this value; opening a presentation gives every slide a fresh identifier, so a value you supply for this identifier isn’t kept.
- `layout` (string): The slide layout of the slide. Keynote matches this value against each layout’s `SlideLayout.identifier`, then its `SlideLayout.name`. If nothing matches, it uses the theme’s first layout and reports a warning; if it’s absent, it uses the first layout.
- `contents` ([SlideObject]): The objects on the slide, ordered back to front, with the first one farthest back. This list includes objects that belong to the slide’s layout, with `SlideObject.source_kind` set to `layout`, only when that layout sets `SlideLayout.slide_objects_layer_with_layout`; otherwise, this list doesn’t include those objects, and the slide draws them behind everything in this list.
- `background` ((SlideBackground | null)): Define the slide background as a color, gradient, or image, which overrides the default background inherited from the layout. A value of `null` removes the background entirely; if you omit the key, the slide retains the background associated with the specified layout.

  **Allowed Types**: `SlideBackground`, `null`
- `depth` (integer): The slide’s indentation level in the slide navigator, on a scale of `1` to `6`. A slide indented deeper than the one before it becomes its child. Keynote clamps rather than rejects a depth more than `6` or more than one level below the preceding slide, and the first slide is always at the top level. The default indentation level is `1`.
- `note` (Text): The slide’s presenter notes contains only text. Keynote removes inline objects with a warning, except for connection lines and non-table objects with an identifier, which prevent the document from loading. Image bullets whose image is missing and inline objects that aren’t importable also halt loading, in contrast to slides, where they merely remove the text box. A paragraph that lacks a `Paragraph.style` defaults to the theme’s Presenter Notes style, or the presentation’s custom style if previously overridden, and Keynote omits `Paragraph.style` for paragraphs that already use the presentation’s Presenter Notes style.

## See Also

### Slides
- [object SlideBackground](./slidebackground.md)
  The background of a slide.
- [object SlideLayout](./slidelayout.md)
  A slide layout in a Keynote theme.
- [object SlideObject](./slideobject.md)
  An object on a slide or slide layout, with slide-specific information about it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/slide)*