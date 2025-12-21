# PoseJointName

**Framework**: Vision  
**Kind**: associatedtype  
**Required**: Yes

A type that represents a joint name.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
associatedtype PoseJointName : Decodable, Encodable, Hashable, RawRepresentable where Self.PoseJointName.RawValue == String
```

## See Also

- [var availableJointNames: [Self.PoseJointName]](poseproviding/availablejointnames.md)
  The names of the available joints in the observation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/poseproviding/posejointname)*