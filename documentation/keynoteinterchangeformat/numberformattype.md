# NumberFormatType

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A format for numbers, such as those in a numbered list.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object NumberFormatType
```

## Overview

Not every combination of `kind`, `upper`, `formal`, and `format` exists; an unsupported combination falls back to a plain number followed by a period.

## Topics

### Enumerations
- [type NumberFormatType.Format](./numberformattype.format.md)
  The decoration around a number, such as a trailing period or parentheses.
- [type NumberFormatType.Kind](./numberformattype.kind.md)
  A numbering system.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.number-format-type`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `kind` (NumberFormatType.Kind): The numbering system used for the label, such as Western digits, Roman numerals, Latin letters, or a Japanese, Chinese, Korean, Arabic, or Hebrew system. The default is `numeric`.
- `upper` (boolean): Whether to use uppercase, which applies only to the `roman` and `alpha` kinds; every other kind requires `false`. The default is `false`.
- `formal` (boolean): Whether to use the formal ideographic form, which applies only to the `japanese`, `simplified_chinese`, and `traditional_chinese` kinds; every other kind requires `false`. The default is `false`.
- `format` (NumberFormatType.Format): The decoration around the number: `decimal` for a trailing period, `paren` for a trailing parenthesis, `double_paren` for enclosing parentheses, `circled` (`numeric` kind only), or `standard` (`hebrew_biblical` kind only). The default is `decimal`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/numberformattype)*