# uiDelegate

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The object you use to integrate custom user interface elements, such as contextual menus or panels, into web view interactions.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
weak var uiDelegate: (any WKUIDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<WKUIDelegate> UIDelegate;
```

## See Also

### Displaying native user interface elements
- [protocol WKUIDelegate](../wkuidelegate.md)
  The methods for presenting native user interface elements on behalf of a webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/uidelegate)*