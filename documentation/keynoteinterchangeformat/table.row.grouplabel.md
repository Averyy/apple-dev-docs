# Table.Row.GroupLabel

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The group that a category header row, or a pivot table’s row-axis group label, stands for.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.Row.GroupLabel
```

## Overview

It’s reserved for categorized and pivot tables, which version 1.0 doesn’t support. A row whose kind is `group_label` carries it. It identifies the column being grouped on and the group the row represents.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.row.group-label`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `grouping_column_identifier` (string) *(required)*: The stable `Table.ColumnHeader.column_identifier` of the column in `transformation.base_table.column_headers` whose value drives this grouping.
- `group_value` (string) *(required)*: The raw lookup key for this group (for example, `West`). The formatted form is in the `value` of the row’s first cell; this is the key used for grouping and sorting, and it identifies the group.
- `is_collapsed` (boolean): Whether this group is collapsed.

  **Default**: `false`
- `nesting_level` (integer): The zero-based nesting depth among the row-axis groupings. A value of `0` is the outermost grouping, and deeper levels nest inside it.

  **Default**: `0`


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.row.grouplabel)*