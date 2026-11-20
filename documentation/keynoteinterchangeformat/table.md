# Table

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A table of cells, nested two levels deep.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table
```

## Overview

`content` holds the table’s rows, ordered top to bottom, and each row’s `cells` holds that row’s cells, ordered left to right. The first `number_of_header_rows` rows are header rows, and the last `number_of_footer_rows` are footer rows. Rows and cells that carry nothing may be omitted, so `Table.Row.row_index` and `Table.Cell.column_index` mark where a run resumes after a gap. On a slide, a table whose `title` is absent, has no text, or reads `Unnamed` or `Unnamed Table` gets a default name such as Table `1` as its built-in title, and Keynote renames tables there that share a name the same way until each has its own; which of them keeps the name isn’t defined, and Keynote reports no warning.

This type includes the properties of `CanvasObject`, `CaptionOwning`, and `TitleOwning`, as does every other type that adopts them.

## Topics

### Objects
- [object Table.CategoryRules](./table.categoryrules.md)
  An empty object for a categorized table’s rules, which version 1.0 doesn’t support.
- [object Table.Cell](./table.cell.md)
  A cell in a table.
- [object Table.CellFormat](./table.cellformat.md)
  The display format of a cell’s value.
- [object Table.CellProperties](./table.cellproperties.md)
  The styling of a table cell, other than its strokes.
- [object Table.ColumnHeader](./table.columnheader.md)
  The metadata for a column in a table.
- [object Table.ConditionalStyleSet](./table.conditionalstyleset.md)
  A shared set of conditional highlighting rules that multiple cells can reference.
- [object Table.CustomFormat](./table.customformat.md)
  A user-defined format for a cell.
- [object Table.Date](./table.date.md)
  An absolute point in time.
- [object Table.FilterSet](./table.filterset.md)
  The complete filter configuration for a table.
- [object Table.PivotRules](./table.pivotrules.md)
  A placeholder for a pivot table’s rules, which version 1.0 doesn’t support.
- [object Table.Predicate](./table.predicate.md)
  A condition that’s evaluated against a single cell’s value.
- [object Table.Row](./table.row.md)
  A row in a table.
- [object Table.Sort](./table.sort.md)
  The sort rules that the reader applies to the rows of a table’s content.
- [object Table.VisualProperties](./table.visualproperties.md)
  The default styling of a table, broken down by region.
### Enumerations
- [object Table.CellRange](./table.cellrange.md)
  A rectangular range of cells in a table.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `identifier` (string): An identifier for this object that other objects use to refer to it. This identifier must be unique across the whole document.
- `geometry` (Geometry): The object’s position and size. If this value is absent, Keynote places the object automatically, with a default position and size for its kind.
- `aspect_ratio_locked` (boolean): A Boolean value that indicates whether the object’s width-to-height ratio is locked when the object resizes. The lock doesn’t constrain the `geometry` property. If this property is absent, images, movies, and groups default to `true`, and other objects to `false`.

  **Default**: `false`
- `description` (string): The accessibility description for the object, read aloud by assistive technologies such as VoiceOver.
- `title` (Label): The object’s title.
- `caption` (Label): The object’s caption, which Keynote always places below the object. If a caption is off, you still write it out with `Label.is_visible` set to `false`, so having a value doesn’t mean the caption shows.
- `table_name_border_enabled` (boolean): Whether a border is drawn around the table’s name (title) box. The border uses the header row’s border stroke, `Table.VisualProperties.header_row_stroke_properties.border_stroke`.

  **Default**: `false`
- `number_of_columns` (integer) *(required)*: The total number of columns in the table, including header, body, and hidden columns. A count below 1, or above the largest supported column count, is adjusted to the nearest supported count rather than rejected.
- `number_of_rows` (integer) *(required)*: The total number of rows in the table, including header, body, footer, hidden, and filtered rows. A count below 1, or above the largest supported row count, is adjusted to the nearest supported count rather than rejected.
- `number_of_header_rows` (integer): The number of header rows at the top of the table, which are styled separately from body rows and typically contain column titles. A negative count, or one greater than `number_of_rows`, is adjusted to fit rather than rejected.

  **Default**: `0`
- `number_of_header_columns` (integer): The number of header columns at the leading edge of the table, which are styled separately from body columns and typically contain row labels. A negative count, or one greater than `number_of_columns`, is adjusted to fit rather than rejected.

  **Default**: `0`
- `number_of_footer_rows` (integer): The number of footer rows at the bottom of the table, which are styled separately from body rows and typically contain totals or summaries. A negative count is treated as zero, and if `number_of_header_rows` plus `number_of_footer_rows` would exceed `number_of_rows`, the footer count is reduced to fit rather than rejected.

  **Default**: `0`
- `default_column_width` (number): The default column width, in points, which must be greater than 0. It’s used for any column that doesn’t override it with `Table.ColumnHeader.column_width`.

  **Default**: `98`
- `default_row_height` (number): The default row height, in points, which must be greater than 0. It’s used for any row that doesn’t override it with `Table.Row.row_height`.

  **Default**: `20`
- `visual_properties` (Table.VisualProperties): The default styles for the whole table. These are table-level properties, such as strokes and alternating row fills, plus default cell and text properties for each region (body, header rows, header columns, and footer rows). Cell- and column-level overrides take precedence over these defaults.
- `column_headers` ([Table.ColumnHeader]): The metadata for each column, including its stable column ID, its display title, its default cell format, style, and text, and an optional column width override. It provides the column identity that formula references and merges use. There’s one entry for each column, in left-to-right order, so an entry’s position here is that column’s position in every row’s `cells`.
- `content` ([Table.Row]): The table’s rows as displayed, including header and footer rows; trailing blank rows can be omitted. Hidden and filtered rows are included, marked by their `Table.Row.visibility_state`.
- `merges` ([Table.CellRange]): The cell ranges that are each visually merged into a single cell. The content is in the top-left cell, and the other cells in the range are blank. Each range names its corners by this table’s row and column IDs. If a corner names a row or column the table doesn’t have, or a range’s end comes before its start, Keynote drops the whole table, with a warning, instead of loading the table without that merge.
- `conditional_style_sets` ([Table.ConditionalStyleSet]): The shared sets of conditional highlighting rules. Cells reference a set by ID in `Table.Cell.conditional_style_set_identifier`, so the same rules can be reused across many cells without duplication.
- `custom_formats` ([Table.CustomFormat]): The shared custom-format definitions. Cells whose `cell_format.format_type` is `custom` reference one of these by ID in `cell_format.custom_format_identifier`, so the same format definition can be reused across many cells without duplication.
- `transformation` (Table.TransformationInfo): The filter and sort rules applied to this table, in `filter_set` and `sort`; `content` holds the result.

## See Also

### Tables
- [object Table.TransformationInfo](./table.transformationinfo.md)
  Information about how the reader derives a table.
- [type ColumnMetrics](./columnmetrics.md)
  The arrangement of a text area into columns, and the width of the gutters between them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table)*