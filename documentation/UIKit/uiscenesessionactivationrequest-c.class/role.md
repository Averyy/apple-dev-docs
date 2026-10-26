# role

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The role to request.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, readonly) UISceneSessionRole role;
```

#### Discussion

If you created the request using [`requestWithSession:`](./requestwithsession_.md), this property reflects the role of the `session`.

## See Also

### Managing request details
- [options](./options.md)
  Activation request options to further customize the request.
- [session](./session.md)
  The specific scene session to activate.
- [userActivity](./useractivity.md)
  A user activity to send to the newly activated scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenesessionactivationrequest-c.class/role)*