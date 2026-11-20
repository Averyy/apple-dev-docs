# Textbox

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A container for text that someone places directly on a slide or slide layout.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Textbox
```

## Overview

It takes its typography and background from the text-box presets rather than the shape presets. A `shape` can hold text too.

This type includes the properties of `CanvasObject`, `CaptionOwning`, and `PlaceableTitleOwning`, as does every other type that adopts them.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.textbox`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `identifier` (string): An identifier for this object that other objects use to refer to it. This identifier must be unique across the whole document.
- `geometry` (Geometry): The object’s position and size. If this value is absent, Keynote places the object automatically, with a default position and size for its kind.
- `aspect_ratio_locked` (boolean): A Boolean value that indicates whether the object’s width-to-height ratio is locked when the object resizes. The lock doesn’t constrain the `geometry` property. If this property is absent, images, movies, and groups default to `true`, and other objects to `false`.

  **Default**: `false`
- `description` (string): The accessibility description for the object, read aloud by assistive technologies such as VoiceOver.
- `title` (Label): The object’s title.
- `title_is_positioned_on_top` (boolean): When `true`, the title appears above the object; when `false`, the title appears below the object, above the caption if there is one. Defaults to `true`. Keynote ignores this when the object has none, or when it’s hidden with `Label.is_visible` set to `false`; Keynote places a hidden title above the object, where it appears when it shows again.

  **Default**: `true`
- `caption` (Label): The object’s caption, which Keynote always places below the object. If a caption is off, you still write it out with `Label.is_visible` set to `false`, so having a value doesn’t mean the caption shows.
- `fill` (Fill): The fill inside the text box. If absent, the fill from the text box’s preset style is used.
- `stroke` (Stroke): The border around the text box’s shape.
- `opacity` (number): The text box’s opacity, in the range `0` to `1`.

  **Default**: `1`
- `shadow` ((Shadow | null)): The shadow shown beneath the text box.

  **Allowed Types**: `Shadow`, `null`
- `reflection` (Reflection): The reflection shown for the text box.
- `layout_properties` (LayoutProperties): Layout overrides, such as insets and columns, for the text box’s text.
- `paragraph_properties` (ParagraphProperties): Paragraph-level style, such as alignment and spacing, for the text box’s text.
- `text` (Text): The text in the text box.

## See Also

### Text
- [type Text](./text.md)
  A body of text, such as the text of a text box, a table cell, or a slide’s presenter notes.
- [object TextRun](./textrun.md)
  A run of text with a single character style.
- [object TextStroke](./textstroke.md)
  A stroke for text, or a special value for no stroke.
- [object Paragraph](./paragraph.md)
  A paragraph of text.
- [object ParagraphProperties](./paragraphproperties.md)
  The paragraph-level properties of text.
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

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/textbox)*