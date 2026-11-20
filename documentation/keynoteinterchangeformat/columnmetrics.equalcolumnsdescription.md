# ColumnMetrics.EqualColumnsDescription

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

An arrangement of a text area into columns of equal width.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object ColumnMetrics.EqualColumnsDescription
```

## Overview

Only `count` and `gutter_width` are specified; each column takes an equal share of the width the gutters leave. The gutters together are clamped to 75% of the text width, so a large `gutter_width` is silently narrowed.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.column-metrics.equal-columns-description`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `count` (integer) *(required)*: The number of columns. Validation: minimum value `1`, maximum value `10`.

  **Minimum**: `1`; **Maximum**: `10`
- `gutter_width` (number): The width of the gutter between adjacent columns, the same between every pair, as a percentage of the width available for text inside the container (its width less its padding). It’s only meaningful when `count` is greater than `1`; the default is 5%. Validation: minimum value `0`, maximum value `75`.

  **Minimum**: `0`; **Maximum**: `75`

## See Also

### Objects
- [object ColumnMetrics.UnequalColumnsDescription](./columnmetrics.unequalcolumnsdescription.md)
  An arrangement of a text area into columns of specified widths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/columnmetrics.equalcolumnsdescription)*