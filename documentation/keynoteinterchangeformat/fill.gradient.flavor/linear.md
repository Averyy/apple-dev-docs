# Fill.Gradient.Flavor.linear

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A gradient that varies along a straight line between its stops.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Fill.Gradient.Flavor.linear
```

## Overview

Written as `{"linear": …}`: the `linear` form of `Fill.Gradient.Flavor`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.fill.gradient.flavor`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `linear` (Fill.Gradient.Flavor.Linear) *(required)*: A gradient that varies along a straight line between its stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/fill.gradient.flavor/linear)*