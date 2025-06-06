# perform()

**Framework**: UIKit  
**Kind**: method

Performs the visual transition for the segue.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func perform()
```

#### Discussion

Subclasses override this method and use it to perform the animations from the views in [`source`](uistoryboardsegue/source.md) to the views in [`destination`](uistoryboardsegue/destination.md). Typically, you use UIKit or Core Animation to set up an animation from one set of views to the next. For more complex animations, you might take a snapshot image of the two view hierarchies and manipulate the images instead of the actual view objects.

Regardless of how you perform the animation, at the end of it, you’re responsible for installing the destination view controller (and its views) in the right place so that it can handle events. For example, if you were to implement a custom modal transition, you might perform your animations using snapshot images and then at the end call the [`presentModalViewController:animated:`](uiviewcontroller/presentmodalviewcontroller:animated:.md) method (with animations disabled) to set up the appropriate modal relationship between the source and destination view controllers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistoryboardsegue/perform())*