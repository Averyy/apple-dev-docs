# caseSensitive

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to consider case when matching the search string.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- visionOS 1.0+

## Declaration

```swift
var caseSensitive: Bool { get set }
```

```objc
@property (nonatomic) BOOL caseSensitive;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the web view takes case into account when matching the search string. The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Configuring the Search Parameters
- [var backwards: Bool](./backwards.md)
  A Boolean value that indicates the search direction, relative to the current selection.
- [var wraps: Bool](./wraps.md)
  A Boolean value that indicates whether the search wraps around to the other side of the page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkfindconfiguration/casesensitive)*