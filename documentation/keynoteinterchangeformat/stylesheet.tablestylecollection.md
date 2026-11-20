# Stylesheet.TableStyleCollection

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The styles that make up one table style preset.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Stylesheet.TableStyleCollection
```

## Overview

Each style applies to one region of a table, and the category and label styles are numbered by grouping depth, with `1` the outermost. The category and pivot styles apply to categorized and pivot tables, which version 1.0 doesn’t support. An omitted style is filled in from the collection’s other styles.

## Topics

### Objects
- [object Stylesheet.TableStyleCollection.BodyStrokeStyle](./stylesheet.tablestylecollection.bodystrokestyle.md)
  Gridlines and outer borders for the body of a table, with an optional name.
- [object Stylesheet.TableStyleCollection.CellStyle](./stylesheet.tablestylecollection.cellstyle.md)
  Cell styling for one region of a table, with an optional name.
- [object Stylesheet.TableStyleCollection.HeaderFooterStrokeStyle](./stylesheet.tablestylecollection.headerfooterstrokestyle.md)
  Gridlines, outer border, and separator line for one header or footer region of a table, with an optional name.
- [object Stylesheet.TableStyleCollection.OverallStyle](./stylesheet.tablestylecollection.overallstyle.md)
  A table style’s table-wide settings, with an optional name.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.stylesheet.table-style-collection`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `category_level1_cell_style` (Stylesheet.TableStyleCollection.CellStyle): The cell styling for the group rows of a categorized table at grouping depth 1.
- `category_level1_text_style` (Stylesheet.ParagraphStyle): The text style used in the group rows of a categorized table at grouping depth 1.
- `category_level2_cell_style` (Stylesheet.TableStyleCollection.CellStyle): The cell styling for the group rows of a categorized table at grouping depth 2.
- `category_level2_text_style` (Stylesheet.ParagraphStyle): The text style used in the group rows of a categorized table at grouping depth 2.
- `category_level3_cell_style` (Stylesheet.TableStyleCollection.CellStyle): The cell styling for the group rows of a categorized table at grouping depth 3.
- `category_level3_text_style` (Stylesheet.ParagraphStyle): The text style used in the group rows of a categorized table at grouping depth 3.
- `category_level4_cell_style` (Stylesheet.TableStyleCollection.CellStyle): The cell styling for the group rows of a categorized table at grouping depth 4.
- `category_level4_text_style` (Stylesheet.ParagraphStyle): The text style used in the group rows of a categorized table at grouping depth 4.
- `category_level5_cell_style` (Stylesheet.TableStyleCollection.CellStyle): The cell styling for the group rows of a categorized table at grouping depth 5.
- `category_level5_text_style` (Stylesheet.ParagraphStyle): The text style used in the group rows of a categorized table at grouping depth 5.
- `label_level1_cell_style` (Stylesheet.TableStyleCollection.CellStyle): The cell styling for the row of captions naming a group’s summary values, at grouping depth 1.
- `label_level1_text_style` (Stylesheet.ParagraphStyle): The text style used in the row of captions naming a group’s summary values, at grouping depth 1.
- `label_level2_cell_style` (Stylesheet.TableStyleCollection.CellStyle): The cell styling for the row of captions naming a group’s summary values, at grouping depth 2.
- `label_level2_text_style` (Stylesheet.ParagraphStyle): The text style used in the row of captions naming a group’s summary values, at grouping depth 2.
- `label_level3_cell_style` (Stylesheet.TableStyleCollection.CellStyle): The cell styling for the row of captions naming a group’s summary values, at grouping depth 3.
- `label_level3_text_style` (Stylesheet.ParagraphStyle): The text style used in the row of captions naming a group’s summary values, at grouping depth 3.
- `label_level4_cell_style` (Stylesheet.TableStyleCollection.CellStyle): The cell styling for the row of captions naming a group’s summary values, at grouping depth 4.
- `label_level4_text_style` (Stylesheet.ParagraphStyle): The text style used in the row of captions naming a group’s summary values, at grouping depth 4.
- `label_level5_cell_style` (Stylesheet.TableStyleCollection.CellStyle): The cell styling for the row of captions naming a group’s summary values, at grouping depth 5.
- `label_level5_text_style` (Stylesheet.ParagraphStyle): The text style used in the row of captions naming a group’s summary values, at grouping depth 5.
- `pivot_body_summary_row_cell_style` (Stylesheet.TableStyleCollection.CellStyle): The cell styling for the subtotal rows in the body of a pivot table.
- `pivot_body_summary_column_cell_style` (Stylesheet.TableStyleCollection.CellStyle): The cell styling for the subtotal columns in the body of a pivot table.
- `pivot_header_column_summary_cell_style` (Stylesheet.TableStyleCollection.CellStyle): The cell styling for the header column cells that label a pivot table’s subtotal rows.
- `body_cell_style` (Stylesheet.TableStyleCollection.CellStyle) *(required)*
- `body_stroke_style` (Stylesheet.TableStyleCollection.BodyStrokeStyle) *(required)*
- `body_text_style` (Stylesheet.ParagraphStyle) *(required)*
- `footer_row_cell_style` (Stylesheet.TableStyleCollection.CellStyle) *(required)*
- `footer_row_stroke_style` (Stylesheet.TableStyleCollection.HeaderFooterStrokeStyle) *(required)*
- `footer_row_text_style` (Stylesheet.ParagraphStyle) *(required)*
- `header_column_cell_style` (Stylesheet.TableStyleCollection.CellStyle) *(required)*
- `header_column_stroke_style` (Stylesheet.TableStyleCollection.HeaderFooterStrokeStyle) *(required)*
- `header_column_text_style` (Stylesheet.ParagraphStyle) *(required)*
- `header_row_cell_style` (Stylesheet.TableStyleCollection.CellStyle) *(required)*
- `header_row_stroke_style` (Stylesheet.TableStyleCollection.HeaderFooterStrokeStyle) *(required)*
- `header_row_text_style` (Stylesheet.ParagraphStyle) *(required)*
- `overall_style` (Stylesheet.TableStyleCollection.OverallStyle) *(required)*
- `table_name_shape_style` (Stylesheet.ShapeStyle)
- `table_name_style` (Stylesheet.ParagraphStyle)

## See Also

### Objects
- [object Stylesheet.CharacterStyle](./stylesheet.characterstyle.md)
  A preset that the reader applies to a range of text within a paragraph.
- [object Stylesheet.ListStyle](./stylesheet.liststyle.md)
  A preset for bullets and numbering.
- [object Stylesheet.MediaStyle](./stylesheet.mediastyle.md)
  A preset for images and movies.
- [object Stylesheet.ParagraphStyle](./stylesheet.paragraphstyle.md)
  A preset that the reader applies to whole paragraphs, such as a title or body style.
- [object Stylesheet.ShapeStyle](./stylesheet.shapestyle.md)
  A preset for shapes, text boxes, lines, and connection lines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/stylesheet.tablestylecollection)*