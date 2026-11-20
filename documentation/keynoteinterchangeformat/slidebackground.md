# SlideBackground

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The background of a slide.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object SlideBackground
```

## Overview

A static color, gradient, or image fill. When Keynote exports a presentation, it writes a dynamic background as this case too: an image fill holding one still frame of it, or a color fill when that frame can’t be drawn.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.slide-background`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `standard` (Fill) *(required)*: A static color, gradient, or image fill. When Keynote exports a presentation, it writes a dynamic background as this case too: an image fill holding one still frame of it, or a color fill when that frame can’t be drawn.

## See Also

### Slides
- [object Slide](./slide.md)
  A slide in a presentation.
- [object SlideLayout](./slidelayout.md)
  A slide layout in a Keynote theme.
- [object SlideObject](./slideobject.md)
  An object on a slide or slide layout, with slide-specific information about it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/slidebackground)*