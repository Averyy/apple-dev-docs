# PlaygroundLiveViewRepresentation.view(_:)

**Framework**: Playground Support  
**Kind**: enumelt

An AppKit view that's displayed as the live view.

**Availability**:
- macOS 11.0+
- Xcode 12.0+

## Declaration

```swift
case view(NSView)
```

#### Discussion

This view must be the root of a view hierarchy (it must not have a superview), and it must not be owned by a view controller.

## See Also

- [PlaygroundLiveViewRepresentation.viewController(_:)](playgroundliveviewrepresentation/viewcontroller-uej.md)
  An AppKit view controller whose view is displayed as the live view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundsupport/playgroundliveviewrepresentation/view-ues)*