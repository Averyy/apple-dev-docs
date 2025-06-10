# javaScriptContext

**Framework**: WebKit  
**Kind**: property

The frame’s global JavaScript execution context.

**Availability**:
- macOS 10.3+

## Declaration

```swift
var javaScriptContext: JSContext! { get }
```

#### Discussion

Use this method to bridge between the WebKit and Objective-C JavaScriptCore API.

## See Also

- [var domDocument: DOMDocument!](webframe/domdocument.md)
  The web frame’s DOM document.
- [var frameElement: DOMHTMLElement!](webframe/frameelement.md)
  The web view’s DOM frame element.
- [var globalContext: JSGlobalContextRef!](webframe/globalcontext.md)
  The global JavaScript execution context for bridging between the WebKit and JavaScriptCore C API.
- [var windowObject: WebScriptObject!](webframe/windowobject.md)
  The JavaScript window object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframe/javascriptcontext)*