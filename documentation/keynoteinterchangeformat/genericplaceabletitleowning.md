# GenericPlaceableTitleOwning

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A stand-in for an object with a free-standing title label, when the reader doesn’t recognize its kind.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object GenericPlaceableTitleOwning
```

## Overview

Every set of shared properties has one, to stand in for an object when the reader doesn’t recognize its kind. Nothing in the format has the type `PlaceableTitleOwning`, though, so this object never appears in a document; its properties appear only as part of the types that adopt `PlaceableTitleOwning`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.placeable-title-owning-generic`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `title` (Label): The object’s title.
- `title_is_positioned_on_top` (boolean): When `true`, the title appears above the object; when `false`, the title appears below the object, above the caption if there is one. Defaults to `true`. Keynote ignores this when the object has none, or when it’s hidden with `Label.is_visible` set to `false`; Keynote places a hidden title above the object, where it appears when it shows again.

  **Default**: `true`

## See Also

### Titles
- [object TitleOwning](./titleowning.md)
  The properties for defining a title that an object can display.
- [object CaptionOwning](./captionowning.md)
  The properties for defining an optional caption an object can display.
- [object PlaceableTitleOwning](./placeabletitleowning.md)
  The properties for defining a title an object can display, positioned above or below the object.
- [object GenericTitleOwning](./generictitleowning.md)
  An object with only the properties of title owning.
- [object GenericCaptionOwning](./genericcaptionowning.md)
  An object with only the properties of caption owning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/genericplaceabletitleowning)*