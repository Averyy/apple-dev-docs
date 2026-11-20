# ConnectionLine.End.Anchor

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

How one end of a connection line connects to another object.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object ConnectionLine.End.Anchor
```

## Overview

The line stays connected as the other object moves. Anchors are resolved after the enclosing list of objects is read, so the target may appear after the line.

## Topics

### Enumerations
- [type ConnectionLine.End.Anchor.Magnet](./connectionline.end.anchor.magnet.md)
  The point on the anchored object that the line connects to.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.connection-line.end.anchor`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `object_id` (string) *(required)*: The identifier of the object this end is connected to. The reference is resolved only among the connection line’s siblings, not across the document, so the object must be a sibling of the connection line. It also can’t be a connection line, a group, an audio clip, or a shape with a straight line path. If it can’t be connected, this end is left unconnected at `ConnectionLine.End.end_point` and a warning is reported. An end connected to the object that fills the `title`, `body`, or `slide_number` placeholder, or a layout’s `object` placeholder, is also left unconnected, but no warning is reported.
- `magnet` (ConnectionLine.End.Anchor.Magnet): Which point on the connected object this end attaches to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/connectionline.end.anchor)*