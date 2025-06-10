# playgroundLiveViewRepresentation

**Framework**: Playground Support  
**Kind**: intfp  
**Required**: Yes

The view or view controller used to render and manage the live view.

**Availability**:
- macOS 11.0+
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
var playgroundLiveViewRepresentation: PlaygroundLiveViewRepresentation { get }
```

#### Return_value

A view or view controller able to render and manage the live view. View controllers are preferred.

> ❗ **Important**: The view or view controller returned by this method must be the root of the hierarchy. Views can't have superviews or associated view controllers, and view controllers can't have parent view controllers.

#### Discussion

The value returned by [`playgroundLiveViewRepresentation`](playgroundliveviewable/1978828-playgroundliveviewrepresentation.md) can be different each time the property is accessed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundsupport/playgroundliveviewable/1978828-playgroundliveviewrepresentation)*