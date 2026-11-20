# Stroke.Frame

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A picture frame drawn around an object as its border.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Stroke.Frame
```

## Topics

### Enumerations
- [type Stroke.Frame.Name](./stroke.frame.name.md)
  The name of the picture frame that Keynote uses to draw the border.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.stroke.frame`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `name` (Stroke.Frame.Name) *(required)*: The name of the picture frame.
- `scale_percent` (number): The scale applied to the picture frame artwork, as a percentage, in the range `10` to `100`. Some picture frames have an effective minimum higher than 10%, and a smaller value is raised to that minimum. Validation: minimum value `10`, maximum value `100`.

  **Default**: `100`; **Minimum**: `10`; **Maximum**: `100`

## See Also

### Objects
- [object Stroke.Line](./stroke.line.md)
  A stroke or border that the reader draws as a line in one of several styles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/stroke.frame)*