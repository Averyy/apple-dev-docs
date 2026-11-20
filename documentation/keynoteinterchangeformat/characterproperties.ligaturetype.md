# CharacterProperties.LigatureType

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The ligatures of the font that the reader substitutes when it draws the text.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
string CharacterProperties.LigatureType
```

## Discussion

This value takes one of the following forms:

- `all`: Also substitutes the ligatures the font marks as optional, such as ct and st in Hoefler Text.
- `required`: Substitutes only the ligatures needed for correct layout, such as those in Arabic script.
- `standard`: Also substitutes the ligatures the font marks as standard, which typically include pairs such as fl and fi.

## See Also

### Enumerations
- [type CharacterProperties.BaselineType](./characterproperties.baselinetype.md)
  The superscript or subscript setting of a text run.
- [type CharacterProperties.CapitalizationType](./characterproperties.capitalizationtype.md)
  The way the reader alters capitalization of text when it shows it.
- [type CharacterProperties.StrikethroughType](./characterproperties.strikethroughtype.md)
  The strikethrough style of text, or no strikethrough.
- [type CharacterProperties.UnderlineType](./characterproperties.underlinetype.md)
  The underline style of text, or no underline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/characterproperties.ligaturetype)*