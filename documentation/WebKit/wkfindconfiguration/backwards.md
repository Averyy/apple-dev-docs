# backwards

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates the search direction, relative to the current selection.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- visionOS 1.0+

## Declaration

```swift
var backwards: Bool { get set }
```

```objc
@property (nonatomic) BOOL backwards;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), searches proceed backward from the current selection. When the value is [`false`](../../Swift/false.md), searches proceed forward from the current selection. The default value of this property is [`false`](../../Swift/false.md).

The web view respects the writing direction of its content. For example, a forward search moves right-to-left and top-to-bottom for a right-to-left language.

## See Also

### Configuring the Search Parameters
- [var caseSensitive: Bool](./casesensitive.md)
  A Boolean value that indicates whether to consider case when matching the search string.
- [var wraps: Bool](./wraps.md)
  A Boolean value that indicates whether the search wraps around to the other side of the page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkfindconfiguration/backwards)*