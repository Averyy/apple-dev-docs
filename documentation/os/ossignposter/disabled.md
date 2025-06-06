# disabled

**Framework**: os  
**Kind**: property

A shared signposter that doesn’t emit signposts at runtime.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
static var disabled: OSSignposter { get }
```

#### Discussion

You can use the signposter this property returns to disable signposts in your production builds without having to refactor your code, as the following example demonstrates:

```swift
let signposter: OSSignposter
#if DEBUG
signposter = OSSignposter()
#else
signposter = OSSignposter.disabled
#endif
```

To determine if a signposter can emit signposts, use the [`isEnabled`](ossignposter/isenabled.md) property.

## See Also

- [init()](ossignposter/init.md)
  Creates a signposter that uses the default subsystem.
- [init(subsystem: String, category: String)](ossignposter/init(subsystem:category:)-94xpb.md)
  Creates a signposter that uses the specified subsystem and category.
- [init(subsystem: String, category: OSLog.Category)](ossignposter/init(subsystem:category:)-4vdri.md)
  Creates a signposter that uses the specified subsystem and system-defined log category.
- [init(logger: Logger)](ossignposter/init(logger:).md)
  Creates a signposter that uses the subsystem and category of an existing logger.
- [init(logHandle: OSLog)](ossignposter/init(loghandle:).md)
  Creates a signposter that uses the subsystem and category of an existing log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/ossignposter/disabled)*