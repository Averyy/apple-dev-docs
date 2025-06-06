# globalContext

**Framework**: Webkit  
**Kind**: property

The global JavaScript execution context for bridging between the WebKit and JavaScriptCore C API.

**Availability**:
- macOS 10.3+

## Declaration

```swift
var globalContext: JSGlobalContextRef! { get }
```

## See Also

- [var domDocument: DOMDocument!](webframe/domdocument.md)
  The web frame’s DOM document.
- [var frameElement: DOMHTMLElement!](webframe/frameelement.md)
  The web view’s DOM frame element.
- [var javaScriptContext: JSContext!](webframe/javascriptcontext.md)
  The frame’s global JavaScript execution context.
- [var windowObject: WebScriptObject!](webframe/windowobject.md)
  The JavaScript window object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframe/globalcontext)*