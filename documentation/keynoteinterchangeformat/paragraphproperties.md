# ParagraphProperties

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The paragraph-level properties of text.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object ParagraphProperties
```

## Overview

A `preset_identifier` here is matched against the document stylesheet’s paragraph styles before the presets in `presets.json`, and an identifier that matches neither is silently ignored. An omitted property is inherited from that preset and its parent presets, or from the style these properties refine, such as a table region’s text style; a `null` clears it instead. `borders` and `character_properties` don’t accept a `null`.

## Topics

### Objects
- [object ParagraphProperties.BorderStyleType](./paragraphproperties.borderstyletype.md)
  The style of a paragraph’s borders or rules.
### Enumerations
- [type ParagraphProperties.AlignmentType](./paragraphproperties.alignmenttype.md)
  The horizontal alignment of a paragraph.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.paragraph-properties`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `alignment` ((ParagraphProperties.AlignmentType | null)): The horizontal alignment of the paragraph.

  **Allowed Types**: `ParagraphProperties.AlignmentType`, `null`
- `decimal_tab` ((string | null)): The character that text lines up on at a decimal tab stop, such as `.` or `,`. The default is the decimal separator of the document’s language.

  **Allowed Types**: `string`, `null`
- `default_tabs` ((number | null)): The distance, in points, between the automatic tab stops that apply where no explicit stop from `tabs` is defined.

  **Allowed Types**: `number`, `null`
- `fill` ((Color | null)): The background color behind the paragraph.

  **Allowed Types**: `Color`, `null`
- `first_line_indent` ((number | null)): The indentation, in points, of the paragraph’s first line, if it differs from the rest. It’s the left indent for left-to-right paragraphs and the right indent for right-to-left paragraphs, and it replaces `left_indent` on that line rather than adding to it, so a smaller value gives a hanging indent.

  **Allowed Types**: `number`, `null`
- `following_style` ((string | null)): The identifier or name of the paragraph style applied to the next paragraph created after this one, such as a body style following a heading. It’s matched first against the identifiers of the styles in the document’s stylesheet (a stylesheet entry’s `preset_identifier`), and then against style names. A value matching neither is ignored.

  **Allowed Types**: `string`, `null`
- `hyphenate` ((boolean | null)): Whether to allow long words in the paragraph to be hyphenated at line breaks. Hyphenation also requires document-wide hyphenation to be on and never happens in right-to-left paragraphs, so `false` suppresses hyphenation for the paragraph while `true` can’t introduce it.

  **Allowed Types**: `boolean`, `null`
- `list_style` ((string | null)): The identifier or name of the list style that text using this paragraph style starts with, matched against list-style identifiers first, then names. A stylesheet list style’s identifier is normally its `preset_identifier`. `null` means no list style, and a value matching no identifier and no name is ignored.

  **Allowed Types**: `string`, `null`
- `keep_lines_together` ((boolean | null)): Whether to keep all of the paragraph’s lines on the same page, if possible.

  **Allowed Types**: `boolean`, `null`
- `keep_with_next` ((boolean | null)): Whether to keep all of the paragraph’s lines on the same page as the next paragraph, if possible.

  **Allowed Types**: `boolean`, `null`
- `left_indent` ((number | null)): The indentation, in points, of the paragraph’s left edge from the left edge of the text column.

  **Allowed Types**: `number`, `null`
- `line_spacing` ((LineSpacingType | null)): The line spacing rule and amount for the paragraph.

  **Allowed Types**: `LineSpacingType`, `null`
- `outline_level` ((integer | null)): The depth of the paragraph in the document outline, where `0` is the top level. Use `-1` for body text that isn’t part of the outline; values outside the range `-1` to `999` are clamped.

  **Allowed Types**: `integer`, `null`
- `start_on_new_page` ((boolean | null)): Whether the paragraph starts on a new page.

  **Allowed Types**: `boolean`, `null`
- `borders` (ParagraphProperties.BorderStyleType): The paragraph’s border or rule style.
- `right_indent` ((number | null)): The indentation, in points, of the paragraph’s right edge from the right edge of the text column.

  **Allowed Types**: `number`, `null`
- `space_after` ((number | null)): The space after the paragraph, in points.

  **Allowed Types**: `number`, `null`
- `space_before` ((number | null)): The space before the paragraph, in points.

  **Allowed Types**: `number`, `null`
- `tabs` (([TabStopType] | null)): The tab stops for the paragraph.

  **Allowed Types**: `[TabStopType]`, `null`
- `prevent_widow` ((boolean | null)): Whether to prevent widows and orphans (a single line that appears by itself at the bottom of a page or top of the following page).

  **Allowed Types**: `boolean`, `null`
- `show_in_bookmarks` ((boolean | null)): Whether to show the paragraph in the bookmarks list.

  **Allowed Types**: `boolean`, `null`
- `show_in_tocnavigator` ((boolean | null)): Whether to show the paragraph in the TOC navigator.

  **Allowed Types**: `boolean`, `null`
- `character_properties` (CharacterProperties): The additional character properties to apply to the paragraph.

## See Also

### Text
- [type Text](./text.md)
  A body of text, such as the text of a text box, a table cell, or a slide’s presenter notes.
- [object TextRun](./textrun.md)
  A run of text with a single character style.
- [object TextStroke](./textstroke.md)
  A stroke for text, or a special value for no stroke.
- [object Textbox](./textbox.md)
  A container for text that someone places directly on a slide or slide layout.
- [object Paragraph](./paragraph.md)
  A paragraph of text.
- [object CharacterProperties](./characterproperties.md)
  The character-level properties of text.
- [type WritingDirectionType](./writingdirectiontype.md)
  The writing direction of the text.
- [type LineEnd](./lineend.md)
  A decoration drawn at the end of a connection line or of a shape’s open path, such as an arrowhead.
- [object LineSpacingType](./linespacingtype.md)
  The spacing between lines of text.
- [object LayoutProperties](./layoutproperties.md)
  The text layout properties of a shape style or a column of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/paragraphproperties)*