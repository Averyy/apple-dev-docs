# Table.Row.Kind

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The structural role of a row.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
(object | string("body" | "grand_total" | "group_subtotal")) Table.Row.Kind
```



**Allowed Types**: `object`, `string("body" | "grand_total" | "group_subtotal")`

## Overview

The default is `body`; the other cases are reserved for categorized and pivot tables, which version 1.0 doesn’t support.

A category header row, or a pivot table’s row-axis group label; version 1.0 supports neither. Its `GroupLabel` value identifies the grouping column and the group the row represents.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.row.kind`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `group_label` (Table.Row.GroupLabel) *(required)*: A category header row, or a pivot table’s row-axis group label; version 1.0 supports neither. Its `GroupLabel` value identifies the grouping column and the group the row represents.

## See Also

### Enumerations
- [type Table.Row.VisibilityState](./table.row.visibilitystate.md)
  Whether a row is visible, and if not, whether it was hidden explicitly or excluded by the active filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.row.kind)*