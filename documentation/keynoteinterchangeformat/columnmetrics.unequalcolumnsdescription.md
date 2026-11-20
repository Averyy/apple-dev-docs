# ColumnMetrics.UnequalColumnsDescription

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

An arrangement of a text area into columns of specified widths.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object ColumnMetrics.UnequalColumnsDescription
```

## Overview

Each of the column and gutter widths is specified, and together they must total 100.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.column-metrics.unequal-columns-description`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `column_widths` ([number]) *(required)*: The width of each column, as a percentage of the width available for text inside the container (its width less its padding). The number of columns is the length of this array, and the column widths together with the gutter widths must total 100. Validation: minimum `1` item, maximum `10` items.
- `gutter_widths` ([number]): The width of the gutter following each column, as a percentage of the width available for text inside the container (its width less its padding). The array’s length must be exactly one less than the number of column widths, or the content is rejected; if it’s omitted, there are no gutters, which is valid only for a single column. Validation: minimum `1` item, maximum `9` items.

## See Also

### Objects
- [object ColumnMetrics.EqualColumnsDescription](./columnmetrics.equalcolumnsdescription.md)
  An arrangement of a text area into columns of equal width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/columnmetrics.unequalcolumnsdescription)*