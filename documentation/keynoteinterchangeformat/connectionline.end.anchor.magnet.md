# ConnectionLine.End.Anchor.Magnet

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The point on the anchored object that the line connects to.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
(ConnectionLine.End.Anchor.Magnet.edge | ConnectionLine.End.Anchor.Magnet.floating | string("center" | "east" | "north" | "south" | "west")) ConnectionLine.End.Anchor.Magnet
```



**Allowed Types**: `ConnectionLine.End.Anchor.Magnet.edge`, `ConnectionLine.End.Anchor.Magnet.floating`, `string("center" | "east" | "north" | "south" | "west")`

## Discussion

Keynote connects every line the same way, whatever this value is: aimed at the object’s center and stopped at its outline.

This value takes one of the following forms:

- `center`: The object’s center. It’s the only value Keynote writes.
- `east`: Not used.
- `edge`: Not used. It stands for the line meeting the object’s outline, at the position given here.
- `floating`: Not used. It stands for the line meeting a point not tied to the object’s outline, at the position given here.
- `north`: Not used.
- `south`: Not used.
- `west`: Not used.

## Topics

### Dictionaries
- [object ConnectionLine.End.Anchor.Magnet.edge](./connectionline.end.anchor.magnet/edge.md)
  Not used. It stands for the line meeting the object’s outline, at the position given here.
- [object ConnectionLine.End.Anchor.Magnet.floating](./connectionline.end.anchor.magnet/floating.md)
  Not used. It stands for the line meeting a point not tied to the object’s outline, at the position given here.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/connectionline.end.anchor.magnet)*