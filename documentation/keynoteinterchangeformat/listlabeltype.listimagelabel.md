# ListLabelType.ListImageLabel

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

An image bullet.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object ListLabelType.ListImageLabel
```

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.list-label-type.list-image-label`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `scale` (number): The height of the bullet image, as a fraction of the text height at the start of the paragraph; the image keeps its aspect ratio. The default is 1.0.
- `offset` (number): The vertical shift of the bullet image from its default position, in points; a positive value raises it. The default is 0.0.
- `resource` (Resource) *(required)*: The resource containing the image’s data.

## See Also

### Objects
- [object ListLabelType.ListNumberLabel](./listlabeltype.listnumberlabel.md)
  A numbered list label.
- [object ListLabelType.ListStringLabel](./listlabeltype.liststringlabel.md)
  A text list label, such as a bullet character or a short string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/listlabeltype.listimagelabel)*