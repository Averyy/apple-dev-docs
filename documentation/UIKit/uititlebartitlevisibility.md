# UITitlebarTitleVisibility

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

States that determine visibility of the title in the title bar.

**Availability**:
- Mac Catalyst 13.0+

## Declaration

```swift
enum UITitlebarTitleVisibility
```

```c
enum UITitlebarTitleVisibility : NSInteger;
```

## Topics

### Visibility states
- [UITitlebarTitleVisibility.visible](./uititlebartitlevisibility/visible.md)
  A state indicating that the title is visible in the title bar.
- [UITitlebarTitleVisibility.hidden](./uititlebartitlevisibility/hidden.md)
  A state indicating that the title isn’t visible in the title bar.
### Initializers
- [init?(rawValue: Int)](./uititlebartitlevisibility/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring the title bar
- [var separatorStyle: UITitlebarSeparatorStyle](./uititlebar/separatorstyle.md)
  The type of separator that the app displays between the title bar and content of a window.
- [enum UITitlebarSeparatorStyle](./uititlebarseparatorstyle.md)
  Styles that determine the type of separator displayed between the title bar and content of a window.
- [var titleVisibility: UITitlebarTitleVisibility](./uititlebar/titlevisibility.md)
  A value that indicates the visibility of the title.
- [var representedURL: URL?](./uititlebar/representedurl.md)
  A URL of the file or resource represented in the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uititlebartitlevisibility)*