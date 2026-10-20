# windowObject

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The JavaScript window object.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var windowObject: WebScriptObject! { get }
```

```objc
@property (nonatomic, strong, readonly) WebScriptObject * windowObject;
```

## See Also

### Getting DOM Objects
- [var domDocument: DOMDocument!](./domdocument.md)
  The web frame’s DOM document.
- [var frameElement: DOMHTMLElement!](./frameelement.md)
  The web view’s DOM frame element.
- [var globalContext: JSGlobalContextRef!](./globalcontext.md)
  The global JavaScript execution context for bridging between the WebKit and JavaScriptCore C API.
- [var javaScriptContext: JSContext!](./javascriptcontext.md)
  The frame’s global JavaScript execution context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframe/windowobject)*