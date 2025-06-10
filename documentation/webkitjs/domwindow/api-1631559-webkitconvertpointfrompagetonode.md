# webkitConvertPointFromPageToNode

**Framework**: WebKit JS  
**Kind**: instm

Converts a point from page coordinates to node coordinates.

**Availability**:
- Safari Desktop 10.1+
- Safari Mobile 3.0+

## Declaration

```swift
WebKitPoint webkitConvertPointFromPageToNode(
    optional Node? node, 
    optional WebKitPoint? p
);
```

#### Return_value

A point that is at the same location as `p` but in node coordinates.

## Parameters

- `node`: The coordinate space to convert the given point to.
- `p`: A point in page coordinates to convert to node coordinates.

## See Also

- [webkitConvertPointFromNodeToPage](domwindow/1631271-webkitconvertpointfromnodetopage.md)
  Converts a point from node coordinates of a block element to page coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/domwindow/1631559-webkitconvertpointfrompagetonode)*