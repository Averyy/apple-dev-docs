# domDocument

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The web frame’s DOM document.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var domDocument: DOMDocument! { get }
```

```objc
@property (nonatomic, strong, readonly) DOMDocument * DOMDocument;
```

## Discussion

`nil` if the receiver doesn’t have a DOM document; for example, if it’s a standalone image.

## See Also

### Getting DOM Objects
- [var frameElement: DOMHTMLElement!](./frameelement.md)
  The web view’s DOM frame element.
- [var globalContext: JSGlobalContextRef!](./globalcontext.md)
  The global JavaScript execution context for bridging between the WebKit and JavaScriptCore C API.
- [var javaScriptContext: JSContext!](./javascriptcontext.md)
  The frame’s global JavaScript execution context.
- [var windowObject: WebScriptObject!](./windowobject.md)
  The JavaScript window object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframe/domdocument)*