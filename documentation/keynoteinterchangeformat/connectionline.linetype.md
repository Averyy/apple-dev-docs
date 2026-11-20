# ConnectionLine.LineType

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

How a connection line is routed between its ends.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
(ConnectionLine.LineType.corner | ConnectionLine.LineType.curved | string("straight")) ConnectionLine.LineType
```



**Allowed Types**: `ConnectionLine.LineType.corner`, `ConnectionLine.LineType.curved`, `string("straight")`

## Discussion

A curved route whose control position lies almost on the line between the two ends is written back as `straight`, and that position is discarded.

This value takes one of the following forms:

- `corner`: A route that makes right-angle turns and passes through this position, though not necessarily with a corner there. The reader usually passes straight through a position partway between the ends.
- `curved`: A route that bows between the ends and passes through this position.
- `straight`: A route that makes a straight line between its ends.

## Topics

### Dictionaries
- [object ConnectionLine.LineType.corner](./connectionline.linetype/corner.md)
  A route that makes right-angle turns and passes through this position, though not necessarily with a corner there.
- [object ConnectionLine.LineType.curved](./connectionline.linetype/curved.md)
  A route that bows between the ends and passes through this position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/connectionline.linetype)*