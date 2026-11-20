# Movie

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A movie or animated image defined by a resource with optional styling.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Movie
```

## Overview

When `geometry` is omitted, the object takes the resource’s natural size, falling back to 640 × 480 points when the reader cannot measure that size. Placed inline in the text of a text box or shape, an unplayable movie removes that whole text box or shape, including all of its text; in a slide’s presenter notes, it stops the document from loading.

This type includes the properties of `CanvasObject`, `CaptionOwning`, and `PlaceableTitleOwning`, as does every other type that adopts them.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.movie`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `identifier` (string): An identifier for this object that other objects use to refer to it. This identifier must be unique across the whole document.
- `geometry` (Geometry): The object’s position and size. If this value is absent, Keynote places the object automatically, with a default position and size for its kind.
- `aspect_ratio_locked` (boolean): Whether the movie’s width-to-height ratio is locked when the movie is resized. The lock doesn’t constrain the `geometry` property. The default is `true`.

  **Default**: `true`
- `description` (string): The accessibility description for the object, read aloud by assistive technologies such as VoiceOver.
- `title` (Label): The object’s title.
- `title_is_positioned_on_top` (boolean): When `true`, the title appears above the object; when `false`, the title appears below the object, above the caption if there is one. Defaults to `true`. Keynote ignores this when the object has none, or when it’s hidden with `Label.is_visible` set to `false`; Keynote places a hidden title above the object, where it appears when it shows again.

  **Default**: `true`
- `caption` (Label): The object’s caption, which Keynote always places below the object. If a caption is off, you still write it out with `Label.is_visible` set to `false`, so having a value doesn’t mean the caption shows.
- `resource` (Resource) *(required)*: The resource containing the movie’s data. The resource must decode to a multi-frame animated image or to a movie with a video track, playable on the device where the file is imported; if not, the object is skipped.
- `poster_image` (Resource): The resource containing the data for the movie’s poster image. The poster image is shown when the movie isn’t playing; this resource is used only as a fallback when a poster image can’t be generated from `poster_time`.
- `poster_time` (Duration): A time, limited to the movie’s duration, used to determine which frame of the movie is shown when the movie isn’t playing. The default is 0, the first frame, which is also used for a negative or otherwise unusable time.
- `playback_options` (PlaybackOptions) *(required)*: Playback settings for the movie, such as volume, start and end trim times, looping, and whether playback continues across slides.
- `stroke` (Stroke): The border stroke drawn around the movie. The default is no border.
- `opacity` (number): The opacity value of the movie, in the range `0` to `1`.

  **Default**: `1`
- `shadow` ((Shadow | null)): The shadow shown beneath the movie.

  **Allowed Types**: `Shadow`, `null`
- `reflection` (Reflection): The reflection shown for the movie.

## See Also

### Media
- [object Audio](./audio.md)
  A sound attached to a slide.
- [object Image](./image.md)
  A picture defined by a resource with optional styling.
- [object PlaybackOptions](./playbackoptions.md)
  Options controlling playback of media.
- [object Duration](./duration.md)
  A length of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/movie)*