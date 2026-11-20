# ColumnMetrics.equal

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

All the columns are the same width, and so are all the gutters.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object ColumnMetrics.equal
```

## Overview

Written as `{"equal": …}`: the `equal` form of `ColumnMetrics`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.column-metrics`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `equal` (ColumnMetrics.EqualColumnsDescription) *(required)*: All the columns are the same width, and so are all the gutters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/columnmetrics/equal)*