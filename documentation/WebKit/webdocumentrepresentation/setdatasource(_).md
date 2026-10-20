# setDataSource(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sets the receiver’s data source.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
func setDataSource(_ dataSource: WebDataSource!)
```

```objc
- (void) setDataSource:(WebDataSource *) dataSource;
```

#### Discussion

This method is invoked soon after the document representation is created.

## Parameters

- `dataSource`: The data source to associate with the object.

## See Also

### Related Documentation
- [WebKit Objective-C Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/DisplayWebContent.html#//apple_ref/doc/uid/10000164i)
- [func finishedLoading(with: WebDataSource!)](./finishedloading%28with%29.md)
  Invoked when a data source finishes loading its content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdocumentrepresentation/setdatasource(_:))*