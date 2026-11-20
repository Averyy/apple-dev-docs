# Path.BezierPath

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A path as an SVG path string, together with the coordinate space in which its points are expressed.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Path.BezierPath
```

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.path.bezier-path`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `path` (string) *(required)*: The path as SVG path data: the value of the `d` attribute of a `<path>` element; it must be non-empty and must begin with a moveto command. Any standard path command is accepted when reading, but only absolute moveto, lineto, curveto, and closepath commands are produced when writing, so the exact command sequence isn’t guaranteed to be preserved.
- `space` (Rect): If present, `path` is treated as relative to this rectangle, and then stretched proportionally to cover the bounding box of the owner’s geometry (`Image.Mask.geometry` for an image mask) before the owner’s flip and rotation apply. The owner’s size and position then become the bounds of the mapped path, so when `space` differs from the path’s tight bounds, the owner’s written size and position aren’t preserved, unless the owner sizes itself to fit its text. When absent, the path’s tight bounds are used. When the owner has no geometry, `space` must equal those bounds, and the points are then absolute coordinates in the containing slide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/path.bezierpath)*