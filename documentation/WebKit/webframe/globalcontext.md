# globalContext

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The global JavaScript execution context for bridging between the WebKit and JavaScriptCore C API.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var globalContext: JSGlobalContextRef! { get }
```

```objc
@property (nonatomic, readonly) JSGlobalContextRef globalContext;
```

## See Also

### Getting DOM Objects
- [var domDocument: DOMDocument!](./domdocument.md)
  The web frame’s DOM document.
- [var frameElement: DOMHTMLElement!](./frameelement.md)
  The web view’s DOM frame element.
- [var javaScriptContext: JSContext!](./javascriptcontext.md)
  The frame’s global JavaScript execution context.
- [var windowObject: WebScriptObject!](./windowobject.md)
  The JavaScript window object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframe/globalcontext)*