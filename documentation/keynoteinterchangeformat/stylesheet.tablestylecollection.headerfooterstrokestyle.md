# Stylesheet.TableStyleCollection.HeaderFooterStrokeStyle

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

Gridlines, outer border, and separator line for one header or footer region of a table, with an optional name.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Stylesheet.TableStyleCollection.HeaderFooterStrokeStyle
```

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.stylesheet.table-style-collection.header-footer-stroke-style`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `name` (string)
- `properties` (Table.VisualProperties.HeaderFooterStrokeProperties) *(required)*

## See Also

### Objects
- [object Stylesheet.TableStyleCollection.BodyStrokeStyle](./stylesheet.tablestylecollection.bodystrokestyle.md)
  Gridlines and outer borders for the body of a table, with an optional name.
- [object Stylesheet.TableStyleCollection.CellStyle](./stylesheet.tablestylecollection.cellstyle.md)
  Cell styling for one region of a table, with an optional name.
- [object Stylesheet.TableStyleCollection.OverallStyle](./stylesheet.tablestylecollection.overallstyle.md)
  A table style’s table-wide settings, with an optional name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/stylesheet.tablestylecollection.headerfooterstrokestyle)*