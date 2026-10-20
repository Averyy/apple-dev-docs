# title

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s original page title.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var title: String! { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * title;
```

#### Discussion

The title returned comes from the title HTML tag for HTML documents.

## See Also

### Getting and setting page titles
- [var alternateTitle: String!](./alternatetitle.md)
  An alternate title that may be used in place of the receiver’s page title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webhistoryitem/title)*