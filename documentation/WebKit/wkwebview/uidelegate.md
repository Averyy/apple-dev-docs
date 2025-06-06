# uiDelegate

**Framework**: Webkit  
**Kind**: property

The object you use to integrate custom user interface elements, such as contextual menus or panels, into web view interactions.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var uiDelegate: (any WKUIDelegate)? { get set }
```

## See Also

- [protocol WKUIDelegate](wkuidelegate.md)
  The methods for presenting native user interface elements on behalf of a webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/uidelegate)*