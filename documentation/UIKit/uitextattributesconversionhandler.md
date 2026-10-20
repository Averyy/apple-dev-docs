# UITextAttributesConversionHandler

**Framework**: UIKit  
**Kind**: typealias  
**Role**: Type Alias

A handler for updating text with current font panel settings.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
typealias UITextAttributesConversionHandler = ([NSAttributedString.Key : Any]) -> [NSAttributedString.Key : Any]
```

```c
typedef NSDictionary<NSString *,id> *(^)(NSDictionary<NSString *,id> *) UITextAttributesConversionHandler;
```

## See Also

### Text formatting
- [class UITextFormattingCoordinator](./uitextformattingcoordinator.md)
  An object that coordinates text formatting using the standard Mac font panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextattributesconversionhandler)*