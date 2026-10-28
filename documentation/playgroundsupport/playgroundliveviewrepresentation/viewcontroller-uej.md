# PlaygroundLiveViewRepresentation.viewController(_:)

**Framework**: Playground Support  
**Kind**: enumelt  
**Role**: Enumeration Case

An AppKit view controller whose view is displayed as the live view.

**Availability**:
- macOS 11.0+
- Xcode 12.0+

## Declaration

```swift
case viewController(NSViewController)
```

## Discussion

This view controller must be the root of a view controller hierarchy (it must not have a parent view controller), and its view must not have a superview.

## See Also

### Displaying AppKit Views
- [PlaygroundLiveViewRepresentation.view(_:)](./view-ues.md)
  An AppKit view that's displayed as the live view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundsupport/playgroundliveviewrepresentation/viewcontroller-uej)*