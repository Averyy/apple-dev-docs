# canMakeTextSmaller

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the text can be made smaller.

**Availability**:
- macOS

## Declaration

```swift
var canMakeTextSmaller: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL canMakeTextSmaller;
```

## Discussion

[`true`](../../Swift/true.md) if able to make the text smaller; otherwise, [`false`](../../Swift/false.md).

## See Also

### Changing the Text Size
- [var canMakeTextLarger: Bool](./canmaketextlarger.md)
  A Boolean that indicates whether the text can be made larger.
- [func makeTextLarger(Any?)](./maketextlarger%28_%29.md)
  Action method that increases the text size by one unit.
- [func makeTextSmaller(Any?)](./maketextsmaller%28_%29.md)
  Action method that reduces the text size by one unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/canmaketextsmaller)*