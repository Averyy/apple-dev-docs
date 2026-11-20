# Group

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

An ordered set of objects that behave as one when selected, moved, or transformed.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Group
```

## Mentions

- [Understanding Keynote Interchange Format structure](./understanding-keynote-interchange-format-structure.md)

## Overview

The group’s position and size are those of the smallest rectangle enclosing its children, so the reader uses only the rotation and flip from its `geometry`.

This type includes the properties of `CanvasObject`, `CaptionOwning`, and `PlaceableTitleOwning`, as does every other type that adopts them.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.group`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `identifier` (string): An identifier for this object that other objects use to refer to it. This identifier must be unique across the whole document.
- `geometry` (Geometry): The object’s position and size. If this value is absent, Keynote places the object automatically, with a default position and size for its kind.
- `aspect_ratio_locked` (boolean): Whether the group’s width-to-height ratio is locked when the group is resized. The lock doesn’t constrain the `geometry` property. The default is `true`, and a group behaves as locked regardless of this value if any object inside it has a locked aspect ratio.

  **Default**: `true`
- `description` (string): The accessibility description for the object, read aloud by assistive technologies such as VoiceOver.
- `title` (Label): The object’s title.
- `title_is_positioned_on_top` (boolean): When `true`, the title appears above the object; when `false`, the title appears below the object, above the caption if there is one. Defaults to `true`. Keynote ignores this when the object has none, or when it’s hidden with `Label.is_visible` set to `false`; Keynote places a hidden title above the object, where it appears when it shows again.

  **Default**: `true`
- `caption` (Label): The object’s caption, which Keynote always places below the object. If a caption is off, you still write it out with `Label.is_visible` set to `false`, so having a value doesn’t mean the caption shows.
- `children` ([CanvasObject]) *(required)*: The objects in this group, in order from rearmost to frontmost; at least one is required. A child that can’t be read is dropped and its siblings are kept. A group with a single child is written back as that single object, and a group with no valid children is skipped. On a slide or slide layout, a group that’s left with a single child when it’s read is ungrouped too, along with every group that contains it. A group removed this way, on writing or on reading, loses its own `title`, `caption`, `description`, and `aspect_ratio_locked`. Validation: minimum `1` item.

## See Also

### Common types
- [object Size](./size.md)
  A width and height in whichever coordinate space the property using it defines.
- [object Label](./label.md)
  Styled text that the reader uses as a title or caption on an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/group)*