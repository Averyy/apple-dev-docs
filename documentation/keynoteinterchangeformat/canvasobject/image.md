# CanvasObject.image

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A picture defined by a resource with optional styling.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object CanvasObject.image
```

## Overview

When `geometry` is absent, the reader places the image at the natural size of `resource`. When Keynote exports a presentation, it writes an object the format has no type for as an image. A 3D object, a drawing, an image gallery, a web video, a live video, or a comment on a slide becomes a picture of the object as it appears, with its rotation, flip, title, and caption drawn in, so the image has no `title` or `caption`, and its `geometry` is an unrotated rectangle enclosing the whole picture, including any shadow or reflection. Keynote also writes such an image without a `description`, so the object’s accessibility description is lost. A comment appears in its image only if comments are shown when someone exports the presentation; otherwise the image is empty.

Written as `{"image": …}`: the `image` form of `CanvasObject`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.canvas-object`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out. The latest version of `CanvasObject` is 1.2.

  **Default**: `1.2`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `image` (Image) *(required)*: A picture defined by a resource with optional styling. When `geometry` is absent, the reader places the image at the natural size of `resource`. When Keynote exports a presentation, it writes an object the format has no type for as an image. A 3D object, a drawing, an image gallery, a web video, a live video, or a comment on a slide becomes a picture of the object as it appears, with its rotation, flip, title, and caption drawn in, so the image has no `title` or `caption`, and its `geometry` is an unrotated rectangle enclosing the whole picture, including any shadow or reflection. Keynote also writes such an image without a `description`, so the object’s accessibility description is lost. A comment appears in its image only if comments are shown when someone exports the presentation; otherwise the image is empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/canvasobject/image)*