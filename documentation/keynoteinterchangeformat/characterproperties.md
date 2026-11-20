# CharacterProperties

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The character-level properties of text.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object CharacterProperties
```

## Overview

A `preset_identifier` here is matched against the document stylesheet’s character styles before the presets in `presets.json`, and an identifier that matches neither is silently ignored. An omitted property is inherited from that preset, from the enclosing style’s parent chain, and, for a text run, from the paragraph style in effect; a `null` clears it instead.

## Topics

### Objects
- [object CharacterProperties.FontFeaturesType](./characterproperties.fontfeaturestype.md)
  A typographic feature of the font.
### Enumerations
- [type CharacterProperties.BaselineType](./characterproperties.baselinetype.md)
  The superscript or subscript setting of a text run.
- [type CharacterProperties.CapitalizationType](./characterproperties.capitalizationtype.md)
  The way the reader alters capitalization of text when it shows it.
- [type CharacterProperties.LigatureType](./characterproperties.ligaturetype.md)
  The ligatures of the font that the reader substitutes when it draws the text.
- [type CharacterProperties.StrikethroughType](./characterproperties.strikethroughtype.md)
  The strikethrough style of text, or no strikethrough.
- [type CharacterProperties.UnderlineType](./characterproperties.underlinetype.md)
  The underline style of text, or no underline.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.character-properties`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `background_color` ((Color | null)): The background color of the text.

  **Allowed Types**: `Color`, `null`
- `baseline` ((CharacterProperties.BaselineType | null)): The superscript or subscript setting of the text.

  **Allowed Types**: `CharacterProperties.BaselineType`, `null`
- `baseline_shift` ((number | null)): The number of points to shift the baseline; a positive value shifts it up and a negative value shifts it down.

  **Allowed Types**: `number`, `null`
- `bold` ((boolean | null)): Whether the text is bold.

  **Allowed Types**: `boolean`, `null`
- `capitalization` ((CharacterProperties.CapitalizationType | null)): The capitalization of the text: All Caps, Small Caps, Start Case, or Title Case.

  **Allowed Types**: `CharacterProperties.CapitalizationType`, `null`
- `character_fill` ((Fill | null)): The fill inside the characters, which can be a color, a gradient, or an image. The outline around the characters comes from `stroke` instead.

  **Allowed Types**: `Fill`, `null`
- `character_fill_should_fill_container` ((boolean | null)): Whether a gradient `character_fill` is measured across the whole text container rather than across just the text it fills. It affects only a gradient fill, and the default is `false`.

  **Allowed Types**: `boolean`, `null`
- `compatibility_font_name` ((string | null)): The original font name, carried over from a PowerPoint presentation whose font was substituted, so that the name can be restored if the presentation is exported back to PowerPoint. It’s absent when no substitution took place.

  **Allowed Types**: `string`, `null`
- `emphasis_mark` ((string | null)): The dot added to the sides of characters for emphasis in Japanese text (boten).

  **Allowed Types**: `string`, `null`
- `font_features` (([CharacterProperties.FontFeaturesType] | null)): The font features applied to the text. In Apple Advanced Typography (AAT), typographic effects are achieved through two 16-bit numbers, called a feature and a selector.

  **Allowed Types**: `[CharacterProperties.FontFeaturesType]`, `null`
- `font_name` ((string | null)): The PostScript name of the font. Only the name is carried, not the font itself, so on a device that doesn’t have the font and can’t download it, the text appears in a substitute font.

  **Allowed Types**: `string`, `null`
- `font_size` ((number | null)): The font size, in points.

  **Allowed Types**: `number`, `null`
- `is_named_point_size` ((boolean | null)): Whether `font_size` matches one of the named Chinese font sizes, such as 初号 for 42 points. `font_size` is a value in points either way.

  **Allowed Types**: `boolean`, `null`
- `italic` ((boolean | null)): Whether the text is italic.

  **Allowed Types**: `boolean`, `null`
- `language` ((string | null)): The language ID of the text, for example, `en`, `en-GB`, or `sr-Cyrl`.

  **Allowed Types**: `string`, `null`
- `ligatures` ((CharacterProperties.LigatureType | null)): The ligatures to use: required, standard, or all.

  **Allowed Types**: `CharacterProperties.LigatureType`, `null`
- `shadow` ((Shadow | null)): The shadow applied to the characters.

  **Allowed Types**: `Shadow`, `null`
- `strikethrough` ((CharacterProperties.StrikethroughType | null)): The strikethrough style of the text: single, double, or none.

  **Allowed Types**: `CharacterProperties.StrikethroughType`, `null`
- `strikethrough_color` ((Color | null)): The color of the strikethrough line or lines. When it’s `null`, the line is drawn in the text’s own color; whether a line appears at all comes from `strikethrough`.

  **Allowed Types**: `Color`, `null`
- `strikethrough_width` ((number | null)): The thickness of the strikethrough line or lines, as a multiple of the font’s normal line thickness rather than a length in points; `1` is the font’s normal thickness.

  **Allowed Types**: `number`, `null`
- `stroke` ((TextStroke | null)): The stroke that outlines the characters.

  **Allowed Types**: `TextStroke`, `null`
- `tracking` ((number | null)): The character spacing, as a fraction of the font’s em. For example, 0.20 adds about 20% extra spacing per character; a negative value tightens it.

  **Allowed Types**: `number`, `null`
- `underline` ((CharacterProperties.UnderlineType | null)): The underline style of the text: single, double, wavy, or none.

  **Allowed Types**: `CharacterProperties.UnderlineType`, `null`
- `underline_color` ((Color | null)): The color of the underline. When it’s `null`, the underline is drawn in the text’s own color; whether an underline appears at all comes from `underline`.

  **Allowed Types**: `Color`, `null`
- `word_strikethrough` ((boolean | null)): Whether the strikethrough is drawn only through words, not through whitespace.

  **Allowed Types**: `boolean`, `null`
- `word_underline` ((boolean | null)): Whether the underline is drawn only beneath words, not beneath whitespace.

  **Allowed Types**: `boolean`, `null`
- `writing_direction` ((WritingDirectionType | null)): The writing direction of the text: left to right, right to left, or natural for the content.

  **Allowed Types**: `WritingDirectionType`, `null`

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
- [object ParagraphProperties](./paragraphproperties.md)
  The paragraph-level properties of text.
- [type WritingDirectionType](./writingdirectiontype.md)
  The writing direction of the text.
- [type LineEnd](./lineend.md)
  A decoration drawn at the end of a connection line or of a shape’s open path, such as an arrowhead.
- [object LineSpacingType](./linespacingtype.md)
  The spacing between lines of text.
- [object LayoutProperties](./layoutproperties.md)
  The text layout properties of a shape style or a column of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/characterproperties)*