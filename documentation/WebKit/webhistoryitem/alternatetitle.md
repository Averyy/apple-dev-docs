# alternateTitle

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

An alternate title that may be used in place of the receiver’s page title.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var alternateTitle: String! { get set }
```

```objc
@property (nonatomic, copy) NSString * alternateTitle;
```

## Discussion

This method returns `nil` if no alternate title exists.

## See Also

### Getting and setting page titles
- [var title: String!](./title.md)
  The receiver’s original page title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webhistoryitem/alternatetitle)*