# Paragraph.Constituent.inline_object

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

An inline object.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Paragraph.Constituent.inline_object
```

## Overview

An object that can’t be imported (for example, a movie the device can’t play) isn’t dropped on its own. In the text of a text box or shape, the whole text box or shape is removed, including all of its text; in a slide’s presenter notes, such an object stops the document from loading.

Written as `{"inline_object": …}`: the `inline_object` form of `Paragraph.Constituent`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.paragraph.constituent`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `inline_object` (CanvasObject) *(required)*: An inline object. An object that can’t be imported (for example, a movie the device can’t play) isn’t dropped on its own. In the text of a text box or shape, the whole text box or shape is removed, including all of its text; in a slide’s presenter notes, such an object stops the document from loading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/paragraph.constituent/inline_object)*