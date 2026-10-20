# minimumFontSize

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The minimum font size of the web view.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var minimumFontSize: Int32 { get set }
```

```objc
@property (nonatomic) int minimumFontSize;
```

#### Discussion

This sets the minimum display font size for the web view, overriding all content-specified styles, including explicitly specified font sizes.

The font size specified by `size` should always be greater than zero.

## See Also

### Getting and Setting Font Sizes
- [var defaultFixedFontSize: Int32](./defaultfixedfontsize.md)
  The default fixed font size of the web view.
- [var defaultFontSize: Int32](./defaultfontsize.md)
  The default font size of the web view.
- [var minimumLogicalFontSize: Int32](./minimumlogicalfontsize.md)
  The minimum logical font size of the web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpreferences/minimumfontsize)*