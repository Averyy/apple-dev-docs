# standardFontFamily

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The standard font family of the web view.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var standardFontFamily: String! { get set }
```

```objc
@property (nonatomic, copy) NSString * standardFontFamily;
```

## Discussion

This preference affects text whose properties do not indicate that they should be displayed in a particular font or class of fonts (such as sans-serif).

## See Also

### Getting and Setting Fonts
- [var cursiveFontFamily: String!](./cursivefontfamily.md)
  The cursive font family of the web view.
- [var fantasyFontFamily: String!](./fantasyfontfamily.md)
  The fantasy font family of the web view.
- [var fixedFontFamily: String!](./fixedfontfamily.md)
  The fixed font family of the web view.
- [var sansSerifFontFamily: String!](./sansseriffontfamily.md)
  The sans serif font family of the web view.
- [var serifFontFamily: String!](./seriffontfamily.md)
  The serif font family of the web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpreferences/standardfontfamily)*