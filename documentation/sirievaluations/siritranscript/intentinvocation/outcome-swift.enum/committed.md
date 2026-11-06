# committed

**Framework**: Siri Evaluations  
**Kind**: property  
**Role**: Instance Property

Whether Siri committed to the call.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
var committed: Bool { get }
```

## Discussion

The value indicates that it ran, that it is waiting only on the person’s confirmation, or that no outcome was recorded, and is what `Calls(.disallowed)` checks.

## See Also

### Checking outcome state
- [var ran: Bool](./ran.md)
  Whether this counts as the call having run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siritranscript/intentinvocation/outcome-swift.enum/committed)*