# didReceiveMemoryWarning()

**Framework**: UIKit  
**Kind**: method

Sent to the view controller when the app receives a memory warning.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func didReceiveMemoryWarning()
```

## Mentions

- [Responding to memory warnings](responding-to-memory-warnings.md)

#### Discussion

Your app never calls this method directly. Instead, this method is called when the system determines that the amount of available memory is low.

You can override this method to release any additional memory used by your view controller. If you do, your implementation of this method must call the `super` implementation at some point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/didreceivememorywarning())*