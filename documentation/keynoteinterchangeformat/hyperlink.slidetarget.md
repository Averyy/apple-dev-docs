# Hyperlink.SlideTarget

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A target slide inside the same presentation, given either by identifier or by position.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
(object | string("first" | "last" | "last_viewed" | "next" | "previous")) Hyperlink.SlideTarget
```



**Allowed Types**: `object`, `string("first" | "last" | "last_viewed" | "next" | "previous")`

## Overview

The five position cases have no settings of their own, can be written as a plain string, and are the dependable choice when authoring, because they are resolved at the moment the link is followed. `by_identifier` is meaningful only against identifiers belonging to the document being read.

References the `Slide.identifier` of a slide in the same presentation. The value is stored exactly as supplied, and reading a presentation assigns every slide a fresh identifier, so a link whose value matches no identifier in the document being read does nothing when it’s followed.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.hyperlink.slide-target`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `by_identifier` (string) *(required)*: References the `Slide.identifier` of a slide in the same presentation. The value is stored exactly as supplied, and reading a presentation assigns every slide a fresh identifier, so a link whose value matches no identifier in the document being read does nothing when it’s followed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/hyperlink.slidetarget)*