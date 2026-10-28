# requestWithRole:

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a scene session activation request object with a role that you provide.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) requestWithRole:(UISceneSessionRole) role;
```

## Return Value

A scene session activation request object.

## Discussion

Create an activation request with this method when you want the system to activate a scene session appropriate for the `role` and `userActivity` you provide. The system activates an existing scene session when the scene session’s [`role`](../uiscenesession/role-swift.property.md) matches the [`role`](./role.md) you request, and the user activity’s [`targetContentIdentifier`](../../Foundation/nsuseractivity/targetcontentidentifier.md) satisfies the scene’s [`activationConditions`](../uiscene/activationconditions.md). Otherwise, the system activates a new scene session.

## Parameters

- `role`: The role to request.

## See Also

### Creating a request
- [+ request](./request.md)
  Creates a scene session activation request object.
- [+ requestWithSession:](./requestwithsession_.md)
  Creates a scene session activation request object with a scene session that you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenesessionactivationrequest-c.class/requestwithrole:)*