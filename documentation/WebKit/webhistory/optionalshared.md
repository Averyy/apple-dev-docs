# optionalShared()

**Framework**: WebKit  
**Kind**: method

Returns a shared web history object, if one exists.

**Availability**:
- macOS 10.3+

## Declaration

```swift
class func optionalShared() -> WebHistory!
```

#### Return Value

A shared web history object initialized with the default web history file, or `nil` if one was not previously specified using the [`setOptionalShared(_:)`](webhistory/setoptionalshared(_:).md) method.

## See Also

- [func load(from: URL!) throws](webhistory/load(from:).md)
  Loads the contents of the specified web history file.
- [WebKit Objective-C Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/DisplayWebContent.html#//apple_ref/doc/uid/10000164i)
- [class func setOptionalShared(WebHistory!)](webhistory/setoptionalshared(_:).md)
  Sets the web history object to share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webhistory/optionalshared())*