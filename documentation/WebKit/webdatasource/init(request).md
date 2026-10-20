# init(request:)

**Framework**: WebKit  
**Kind**: init  
**Role**: Initializer

initializes a data source with a URL request.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
init!(request: URLRequest!)
```

```objc
- (instancetype) initWithRequest:(NSURLRequest *) request;
```

#### Return Value

The initialized web data source.

#### Discussion

This method is the designated initializer for `WebDataSource` objects. Normally, `WebFrame` objects create their data sources, so you should not invoke this method directly.

## Parameters

- `request`: The URL request used to load the web content.

## See Also

### Related Documentation
- [WebKit Objective-C Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/DisplayWebContent.html#//apple_ref/doc/uid/10000164i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdatasource/init(request:))*