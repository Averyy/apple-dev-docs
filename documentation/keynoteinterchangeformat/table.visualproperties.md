# Table.VisualProperties

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The default styling of a table, broken down by region.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.VisualProperties
```

## Overview

It holds one set of table-wide settings, `overall_properties`, plus paired cell, text, and stroke settings for the body and for each header and footer region. A header or footer region’s settings override the body defaults; per-row, per-column, and per-cell overrides take precedence over everything here.

## Topics

### Objects
- [object Table.VisualProperties.BodyStrokeProperties](./table.visualproperties.bodystrokeproperties.md)
  The borders and gridlines of a table’s body region, and their visibility.
- [object Table.VisualProperties.HeaderFooterStrokeProperties](./table.visualproperties.headerfooterstrokeproperties.md)
  The borders, gridlines, and visibility toggles of a table’s header or footer region.
- [object Table.VisualProperties.OverallProperties](./table.visualproperties.overallproperties.md)
  The style settings that apply to a whole table.
- [object Table.VisualProperties.StrokePreset](./table.visualproperties.strokepreset.md)
  One of a table’s stroke presets.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.visual-properties`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `overall_properties` (Table.VisualProperties.OverallProperties): The table-wide style settings, which include alternating-row fill, writing direction, auto-resize, rounded corners, and other settings for the whole table. Strokes are set in each region’s stroke properties (`body_stroke_properties` and its header-row, header-column, and footer-row counterparts), and cell settings in the matching cell properties.
- `body_cell_properties` (Table.CellProperties): The default cell styling (fill, alignment, padding, and wrap) applied to body cells: the cells outside the header rows, header columns, and footer rows.
- `body_text_properties` (ParagraphProperties): The default paragraph and text style (font, size, color, and alignment) applied to body cells.
- `body_stroke_properties` (Table.VisualProperties.BodyStrokeProperties): The outer borders and interior gridlines of the body region, and their visibility toggles.
- `header_row_cell_properties` (Table.CellProperties): The default cell styling for header rows. It overrides `body_cell_properties` for the cells in the top `Table.number_of_header_rows` rows.
- `header_row_text_properties` (ParagraphProperties): The default text style for header rows. It overrides `body_text_properties` for the cells in the top `Table.number_of_header_rows` rows.
- `header_row_stroke_properties` (Table.VisualProperties.HeaderFooterStrokeProperties): The outer border, body separator, and interior gridlines of the header-rows region, plus visibility toggles.
- `header_column_cell_properties` (Table.CellProperties): The default cell styling for header columns. It overrides `body_cell_properties` for the cells in the leading `Table.number_of_header_columns` columns.
- `header_column_text_properties` (ParagraphProperties): The default text style for header columns. It overrides `body_text_properties` for the cells in the leading `Table.number_of_header_columns` columns.
- `header_column_stroke_properties` (Table.VisualProperties.HeaderFooterStrokeProperties): The outer border, body separator, and interior gridlines of the header-columns region, plus visibility toggles.
- `footer_row_cell_properties` (Table.CellProperties): The default cell styling for footer rows. It overrides `body_cell_properties` for the cells in the bottom `Table.number_of_footer_rows` rows.
- `footer_row_text_properties` (ParagraphProperties): The default text style for footer rows. It overrides `body_text_properties` for the cells in the bottom `Table.number_of_footer_rows` rows.
- `footer_row_stroke_properties` (Table.VisualProperties.HeaderFooterStrokeProperties): The outer border, body separator, and interior gridlines of the footer-rows region, plus visibility toggles.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.visualproperties)*