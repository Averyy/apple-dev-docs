# Image

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A picture defined by a resource with optional styling.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Image
```

## Overview

When `geometry` is absent, the reader places the image at the natural size of `resource`. When Keynote exports a presentation, it writes an object the format has no type for as an image. A 3D object, a drawing, an image gallery, a web video, a live video, or a comment on a slide becomes a picture of the object as it appears, with its rotation, flip, title, and caption drawn in, so the image has no `title` or `caption`, and its `geometry` is an unrotated rectangle enclosing the whole picture, including any shadow or reflection. Keynote also writes such an image without a `description`, so the object’s accessibility description is lost. A comment appears in its image only if comments are shown when someone exports the presentation; otherwise the image is empty.

This type includes the properties of `CanvasObject`, `CaptionOwning`, and `PlaceableTitleOwning`, as does every other type that adopts them.

## Topics

### Objects
- [object Image.InstantAlphaPath](./image.instantalphapath.md)
  A masking path applied to an image to clip out its background, with only the area it encloses shown.
- [object Image.Mask](./image.mask.md)
  The crop applied to an image, clipping the resource to a path within the mask’s own geometry.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.image`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `identifier` (string): An identifier for this object that other objects use to refer to it. This identifier must be unique across the whole document.
- `geometry` (Geometry): The object’s position and size. If this value is absent, Keynote places the object automatically, with a default position and size for its kind.
- `aspect_ratio_locked` (boolean): Whether the image’s width-to-height ratio is locked when the image is resized. The lock doesn’t constrain the `geometry` property. The default is `true`.

  **Default**: `true`
- `description` (string): The accessibility description for the object, read aloud by assistive technologies such as VoiceOver.
- `title` (Label): The object’s title.
- `title_is_positioned_on_top` (boolean): When `true`, the title appears above the object; when `false`, the title appears below the object, above the caption if there is one. Defaults to `true`. Keynote ignores this when the object has none, or when it’s hidden with `Label.is_visible` set to `false`; Keynote places a hidden title above the object, where it appears when it shows again.

  **Default**: `true`
- `caption` (Label): The object’s caption, which Keynote always places below the object. If a caption is off, you still write it out with `Label.is_visible` set to `false`, so having a value doesn’t mean the caption shows.
- `resource` (Resource) *(required)*: The resource containing the image’s data. The resource data must decode to a single-frame image; use `Movie` for multi-frame images. A multi-frame animated image, such as an animated GIF, is rejected and the object is dropped. When Keynote writes an image changed with Adjust Image, the resource holds the image with those changes applied, not the original.
- `mask` (Image.Mask): A cropping mask that is applied to the image before it’s shown. The mask’s `geometry` is the visible frame, while the image’s own `geometry` places the image resource. Decorations are shown relative to the intersection of the mask and the image. If absent, the image isn’t cropped.
- `instant_alpha_path` (Image.InstantAlphaPath): A cropping path applied to the image before it’s shown, removing the image’s background.
- `stroke` (Stroke): A border stroke drawn around the image. Defaults to no border.
- `opacity` (number): The image’s opacity, in the range `0` to `1`.

  **Default**: `1`
- `shadow` ((Shadow | null)): The shadow shown beneath the image.

  **Allowed Types**: `Shadow`, `null`
- `reflection` (Reflection): The reflection shown for the image.
- `is_placeholder` (boolean): Whether this image is a media placeholder, meant to be replaced with another image. When `false`, `was_media_replaced` is ignored and treated as `false`.

  **Default**: `false`
- `was_media_replaced` (boolean): If this image is a placeholder, whether the resource in it was replaced.

  **Default**: `false`

## See Also

### Media
- [object Audio](./audio.md)
  A sound attached to a slide.
- [object Movie](./movie.md)
  A movie or animated image defined by a resource with optional styling.
- [object PlaybackOptions](./playbackoptions.md)
  Options controlling playback of media.
- [object Duration](./duration.md)
  A length of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/image)*