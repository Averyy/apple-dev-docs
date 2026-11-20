# SlideObject

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

An object on a slide or slide layout, with slide-specific information about it.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object SlideObject
```

## Mentions

- [Understanding Keynote Interchange Format structure](./understanding-keynote-interchange-format-structure.md)

## Topics

### Enumerations
- [type SlideObject.PlaceholderInfo](./slideobject.placeholderinfo.md)
  The placeholder an object acts as on its slide.
- [type SlideObject.SourceKind](./slideobject.sourcekind.md)
  The source of an object.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.slide-object`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `instructional_text` (string): The placeholder text shown in the object while it’s empty, such as “Title Text” or “Double-click to edit.” It stops showing as soon as the object has content of its own.
- `is_locked` (boolean): Whether the object is locked to prevent editing. It’s ignored when the document is read, so the object always opens unlocked.

  **Default**: `false`
- `object` (CanvasObject) *(required)*: The object itself, such as a shape, text box, image, movie, audio clip, table, chart, connection line, or group.
- `placeholder_info` (SlideObject.PlaceholderInfo): The placeholder the object acts as, predefined or tagged. Setting it marks the object as a placeholder. A tagged placeholder is always shown, and `PlaceholderDefinition` gives the restrictions on a predefined one. When several objects use the same predefined placeholder, only the first is kept and the rest are dropped from the slide without a warning.
- `source_kind` (SlideObject.SourceKind): The source of the object. If it’s absent, the object is treated as the slide’s own. For the `layout` kind, the object’s identifier is matched against the corresponding object in the layout the slide names; an identifier that matches nothing there creates a second, slide-owned copy alongside the layout’s object.

## See Also

### Slides
- [object Slide](./slide.md)
  A slide in a presentation.
- [object SlideBackground](./slidebackground.md)
  The background of a slide.
- [object SlideLayout](./slidelayout.md)
  A slide layout in a Keynote theme.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/slideobject)*