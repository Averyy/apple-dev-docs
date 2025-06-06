# domDocument

**Framework**: Webkit  
**Kind**: property

The web frame’s DOM document.

**Availability**:
- macOS 10.3+

## Declaration

```swift
var domDocument: DOMDocument! { get }
```

#### Discussion

`nil` if the receiver doesn’t have a DOM document; for example, if it’s a standalone image.

## See Also

- [var frameElement: DOMHTMLElement!](webframe/frameelement.md)
  The web view’s DOM frame element.
- [var globalContext: JSGlobalContextRef!](webframe/globalcontext.md)
  The global JavaScript execution context for bridging between the WebKit and JavaScriptCore C API.
- [var javaScriptContext: JSContext!](webframe/javascriptcontext.md)
  The frame’s global JavaScript execution context.
- [var windowObject: WebScriptObject!](webframe/windowobject.md)
  The JavaScript window object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframe/domdocument)*