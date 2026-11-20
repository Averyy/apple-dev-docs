# ConnectionLine.End

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

One end of a connection line.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object ConnectionLine.End
```

## Overview

`end_point` is effectively required: if a line’s `tail` or `head` leaves it out, the line is dropped, even if that end supplies an `anchor`.

## Topics

### Objects
- [object ConnectionLine.End.Anchor](./connectionline.end.anchor.md)
  How one end of a connection line connects to another object.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.connection-line.end`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `end_point` (Position): Where this end of the line stops, unless `anchor` attaches it to an object. Although it’s marked optional, omitting it drops the whole line, even when `anchor` is present. For an attached end, give the object’s center, so a curved line bows where its `line_type` puts it.
- `line_end` (LineEnd): The decoration shown at this end of the connection line, such as an arrowhead. The default is `none`.
- `outset` (number): When anchored, the size of the gap between the edge of the connected object and the start of the connection line, measured along the path in points. Defaults to 0, so the line begins at the edge of the connected object.

  **Default**: `0`
- `anchor` (ConnectionLine.End.Anchor): The object this end attaches to. If it’s absent, the end is unattached and stays at `end_point`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/connectionline.end)*