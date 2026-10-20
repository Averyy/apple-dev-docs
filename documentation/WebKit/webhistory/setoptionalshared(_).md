# setOptionalShared(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Type Method

Sets the web history object to share.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
class func setOptionalShared(_ history: WebHistory!)
```

```objc
+ (void) setOptionalSharedHistory:(WebHistory *) history;
```

## Parameters

- `history`: The web history object to share.

## See Also

### Related Documentation
- [func load(from: URL!) throws](./load%28from%29.md)
  Loads the contents of the specified web history file.
### Accessing Shared History Objects
- [class func optionalShared() -> WebHistory!](./optionalshared%28%29.md)
  Returns a shared web history object, if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webhistory/setoptionalshared(_:))*