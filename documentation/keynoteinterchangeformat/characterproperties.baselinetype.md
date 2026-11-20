# CharacterProperties.BaselineType

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The superscript or subscript setting of a text run.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
string CharacterProperties.BaselineType
```

## Discussion

A superscript or subscript run is set at a reduced size, even though `font_size` keeps the value written for it, and the shift it applies is added to `baseline_shift` rather than replacing it.

## See Also

### Enumerations
- [type CharacterProperties.CapitalizationType](./characterproperties.capitalizationtype.md)
  The way the reader alters capitalization of text when it shows it.
- [type CharacterProperties.LigatureType](./characterproperties.ligaturetype.md)
  The ligatures of the font that the reader substitutes when it draws the text.
- [type CharacterProperties.StrikethroughType](./characterproperties.strikethroughtype.md)
  The strikethrough style of text, or no strikethrough.
- [type CharacterProperties.UnderlineType](./characterproperties.underlinetype.md)
  The underline style of text, or no underline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/characterproperties.baselinetype)*