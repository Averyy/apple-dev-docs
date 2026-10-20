# VSAccountAccessStatus.restricted

**Framework**: Video Subscriber Account  
**Kind**: case  
**Role**: Case

The app isn’t allowed to access subscription information.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case restricted
```

```c
VSAccountAccessStatusRestricted
```

#### Discussion

This status can result if parental controls prohibit the user from allowing access.

## See Also

### Statuses
- [VSAccountAccessStatus.denied](./denied.md)
  The user denied the app access to subscription information.
- [VSAccountAccessStatus.granted](./granted.md)
  The user allowed the app to access subscription information.
- [VSAccountAccessStatus.notDetermined](./notdetermined.md)
  The user hasn’t chosen whether to allow the app to access subscription information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountaccessstatus/restricted)*