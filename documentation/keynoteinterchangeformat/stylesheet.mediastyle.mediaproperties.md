# Stylesheet.MediaStyle.MediaProperties

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The appearance that a media style applies.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Stylesheet.MediaStyle.MediaProperties
```

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.stylesheet.media-style.media-properties`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `stroke` ((Stroke | null)): The stroke or border drawn around an image or movie.

  **Allowed Types**: `Stroke`, `null`
- `opacity` ((number | null)): The opacity of the image or movie, in the range `0` to `1`.

  **Allowed Types**: `number`, `null`
- `reflection` ((Reflection | null)): The reflection of the image or movie.

  **Allowed Types**: `Reflection`, `null`
- `shadow` ((Shadow | null)): The shadow cast behind the image or movie.

  **Allowed Types**: `Shadow`, `null`


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/stylesheet.mediastyle.mediaproperties)*