# getContext

**Framework**: Webkitjs  
**Kind**: instm

Returns the drawing context for the canvas.

**Availability**:
- Safari Desktop 3.0+
- Safari Mobile 1.0+

## Declaration

```swift
RenderingContext? getContext(
    DOMString contextId, 
    any ... arguments
);
```

#### Return_value

The context object. Currently, always a `CanvasRenderingContext2D` object.

#### Discussion

 Use the `getContext` method to obtain a drawing context for the canvas. All drawing on the canvas is done using the methods and properties of the context.

## Parameters

- `contextId`: The identifier for the context. Currently, only the identifier   is supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/htmlcanvaselement/1629325-getcontext)*