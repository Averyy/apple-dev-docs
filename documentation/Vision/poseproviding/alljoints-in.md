# allJoints(in:)

**Framework**: Vision  
**Kind**: method  
**Required**: Yes

Retrieves a dictionary of all joints in the observation or joint group.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func allJoints(in groupName: Self.PoseJointsGroupName?) -> [Self.PoseJointName : Joint]
```

#### Return Value

The list of joints in the observation or joint group. If no `groupName` is specified, the system returns all joints in the observation..

## Parameters

- `groupName`: The group name to retrieve the joint names of.

## See Also

- [func joint(for: Self.PoseJointName) -> Joint?](poseproviding/joint(for:).md)
  Retrieves a joint for a given joint name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/poseproviding/alljoints(in:))*