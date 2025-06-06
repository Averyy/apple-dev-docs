# webkitConvertPointFromNodeToPage

**Framework**: Webkitjs  
**Kind**: instm

Converts a point from node coordinates of a block element to page coordinates.

**Availability**:
- Safari Desktop 10.1+
- Safari Mobile 3.0+

## Declaration

```swift
WebKitPoint webkitConvertPointFromNodeToPage(
    optional Node? node, 
    optional WebKitPoint? p
);
```

#### Return_value

A point that is at the same location as `p` but in page coordinates.

## Parameters

- `node`: The coordinate space for  .
- `p`: A point in node coordinates to convert to page coordinates.

## See Also

- [webkitConvertPointFromPageToNode](domwindow/1631559-webkitconvertpointfrompagetonode.md)
  Converts a point from page coordinates to node coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/domwindow/1631271-webkitconvertpointfromnodetopage)*