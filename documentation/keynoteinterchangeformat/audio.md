# Audio

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A sound attached to a slide.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Audio
```

## Overview

An audio object has no visible size of its own; it appears as a fixed-size icon, so Keynote ignores the size in `geometry` and only uses the position.

This type includes the properties of `CanvasObject`, as does every other type that adopts it.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.audio`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `identifier` (string): An identifier for this object that other objects use to refer to it. This identifier must be unique across the whole document.
- `geometry` (Geometry): The object’s position and size. If this value is absent, Keynote places the object automatically, with a default position and size for its kind.
- `aspect_ratio_locked` (boolean): A Boolean value that indicates whether the object’s width-to-height ratio is locked when the object resizes. The lock doesn’t constrain the `geometry` property. If this property is absent, images, movies, and groups default to `true`, and other objects to `false`.

  **Default**: `false`
- `description` (string): The accessibility description for the object, read aloud by assistive technologies such as VoiceOver.
- `resource` (Resource) *(required)*: The resource that contains the audio data. If the resource isn’t playable on the device, has no audio track, or contains video, the object has no effect.
- `playback_options` (PlaybackOptions) *(required)*: The playback settings for the audio, such as volume, start and end trim times, looping, and whether playback continues across slides.
- `native_audio_recording` (boolean): A Boolean value that indicates whether to treat the audio as recorded into the document rather than imported as a sound file. Recorded audio can’t loop back and forth, and instead plays from beginning to end: when this value is `true`, a Loop Back and Forth setting is replaced with no looping.

  **Default**: `false`

## See Also

### Media
- [object Image](./image.md)
  A picture defined by a resource with optional styling.
- [object Movie](./movie.md)
  A movie or animated image defined by a resource with optional styling.
- [object PlaybackOptions](./playbackoptions.md)
  Options controlling playback of media.
- [object Duration](./duration.md)
  A length of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/audio)*