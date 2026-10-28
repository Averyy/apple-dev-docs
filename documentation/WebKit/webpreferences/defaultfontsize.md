# defaultFontSize

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The default font size of the web view.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var defaultFontSize: Int32 { get set }
```

```objc
@property (nonatomic) int defaultFontSize;
```

## Discussion

The default font size to use for content displayed in a fixed font if no font size or font family is specified.

The font size specified by `size` should always be greater than zero.

## See Also

### Getting and Setting Font Sizes
- [var defaultFixedFontSize: Int32](./defaultfixedfontsize.md)
  The default fixed font size of the web view.
- [var minimumFontSize: Int32](./minimumfontsize.md)
  The minimum font size of the web view.
- [var minimumLogicalFontSize: Int32](./minimumlogicalfontsize.md)
  The minimum logical font size of the web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpreferences/defaultfontsize)*