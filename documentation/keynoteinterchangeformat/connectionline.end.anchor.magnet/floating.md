# ConnectionLine.End.Anchor.Magnet.floating

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

Not used. It stands for the line meeting a point not tied to the object’s outline, at the position given here.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object ConnectionLine.End.Anchor.Magnet.floating
```

## Overview

Written as `{"floating": …}`: the `floating` form of `ConnectionLine.End.Anchor.Magnet`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.connection-line.end.anchor.magnet`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `floating` (Position) *(required)*: Not used. It stands for the line meeting a point not tied to the object’s outline, at the position given here.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/connectionline.end.anchor.magnet/floating)*