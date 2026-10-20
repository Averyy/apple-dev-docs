# identifier

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The unique identifier of the context object.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
var identifier: UUID { get }
```

```objc
@property (nonatomic, strong, readonly) NSUUID * identifier;
```

#### Discussion

The [`UIWritingToolsCoordinator.Context`](../context.md) object initializes the value of this property at creation time. Use this value to identify the context object within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/context/identifier)*