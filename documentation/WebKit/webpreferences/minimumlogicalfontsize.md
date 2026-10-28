# minimumLogicalFontSize

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The minimum logical font size of the web view.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var minimumLogicalFontSize: Int32 { get set }
```

```objc
@property (nonatomic) int minimumLogicalFontSize;
```

## Discussion

The minimum logical font size is the smallest font size that will display in a web view when the content’s font size is imprecisely specified. This includes content with logical sizes (such as `small`) or with a font size specified as a percentage of the default.

Most clients will not want to use this ; rather, explicitly set the minimum display font size using the [`minimumFontSize`](./minimumfontsize.md) property.

The font size specified by `size` should always be greater than zero.

## See Also

### Getting and Setting Font Sizes
- [var defaultFixedFontSize: Int32](./defaultfixedfontsize.md)
  The default fixed font size of the web view.
- [var defaultFontSize: Int32](./defaultfontsize.md)
  The default font size of the web view.
- [var minimumFontSize: Int32](./minimumfontsize.md)
  The minimum font size of the web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpreferences/minimumlogicalfontsize)*