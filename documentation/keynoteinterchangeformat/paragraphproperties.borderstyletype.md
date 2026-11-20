# ParagraphProperties.BorderStyleType

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The style of a paragraph’s borders or rules.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object ParagraphProperties.BorderStyleType
```

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.paragraph-properties.border-style-type`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `stroke` ((TextStroke | null)): The stroke used to draw the border or rule.

  **Allowed Types**: `TextStroke`, `null`
- `width` ((number | null)): The length of the paragraph’s rule lines as a fraction of the paragraph width, where `1` spans the full width and shorter rules are centered. Line thickness comes from `stroke` rather than from this value, and joined border lines that enclose the paragraph always span the full width.

  **Allowed Types**: `number`, `null`
- `offset` ((Offset | null)): The offset to the border or rule, or none.

  **Allowed Types**: `Offset`, `null`
- `rounded` ((boolean | null)): Whether the border corners are rounded.

  **Allowed Types**: `boolean`, `null`
- `no_borders` (boolean): Whether the paragraph has no border or rule lines. It takes precedence over `all_borders` and over the individual `before`, `after`, `leading`, and `trailing` flags. Only `true` has an effect: with none of the six flags `true`, border positions are inherited from the paragraph style rather than cleared.
- `all_borders` (boolean): Whether the paragraph has a border on every side.
- `before` (boolean): Whether the paragraph has a top rule or border.
- `after` (boolean): Whether the paragraph has a bottom rule or border.
- `leading` (boolean): Whether the paragraph has a leading rule or border (left for left-to-right paragraphs, right for right-to-left paragraphs).
- `trailing` (boolean): Whether the paragraph has a trailing rule or border (right for left-to-right paragraphs, left for right-to-left paragraphs).


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/paragraphproperties.borderstyletype)*