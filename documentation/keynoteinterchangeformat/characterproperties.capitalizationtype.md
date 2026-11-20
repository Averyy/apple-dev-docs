# CharacterProperties.CapitalizationType

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The way the reader alters capitalization of text when it shows it.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
string CharacterProperties.CapitalizationType
```

## Discussion

This value takes one of the following forms:

- `all_caps`: Draws every letter as a capital of the same height.
- `none`: Draws the text as written, with no change to its capitalization.
- `small_caps`: Draws every letter as a capital, using taller capitals for the letters that were already uppercase.
- `start`: Capitalizes the first letter of every word, including the short words such as articles that `title` leaves lowercase.
- `title`: Capitalizes the text as a title, applying the language-specific title-casing rules.

## See Also

### Enumerations
- [type CharacterProperties.BaselineType](./characterproperties.baselinetype.md)
  The superscript or subscript setting of a text run.
- [type CharacterProperties.LigatureType](./characterproperties.ligaturetype.md)
  The ligatures of the font that the reader substitutes when it draws the text.
- [type CharacterProperties.StrikethroughType](./characterproperties.strikethroughtype.md)
  The strikethrough style of text, or no strikethrough.
- [type CharacterProperties.UnderlineType](./characterproperties.underlinetype.md)
  The underline style of text, or no underline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/characterproperties.capitalizationtype)*