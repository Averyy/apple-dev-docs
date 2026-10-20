# javaScriptContext

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The frame’s global JavaScript execution context.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var javaScriptContext: JSContext! { get }
```

```objc
@property (nonatomic, strong, readonly) JSContext * javaScriptContext;
```

#### Discussion

Use this method to bridge between the WebKit and Objective-C JavaScriptCore API.

## See Also

### Getting DOM Objects
- [var domDocument: DOMDocument!](./domdocument.md)
  The web frame’s DOM document.
- [var frameElement: DOMHTMLElement!](./frameelement.md)
  The web view’s DOM frame element.
- [var globalContext: JSGlobalContextRef!](./globalcontext.md)
  The global JavaScript execution context for bridging between the WebKit and JavaScriptCore C API.
- [var windowObject: WebScriptObject!](./windowobject.md)
  The JavaScript window object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframe/javascriptcontext)*