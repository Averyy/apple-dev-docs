# init(identifier:source:destination:)

**Framework**: UIKit  
**Kind**: init

Initializes and returns a storyboard segue object for use in performing a segue.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(identifier: String?, source: UIViewController, destination: UIViewController)
```

#### Return Value

An initialized segue object.

#### Discussion

This method is the designated initializer for segue objects. If you subclass [`UIStoryboardSegue`](uistoryboardsegue.md), you can override this method and perform any custom initialization in your implementation. Your implementation should call `super` first and then proceed if that method doesn’t return `nil`.

## Parameters

- `identifier`: The identifier you want to associate with this particular instance of the segue. You can use this identifier to differentiate one type of segue from another at runtime.
- `source`: The view controller visible at the start of the segue.
- `destination`: The view controller to display after the completion of the segue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistoryboardsegue/init(identifier:source:destination:))*