# Duration

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A length of time.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Duration
```

## Overview

The only representation is a number of seconds.

A length of time in seconds.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.duration`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `seconds` (number) *(required)*: A length of time in seconds.

## See Also

### Media
- [object Audio](./audio.md)
  A sound attached to a slide.
- [object Image](./image.md)
  A picture defined by a resource with optional styling.
- [object Movie](./movie.md)
  A movie or animated image defined by a resource with optional styling.
- [object PlaybackOptions](./playbackoptions.md)
  Options controlling playback of media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/duration)*