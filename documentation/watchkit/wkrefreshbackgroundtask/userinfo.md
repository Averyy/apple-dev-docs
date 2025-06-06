# userInfo

**Framework**: Watchkit  
**Kind**: property

Custom information associated with the background task.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
var userInfo: (any NSSecureCoding & NSObjectProtocol)? { get }
```

#### Discussion

If there is no data associated with the task, this property is set to `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask/userinfo)*