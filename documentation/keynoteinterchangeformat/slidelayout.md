# SlideLayout

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A slide layout in a Keynote theme.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object SlideLayout
```

## Mentions

- [Understanding Keynote Interchange Format structure](./understanding-keynote-interchange-format-structure.md)

## Overview

It provides the default arrangement of placeholders, styles, and background for the slides that refer to it by identifier or name.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.slide-layout`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out. The latest version of `SlideLayout` is 1.1.

  **Default**: `1.1`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `identifier` (string): The layout’s identifier, which `Slide.layout` is matched against before `name`. Keynote writes a UUID string here, but any string is accepted. Keep it unique within the theme, since two layouts sharing one can’t be told apart.
- `name` (string) *(required)*: The name of the layout as shown in Keynote’s layout list, such as `Title & Subtitle`. It’s matched by `Slide.layout` when no identifier matches. Keep it unique within the theme, since duplicate names can’t be differentiated.
- `contents` ([SlideObject]): The objects on the layout, ordered back to front (the first one is farthest back).
- `background` (SlideBackground): The layout’s background. Slides based on this layout inherit it unless they specify their own background. A background that can’t be read (for example, a background image that is missing or isn’t a valid image) removes the whole layout, including everything on it, and a warning is reported; slides that would have used the layout are given a different one (see `Slide.layout`).
- `slide_objects_layer_with_layout` (boolean): Whether slides using this layout let their own objects layer with the layout’s objects (`true`), or always show their objects in front of every layout object (`false`). When `false`, all layout objects are drawn behind all slide objects regardless of `contents` order.

  **Default**: `false`

## See Also

### Slides
- [object Slide](./slide.md)
  A slide in a presentation.
- [object SlideBackground](./slidebackground.md)
  The background of a slide.
- [object SlideObject](./slideobject.md)
  An object on a slide or slide layout, with slide-specific information about it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/slidelayout)*