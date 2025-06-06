# init(delegate:)

**Framework**: UIKit  
**Kind**: init

Creates a writing tools coordinator and assigns the specified delegate object to it.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
@MainActor
init(delegate: (any UIWritingToolsCoordinator.Delegate)?)
```

#### Discussion

Create the coordinator object during your view’s initialization, and assign the object to your view. Use the [`addInteraction(_:)`](uiview/addinteraction(_:).md) method to add the object to your view.

## Parameters

- `delegate`: An object capable of handling Writing Tools interactions   for your view. The delegate must be able to modify your view’s text   storage and refresh the view’s layout and appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/init(delegate:))*