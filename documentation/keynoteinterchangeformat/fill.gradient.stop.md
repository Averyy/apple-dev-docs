# Fill.Gradient.Stop

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

One color in the gradient, and its position along it.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Fill.Gradient.Stop
```

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.fill.gradient.stop`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `color` (Color) *(required)*: The stop’s color.
- `fraction` (number) *(required)*: The position of the stop within the entire gradient, in the range `0` to `1`. Each stop must have its position at or after the position of the previous stop. Validation: minimum value `0`, maximum value `1`.

  **Minimum**: `0`; **Maximum**: `1`
- `inflection` (number): A position between the stop and the following stop that defines where the halfway blend of the two stops’ colors falls, as a fraction of the distance between them. An inflection of 0.5 blends two stops evenly; lower values pull the blend toward the stop, and higher values toward the following stop. Has no effect on the last stop. Validation: minimum value `0`, maximum value `1`.

  **Default**: `0.5`; **Minimum**: `0`; **Maximum**: `1`


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/fill.gradient.stop)*