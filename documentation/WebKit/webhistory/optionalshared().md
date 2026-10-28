# optionalShared()

**Framework**: WebKit  
**Kind**: method  
**Role**: Type Method

Returns a shared web history object, if one exists.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
class func optionalShared() -> WebHistory!
```

```objc
+ (WebHistory *) optionalSharedHistory;
```

## Return Value

A shared web history object initialized with the default web history file, or `nil` if one was not previously specified using the [`setOptionalShared(_:)`](./setoptionalshared%28_%29.md) method.

## See Also

### Related Documentation
- [func load(from: URL!) throws](./load%28from%29.md)
  Loads the contents of the specified web history file.
- [WebKit Objective-C Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/DisplayWebContent.html#//apple_ref/doc/uid/10000164i)
### Accessing Shared History Objects
- [class func setOptionalShared(WebHistory!)](./setoptionalshared%28_%29.md)
  Sets the web history object to share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webhistory/optionalshared())*