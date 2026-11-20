# CharacterProperties.FontFeaturesType

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A typographic feature of the font.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object CharacterProperties.FontFeaturesType
```

## Overview

It’s named by an Apple Advanced Typography (AAT) feature type and one of that type’s settings. The feature types and their settings are listed in [Appendix F of the TrueType Reference Manual](https://developer.apple.com/fonts/TrueType-Reference-Manual/RM09/AppendixF.html).

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.character-properties.font-features-type`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `feature` (integer) *(required)*: The identifier of the AAT font feature type, as listed in the TrueType Reference Manual, Appendix F.
- `selector` (integer) *(required)*: The identifier of the setting to apply within the feature type named by `feature`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/characterproperties.fontfeaturestype)*