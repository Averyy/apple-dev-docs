# Shape

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A path with a fill and a stroke.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Shape
```

## Overview

When `geometry` is absent, the geometry defaults to the smallest rectangle that encloses the path. Shapes can have an open or a closed path; a path is *open* when it has a single subpath, no `closepath` command, and ends that don’t meet. Open shapes can have endpoints, `head` and `tail`. Keynote reads a `path` that is a single, straight, open segment as a line and takes its styling from the line presets. A shape with either `Geometry.width_valid` or `Geometry.height_valid` set to `false` becomes an auto-sizing text box. Paths that aren’t straight lines can contain text that appears inside the shape.

This type includes the properties of `CanvasObject`, `CaptionOwning`, and `PlaceableTitleOwning`, as does every other type that adopts them.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.shape`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `identifier` (string): An identifier for this object that other objects use to refer to it. This identifier must be unique across the whole document.
- `geometry` (Geometry): The object’s position and size. If this value is absent, Keynote places the object automatically, with a default position and size for its kind.
- `aspect_ratio_locked` (boolean): A Boolean value that indicates whether the object’s width-to-height ratio is locked when the object resizes. The lock doesn’t constrain the `geometry` property. If this property is absent, images, movies, and groups default to `true`, and other objects to `false`.

  **Default**: `false`
- `description` (string): The accessibility description for the object, read aloud by assistive technologies such as VoiceOver.
- `title` (Label): The object’s title.
- `title_is_positioned_on_top` (boolean): When `true`, the title appears above the object; when `false`, the title appears below the object, above the caption if there is one. Defaults to `true`. Keynote ignores this when the object has none, or when it’s hidden with `Label.is_visible` set to `false`; Keynote places a hidden title above the object, where it appears when it shows again.

  **Default**: `true`
- `caption` (Label): The object’s caption, which Keynote always places below the object. If a caption is off, you still write it out with `Label.is_visible` set to `false`, so having a value doesn’t mean the caption shows.
- `path` (Path): The path that forms the shape’s outline. Either this value or `geometry` must be present. If absent, Keynote assume this shape to be a rectangle the same size as `geometry`.
- `tail` (LineEnd): The tail end of the shape, which is a line-end decoration, such as an arrowhead, at the first point of the shape’s `path`. Keynote only display it for an open path. The default is `none`.
- `head` (LineEnd): The head end of the shape, which is a line-end decoration, such as an arrowhead, at the last point of the shape’s `path`. Keynote only displays it for an open path. The default is `none`.
- `fill` (Fill): The fill of the shape’s interior. If absent, it uses the the fill from the shape’s preset style.
- `stroke` (Stroke): The stroke that appears along the shape’s path.
- `opacity` (number): The shape’s opacity, in the range `0` to `1`.

  **Default**: `1`
- `shadow` ((Shadow | null)): The shadow beneath the shape.

  **Allowed Types**: `Shadow`, `null`
- `reflection` (Reflection): The reflection for the shape.
- `layout_properties` (LayoutProperties): Layout overrides, such as insets and columns, for the shape’s text.
- `paragraph_properties` (ParagraphProperties): Paragraph-level style, such as alignment and spacing, for the shape’s text.
- `text` (Text): The text inside the shape.

## See Also

### Shapes
- [object Rect](./rect.md)
  An axis-aligned rectangle in whichever coordinate space the property using it defines.
- [object Path](./path.md)
  A path that traces the outline of a shape or of an image’s mask.
- [type Stroke](./stroke.md)
  A stroke drawn along a path, such as a border around an object.
- [object ConnectionLine](./connectionline.md)
  A line drawn from its tail end to its head end, each of which can attach to another object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/shape)*