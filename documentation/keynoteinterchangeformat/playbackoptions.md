# PlaybackOptions

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

Options controlling playback of media.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object PlaybackOptions
```

## Topics

### Enumerations
- [type PlaybackOptions.LoopOption](./playbackoptions.loopoption.md)
  The behavior of playback when it reaches the end time.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.playback-options`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `volume` (number): The audio volume for playback, where 0.0 is silent and 1.0 is full volume. Validation: minimum value `0`, maximum value `1`.

  **Default**: `1`; **Minimum**: `0`; **Maximum**: `1`
- `start_time` (Duration): The playback start time. If it’s absent, negative, or later than the end of the media, playback starts at the beginning.
- `end_time` (Duration): The playback end time. If it’s absent, later than the end of the media, or earlier than `start_time`, playback continues to the end of the media.
- `loop_option` (PlaybackOptions.LoopOption): How playback repeats after reaching the end time.
- `plays_across_slides` (boolean): Whether the media plays across slides.

  **Default**: `false`

## See Also

### Media
- [object Audio](./audio.md)
  A sound attached to a slide.
- [object Image](./image.md)
  A picture defined by a resource with optional styling.
- [object Movie](./movie.md)
  A movie or animated image defined by a resource with optional styling.
- [object Duration](./duration.md)
  A length of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/playbackoptions)*