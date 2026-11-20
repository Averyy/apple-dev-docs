# ListLabelType.number

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A number label.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object ListLabelType.number
```

## Overview

Written as `{"number": …}`: the `number` form of `ListLabelType`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.list-label-type`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `number` (ListLabelType.ListNumberLabel) *(required)*: A number label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/listlabeltype/number)*