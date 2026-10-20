# fixedFontFamily

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The fixed font family of the web view.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var fixedFontFamily: String! { get set }
```

```objc
@property (nonatomic, copy) NSString * fixedFontFamily;
```

#### Discussion

This preference affects text whose properties indicate that it should be displayed in a fixed font but do not specify a particular font.

## See Also

### Getting and Setting Fonts
- [var cursiveFontFamily: String!](./cursivefontfamily.md)
  The cursive font family of the web view.
- [var fantasyFontFamily: String!](./fantasyfontfamily.md)
  The fantasy font family of the web view.
- [var sansSerifFontFamily: String!](./sansseriffontfamily.md)
  The sans serif font family of the web view.
- [var serifFontFamily: String!](./seriffontfamily.md)
  The serif font family of the web view.
- [var standardFontFamily: String!](./standardfontfamily.md)
  The standard font family of the web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpreferences/fixedfontfamily)*