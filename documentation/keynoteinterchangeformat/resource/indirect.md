# Resource.indirect

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

Data stored in a separate file, identified by name rather than carried in the resource.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Resource.indirect
```

## Overview

Written as `{"indirect": …}`: the `indirect` form of `Resource`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.resource`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `indirect` (Resource.IndirectResource) *(required)*: Data stored in a separate file, identified by name rather than carried in the resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/resource/indirect)*