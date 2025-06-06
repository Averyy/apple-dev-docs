# cancellationHandler

**Framework**: Xcodekit  
**Kind**: property

A handler to be invoked by Xcode to indicate that the invocation has been canceled by the user.

**Availability**:
- macOS 10.12+

## Declaration

```swift
var cancellationHandler: () -> Void { get set }
```

#### Discussion

There are no guarantees about the thread or queue on which the cancellation handler is invoked. After receiving a cancellation, the command’s `completionHandler` is invoked and no changes are applied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcodekit/xcsourceeditorcommandinvocation/cancellationhandler)*