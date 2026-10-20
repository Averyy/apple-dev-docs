# dateComponents

**Framework**: User Notifications  
**Kind**: property  
**Role**: Instance Property

The date components to construct this object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var dateComponents: DateComponents { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSDateComponents * dateComponents;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSDateComponents * dateComponents;
```

#### Discussion

Use this property to review the date components associated with this trigger.

## See Also

### Getting the Trigger Information
- [func nextTriggerDate() -> Date?](./nexttriggerdate%28%29.md)
  The next date at which the trigger conditions are met.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/uncalendarnotificationtrigger/datecomponents)*