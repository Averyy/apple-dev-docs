# ListLabelType.ListNumberLabel

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A numbered list label.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object ListLabelType.ListNumberLabel
```

## Overview

Its numbers can be tiered, as in 1.1 and 1.2.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.list-label-type.list-number-label`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `number_format` (NumberFormatType): The numbering format for this level, such as numeric, Roman, or alphabetic. The default is a decimal number.
- `scale` (number): The label’s size, as a multiple of the text size at the start of the paragraph. The default is 1.0.
- `tiered` (boolean): Whether the numbers are tiered. The default is `false`.

## See Also

### Objects
- [object ListLabelType.ListImageLabel](./listlabeltype.listimagelabel.md)
  An image bullet.
- [object ListLabelType.ListStringLabel](./listlabeltype.liststringlabel.md)
  A text list label, such as a bullet character or a short string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/listlabeltype.listnumberlabel)*