# Stroke.Line

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A stroke or border that the reader draws as a line in one of several styles.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Stroke.Line
```

## Topics

### Enumerations
- [type Stroke.Line.Pattern](./stroke.line.pattern.md)
  The pattern that the reader uses to draw a stroke: solid, one of the dash styles, or one of the brush styles.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.stroke.line`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `color` (Color): The color of the stroke. If absent, the stroke is black.
- `width` (number): The width of the stroke, in points. Validation: minimum value `0.25`, maximum value `100`.

  **Default**: `1`; **Minimum**: `0.25`; **Maximum**: `100`
- `pattern` (Stroke.Line.Pattern): The pattern of the stroke: solid, dashed, or one of several brush styles.

## See Also

### Objects
- [object Stroke.Frame](./stroke.frame.md)
  A picture frame drawn around an object as its border.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/stroke.line)*