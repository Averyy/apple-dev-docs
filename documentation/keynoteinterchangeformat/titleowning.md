# TitleOwning

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The properties for defining a title that an object can display.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object TitleOwning
```

## Overview

`table` and every type of `Chart` keep only the title’s characters and its `Label.paragraph_properties`, so styling that varies from one run to the next inside `Label.text` is discarded.

An object with only the properties of title owning.

Every set of shared properties has one, to stand in for an object whose kind isn’t recognized. Nothing in the format has the type `TitleOwning`, though, so this object never appears in a document; its properties appear only as part of the types that adopt `TitleOwning`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.title-owning`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `genericTitleOwning` (GenericTitleOwning) *(required)*: An object with only the properties of title owning. Every set of shared properties has one, to stand in for an object whose kind isn’t recognized. Nothing in the format has the type `TitleOwning`, though, so this object never appears in a document; its properties appear only as part of the types that adopt `TitleOwning`.

## See Also

### Titles
- [object CaptionOwning](./captionowning.md)
  The properties for defining an optional caption an object can display.
- [object PlaceableTitleOwning](./placeabletitleowning.md)
  The properties for defining a title an object can display, positioned above or below the object.
- [object GenericTitleOwning](./generictitleowning.md)
  An object with only the properties of title owning.
- [object GenericCaptionOwning](./genericcaptionowning.md)
  An object with only the properties of caption owning.
- [object GenericPlaceableTitleOwning](./genericplaceabletitleowning.md)
  A stand-in for an object with a free-standing title label, when the reader doesn’t recognize its kind.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/titleowning)*