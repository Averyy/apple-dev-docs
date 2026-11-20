# Table.ColumnHeader.GroupLabel

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The group that a pivot table’s group-label column stands for.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.ColumnHeader.GroupLabel
```

## Overview

It’s reserved for pivot tables, which version 1.0 doesn’t support. A column whose kind is `group_label` carries it. It identifies the row in the source data being grouped on and the group the column represents.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.column-header.group-label`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `grouping_row_identifier` (string) *(required)*: The stable `Table.Row.row_identifier` of the row in `transformation.base_table.content` whose value drives this grouping along the column axis.
- `group_value` (string) *(required)*: The raw lookup key for this group (for example, `West`). It’s distinct from any formatted display string in the column header cell: the formatted form is in the corresponding cells, and this is the key used for grouping and sorting, and it identifies the group.
- `is_collapsed` (boolean): Whether this group is collapsed.

  **Default**: `false`
- `nesting_level` (integer): The zero-based nesting depth among the column-axis groupings. A value of `0` is the outermost grouping, and deeper levels nest inside it.

  **Default**: `0`


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.columnheader.grouplabel)*